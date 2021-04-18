import matplotlib
import wx
import wx.adv
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from openpyxl import load_workbook
from views.Dialogs import NotExsit

excel_path = './data/excel/2020-11.xlsx'

class ClockDetail(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.clock_list = ['早起', '早睡', '日语', '英语', '记账', '心情','身体']
        self.InitUi()
        self.Center()


    def InitUi(self):
        boxsizer=wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('white')


        #获取相关数据
        data_mood,data_body,data_time = self.get_mood()
        self.f = Figure(figsize=(20,6),dpi=100,tight_layout=True)
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
        matplotlib.rcParams['axes.unicode_minus'] = False
        self.sub = self.f.add_subplot(2, 2, 1, title="身心状况")
        self.sub.plot(data_time,data_mood,color ='b',label = '心情状况')
        self.sub.plot(data_time,data_body,color ='g',label = '身体状况')
        #self.sub.autofmt_xdate()
        self.sub.grid(True)
        self.sub.set_xlabel('时间')
        self.sub.set_ylabel('状况')
        canvas = FigureCanvas(self, -1, self.f)
        canvas.draw()


        #获取相关信息
        get_up_num = self.get_data(2)
        sleep_num = self.get_data(3)
        Janpenese_num = self.get_data(4)
        english_num = self.get_data(5)
        account_num = self.get_data(8)


        font1 = wx.Font(16, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False)
        #用来陈述每一条习惯的坚持时间
        #用来记录早起
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box1.AddSpacer(20)
        self.t_1 = wx.StaticText(self,label = self.clock_list[0])
        self.t_1.SetFont(font1)
        #self.img_1 = wx.Image()
        self.t_1_1 = wx.StaticText(self,label = u'共坚持'+get_up_num+'天')
        self.t_1_1.SetFont(font1)
        box1.Add(self.t_1,border =10)
        #box1.Add(self.img_1,border =10)
        box1.Add(self.t_1_1,border =10)

        #用来记录早睡
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box2.AddSpacer(20)
        self.t_2 = wx.StaticText(self, label=self.clock_list[1])
        self.t_2.SetFont(font1)
        #self.img_2 = wx.Image()
        self.t_2_1 = wx.StaticText(self, label=u'共坚持'+sleep_num+'天')
        self.t_2_1.SetFont(font1)
        box2.Add(self.t_2, border=10)
        #box2.Add(self.img_2, border=10)
        box2.Add(self.t_2_1,border=10)

        # 用来记录日语坚持时间
        box3 = wx.BoxSizer(wx.HORIZONTAL)
        box3.AddSpacer(20)
        self.t_3 = wx.StaticText(self, label=self.clock_list[2])
        self.t_3.SetFont(font1)
        #self.img_3 = wx.Image()
        self.t_3_1 = wx.StaticText(self, label=u'共坚持'+Janpenese_num+'天')
        self.t_3_1.SetFont(font1)
        box3.Add(self.t_3, border=10)
        #box3.Add(self.img_3, border=10)
        box3.Add(self.t_3_1,  border=10)

        # 用来记录英语坚持
        box4 = wx.BoxSizer(wx.HORIZONTAL)
        box4.AddSpacer(20)
        self.t_4 = wx.StaticText(self, label=self.clock_list[3])
        self.t_4.SetFont(font1)
        #self.img_4 = wx.Image()
        self.t_4_1 = wx.StaticText(self, label=u'共坚持'+english_num+'天')
        self.t_4_1.SetFont(font1)
        box4.Add(self.t_4, border=10)
        #box4.Add(self.img_4, border=10)
        box4.Add(self.t_4_1,  border=10)

        # 用来记录记账坚持时间
        box5 = wx.BoxSizer(wx.HORIZONTAL)
        box5.AddSpacer(20)
        self.t_5 = wx.StaticText(self, label=self.clock_list[4])
        self.t_5.SetFont(font1)
        self.t_5_1 = wx.StaticText(self, label=u'共坚持'+account_num+'天')
        self.t_5_1.SetFont(font1)
        box5.Add(self.t_5, border=10)
        box5.Add(self.t_5_1, border=10)

        boxsizer.AddSpacer(50)
        boxsizer.Add(box1, flag=wx.ALIGN_CENTER)
        boxsizer.Add(box2, flag=wx.ALIGN_CENTER)
        boxsizer.Add(box3, flag=wx.ALIGN_CENTER)
        boxsizer.Add(box4, flag=wx.ALIGN_CENTER)
        boxsizer.Add(box5, flag=wx.ALIGN_CENTER)
        boxsizer.AddSpacer(50)
        boxsizer.Add(canvas,flag=wx.ALIGN_CENTER)



        self.SetSizer(boxsizer)

    def get_data(self,colu):
        #用来返回坚持天数
        #为了复用，采用一个函数,row为列号
        #输入不同的参数，得到不同的结果
        #从最新的一条数据开始，向上查找，若表格内信息不是'是',则退出
        count =0      #用来计数
        try:
            wb = load_workbook(excel_path)
            ws = wb['每日打卡']
            b = int(ws['A1'].value)  # excel 单元格第一格用来记录上次写入的位置
            a = ws.cell(row=b, column=colu)

        except:
            return -1

        while a.value=='是' and b>5:
            count+=1
            b-=1
            a = ws.cell(row = b,column = colu)
        return str(count)

    def get_mood(self):
        #用来返回心情状况与身体状况
        #遍历表格，将状况从很好、较好、一般、较差、很差转换成-2、-1、0、1、2
        #只返回六十条数据，如果数据量不够那就有多少条数据就读取多少条数据

        mood =[0*10]
        body =[0*10]
        X_time =[0*10]
        t_b =6
        #打开excel表格
        try:
            wb = load_workbook(excel_path)
            ws = wb['每日打卡']
            b =int(ws['A1'].value)      #用来读取终止的位置

        except:
            dlg = NotExsit(None, -1)
            dlg.ShowModal()
            dlg.Destroy()
            return mood,body,X_time
        n_count =0    #用来计数，如果数据超过60条，就不再进行查找
        if b>66:
            n_count =b-60

        else:
            n_count =6

        g = b
        for i in range(n_count,b+1):
            X_time.append(ws.cell(g,1).value)
            mood.append(self.str_to_num(ws.cell(g,9).value))
            body.append(self.str_to_num(ws.cell(g,10).value))
            g -=1

        return mood,body,X_time

    def str_to_num(self,t):
        #用来将'很好'等字符串转换为数字
        if t == '很好':
            return 2
        elif t ==' 较好':
            return 1

        elif t == '较差':
            return -1

        elif t == '很差':
            return -2

        else:
            return 0








