import wx
import os
from openpyxl import load_workbook

path1 = os.path.abspath('..')
excel_path = path1 + '\\data\\excel'

sampleList = ['很好', '较好', '一般', '较差', '很差']

class ClockDaily(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.InitUi()




    def InitUi(self):
        Box1=wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self)

        self.SetBackgroundColour('white')

        self.str4 = wx.StaticText(self, label='   ', size=(90, 100))
        Box1.Add(self.str4, border=10)
        self.get_up = wx.CheckBox(self, label=u"早起", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.get_up)
        self.get_up.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.get_up, border=15)

        # 是否早睡
        self.sleep = wx.CheckBox(self, label=u"早睡", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.sleep)
        self.sleep.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.sleep, border=15)

        # 是否学习了日语
        self.Japanese = wx.CheckBox(self, label=u"日语学习", size=(90, 30))
        self.Japanese.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.Japanese)
        self.Japanese.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.Japanese, border=15)

        # 是否背诵了英语单词
        self.English = wx.CheckBox(self, label=u"英语学习", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.English)
        self.English.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.English, border=15)

        # 是否进行了学习
        self.study = wx.CheckBox(self, label=u"学习", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.study)
        self.study.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.study, border=15)

        # 是否有做阅读
        self.reading = wx.CheckBox(self, label=u"阅读", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.reading)
        self.reading.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.reading, border=15)

        self.account = wx.CheckBox(self, label=u"记账", size=(90, 30))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.account)
        self.reading.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.account, border=15)

        # 心情状况
        Box3 = wx.BoxSizer(wx.HORIZONTAL)
        self.mood1 = wx.StaticText(self, label=u"心情状况", size=(50, 20))
        Box3.Add(self.mood1, border=5)
        self.ch = wx.Choice(self, -1, (60, 50), choices=sampleList, )
        self.Bind(wx.EVT_CHOICE, self.EvtChoice1, self.ch)
        Box3.Add(self.ch, flag=wx.EXPAND | wx.RIGHT, border=20)

        Box1.Add(Box3, border=20)

        # 打卡项，身体状况
        Box4 = wx.BoxSizer(wx.HORIZONTAL)
        self.body1 = wx.StaticText(self, label=u"身体状况", size=(50, 20))
        Box4.Add(self.body1, border=15)
        self.ch1 = wx.Choice(self, -1, (60, 50), choices=sampleList)
        self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.ch1)
        Box4.Add(self.ch1, flag=wx.EXPAND | wx.RIGHT, border=20)

        Box1.Add(Box4, border=20)

        # 用来填充

        Box1.Add((-1, 10))
        # 提交按钮
        self.summit = wx.Button(self, label=u"提交", size=(90, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.summit)

        Box1.Add(self.summit, border=15)

        Box2 = wx.BoxSizer(wx.VERTICAL)
        str1 = wx.StaticText(panel, label=u"    ", size=(10, 10))
        Box2.Add(str1)

        Box = wx.BoxSizer(wx.HORIZONTAL)
        Box.Add(Box2)
        Box.Add(Box1)

        self.SetSizer(Box)



    def EvtCheckBox(self, e):
        if e.GetEventObject().GetLabel() == '早起':
            e.Skip()
        elif e.GetEventObject().GetLabel() == '早睡':
            e.Skip()
        elif e.GetEventObject().GetLabel() == '日语学习':
            e.Skip()
        elif e.GetEventObject().GetLabel() == '英语学习':
            e.Skip()
        elif e.GetEventObject().GetLabel() == '学习':
            e.Skip()
        elif e.GetEventObject().GetLabel() == '阅读':
            e.Skip()

    def EvtChoice1(self,e):
        pass

    def EvtChoice2(self,e):
        pass

    def OnClick(self, e):
        if e.GetEventObject() == self.summit:
            if self.get_up.GetValue():
                self.is_getup = 1
            if self.sleep.GetValue():
                self.is_sleep = 1
            if self.Japanese.GetValue():
                self.is_Japanese = 1
            if self.English.GetValue():
                self.is_English =1

            if self.reading.GetValue():
                self.is_reading = 1

            if self.study.GetValue():
                self.is_study = 1
            if self.account.GetValue():
                self.is_account = 1

        try:

            wb=load_workbook(excel_path)
            ws=wb['每日打卡']
            print("文件打开成功")
            b=5
            a=ws['A'+str(b)]
            print('单元格获取成功')
            while True:
                #使用遍历的方式来对单元格进行检查
                #如果获取的单元格的内容为空，则表示可以写入
                #b参数为行数
                if len(a)>=0:
                    b+=1
                    a = wx['A' + str(b)]

            ws['A'+str(b)]=st1
            ws['B'+str(b)]=is_getup
            ws['D'+str(b)]=is_Japanese
            ws['E'+str(b)]=is_English
            ws['F'+str(b)]=is_study
            ws['H'+str(b)]=is_reading
            ws['I'+str(b)]=is_sleep
            wb.save(path3)

            print('文件写入成功')




        except:
            dlg=NotExsit(None,-1)
            dlg.ShowModal()
            dlg.Destroy()


class AddSuccess(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self, parent, id, "添加成功 ", size=(350, 350))
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        str = wx.StaticText(self, -1, u"添加成功")
        but = wx.Button(self, wx.ID_OK)
        sizer2.Add(str, flag=wx.ALIGN_CENTER, border=10)
        sizer2.Add(but, flag=wx.ALIGN_CENTER)
        path = os.path.abspath('...') + '\image\\微笑.png'
        image = wx.StaticBitmap(self,
                                wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY))
        sizer1.Add(image, border=10)
        sizer1.Add(sizer2, border=10)

        self.SetSizer(sizer1)

class NotExsit(wx.Dialog):
    def __init__(self, parent, id):
        wx.Dialog.__init__(self, parent, id, " ", size=(350, 350))
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2=wx.BoxSizer(wx.VERTICAL)
        str = wx.StaticText(self, -1, u"文件不存在")
        but = wx.Button(self, wx.ID_OK)
        sizer2.Add(str, flag=wx.ALIGN_CENTER, border=10)
        sizer2.Add(but, flag=wx.ALIGN_CENTER)
        path=os.path.abspath('...')+'\image\\悲伤.png'
        image = wx.StaticBitmap(self,
                                      wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY))
        sizer1.Add(image,border=10)
        sizer1.Add(sizer2,border=10)

        self.SetSizer(sizer1)