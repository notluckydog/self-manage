import wx
from .account_expenditure  import Expenditure
from .account_income import InCome
from .clock_daily import ClockDaily
from .clock_details import ClockDetail
from pubsub import pub
from .account_month import AccountMonth
from .acount_list import Account_list


class RightPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        self.update =0
        pub.subscribe(self.get_update,'ui_update')
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.get_update,self.timer)
        self.timer.Start(milliseconds=-1, oneShot=True)
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel = ClockDaily(self)
        #panel = RecordClock(self)
        #panel = Expenditure(self)
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.panel, 1, wx.EXPAND)

    def get_update(self,note):
        self.update = note
        if self.panel:
            self.panel.Destroy()
            #self.Sizer.Destroy()

        self.panel = wx.Panel(self)
        if self.update == 0:
            self.panel = ClockDaily(self)

        if self.update == 1:
            self.panel = ClockDetail(self)

        if self.update == 10:
            self.panel = Expenditure(self)

        if self.update == 11:
            self.panel = InCome(self)

        if self.update == 12:
            self.panel =Account_list(self)

        if self.update == 13:
            self.panel = AccountMonth(self)
        if self.update ==14:
            pass
        # panel = RecordClock(self)
        # panel = Expenditure(self)
        #self.Sizer.Destroy()
        #self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.panel, 1, wx.EXPAND)
        self.Show()

class RecordClock(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour('gray')
        sampleList = ['很好', '较好', '一般', '较差', '很差']
        Box1 = wx.BoxSizer(wx.VERTICAL)
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

        Box1.AddSpacer(10)

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
        Box.AddSpacer(20)
        Box.Add(Box2)
        Box.Add(Box1)

        self.SetSizer(Box)

    def EvtCheckBox(self, e):
        pass

    def EvtChoice1(self, e):
        pass

    def EvtChoice2(self, e):
        pass

    def OnClick(self, e):
        pass