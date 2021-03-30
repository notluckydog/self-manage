import time

import wx
import os
from openpyxl import load_workbook
from .Dialogs import NotExsit, AddSuccess

path1 = os.path.abspath('..')
excel_path = './data/excel/2020-11.xlsx'

sampleList = ['很好', '较好', '一般', '较差', '很差']

class ClockDaily(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        #用来记录打卡项，也方便日后生成或者删除打卡项
        self.clock_list = ['时间','早起','早睡','日语','英语','记账','心情状况','身体状况']
        self.clock_data = ['否' for i in range(len(self.clock_list))]
        self.is_getup = '否'
        self.is_sleep = '否'
        self.is_Japanese = '否'
        self.is_English = '否'
        self.is_reading = '否'
        self.is_study = '否'
        self.is_study = '否'
        self.InitUi()

    def InitUi(self):
        Box1=wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self)

        self.SetBackgroundColour('white')

        self.str4 = wx.StaticText(self, label='   ', size=(90, 100))
        Box1.Add(self.str4, border=10)
        self.get_up = wx.CheckBox(self, label=u"早起", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.get_up)
        self.get_up.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.get_up, border=15)

        # 是否早睡
        self.sleep = wx.CheckBox(self, label=u"早睡", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.sleep)
        self.sleep.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.sleep, border=15)

        # 是否学习了日语
        self.Japanese = wx.CheckBox(self, label=u"日语学习", size=(90, 30))
        #self.Japanese.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.Japanese)
        self.Japanese.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.Japanese, border=15)

        # 是否背诵了英语单词
        self.English = wx.CheckBox(self, label=u"英语学习", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.English)
        self.English.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.English, border=15)

        # 是否进行了学习
        self.study = wx.CheckBox(self, label=u"学习", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.study)
        self.study.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.study, border=15)

        # 是否有做阅读
        self.reading = wx.CheckBox(self, label=u"阅读", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.reading)
        self.reading.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.reading, border=15)

        self.account = wx.CheckBox(self, label=u"记账", size=(90, 30))
        #self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.account)
        self.reading.SetValue(False)  # 设置当前是否被选中
        Box1.Add(self.account, border=15)

        # 心情状况
        Box3 = wx.BoxSizer(wx.HORIZONTAL)
        self.mood1 = wx.StaticText(self, label=u"心情状况", size=(50, 20))
        Box3.Add(self.mood1, border=5)
        Box3.AddSpacer(20)
        self.ch = wx.Choice(self, -1, (60, 50), choices=sampleList, )
        #self.Bind(wx.EVT_CHOICE, self.EvtChoice1, self.ch)
        Box3.Add(self.ch, flag=wx.EXPAND | wx.RIGHT, border=20)
        Box1.AddSpacer(10)
        Box1.Add(Box3, border=20)

        # 打卡项，身体状况
        Box4 = wx.BoxSizer(wx.HORIZONTAL)
        self.body1 = wx.StaticText(self, label=u"身体状况", size=(50, 20))

        Box4.Add(self.body1, border=15)
        Box4.AddSpacer(10)
        self.ch1 = wx.Choice(self, -1, (60, 50), choices=sampleList)
        #self.Bind(wx.EVT_CHOICE, self.EvtChoice2, self.ch1)
        Box4.Add(self.ch1, flag=wx.EXPAND | wx.RIGHT, border=20)

        Box1.AddSpacer(20)
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
                self.is_getup = '是'
            if self.sleep.GetValue():
                self.is_sleep = '是'
            if self.Japanese.GetValue():
                self.is_Japanese = '是'
            if self.English.GetValue():
                self.is_English ='是'

            if self.reading.GetValue():
                self.is_reading = '是'

            if self.study.GetValue():
                self.is_study = '是'
            if self.account.GetValue():
                self.is_study = '是'

        try:

            wb=load_workbook(excel_path)
            ws=wb['每日打卡']
            print("文件打开成功")
            c = ws['A1']
            b = int(c.value)  # excel 单元格第一格用来记录上次写入的位置
            a=ws['A'+str(b)]
            print('单元格获取成功')
            a = ws.cell(row=b, column=1)

        except:
            dlg = NotExsit(None, -1)
            dlg.ShowModal()
            dlg.Destroy()

        #用来防止误操作导致b的值与实际值不相符，再做一次判断
        while a.value:
            b += 1
            a = ws['A' + str(b)]
            if b >= 1500:
                break
        #写入数据
        try:
            print('写数据')
            ws['A'+str(b)]=time.strftime('%Y-%m-%d', time.localtime())
            print('1')
            ws['B'+str(b)]= self.is_getup
            print('2')
            ws['D'+str(b)]= self.is_Japanese
            print('3')
            ws['E'+str(b)]= self.is_English
            print('4')
            ws['F'+str(b)]=self.is_study
            print('5')
            ws['H'+str(b)]=self.is_reading
            print('6')
            ws['I'+str(b)]=self.is_sleep
            print('写入数据')
            ws['A'+1] = b+1
            wb.save(excel_path)
            print('写入成功')
            dlg = AddSuccess(None,-1)
            print('对话框')
            dlg.ShowModal()
            dlg.Destroy()

        except:
            dlg=NotExsit(None,-1)
            dlg.ShowModal()
            dlg.Destroy()


