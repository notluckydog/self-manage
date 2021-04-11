import wx
import os
import wx.adv

class ClockDetail(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.clock_list = ['早起', '早睡', '日语', '英语', '记账', '心情','身体']

        self.InitUi()
        self.Center()


    def InitUi(self):
        boxsizer=wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('white')
        dpc = wx.adv.DatePickerCtrl(self, size=(120, -1),
                                    style=wx.adv.DP_DROPDOWN
                                          | wx.adv.DP_SHOWCENTURY
                                          | wx.adv.DP_ALLOWNONE)
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        boxsizer.Add(dpc, 0, wx.ALL, 50)

        # In some cases the widget used above will be a native date
        # picker, so show the generic one too.
        # dpc = wx.adv.DatePickerCtrlGeneric(self, size=(120,-1),
        # style = wx.TAB_TRAVERSAL
        # | wx.adv.DP_DROPDOWN
        # | wx.adv.DP_SHOWCENTURY
        # | wx.adv.DP_ALLOWNONE )
        # self.Bind(wx.adv.EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        # sizer.Add(dpc, 0, wx.LEFT, 50)

        font1 = wx.Font(16, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False)
        #用来陈述每一条习惯的坚持时间
        #用来记录早起
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box1.AddSpacer(20)
        self.t_1 = wx.StaticText(self,label = self.clock_list[1])
        self.t_1.SetFont(font1)
        #self.img_1 = wx.Image()
        self.t_1_1 = wx.StaticText(self,label = u'共坚持')
        self.t_1_1.SetFont(font1)
        box1.Add(self.t_1,border =10)
        #box1.Add(self.img_1,border =10)
        box1.Add(self.t_1_1,border =10)

        #用来记录早睡
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        self.t_2 = wx.StaticText(self, label=self.clock_list[2])
        self.t_2.SetFont(font1)
        #self.img_2 = wx.Image()
        self.t_2_1 = wx.StaticText(self, label=u'共坚持')
        self.t_2_1.SetFont(font1)
        box2.Add(self.t_2, border=10)
        #box2.Add(self.img_2, border=10)
        box2.Add(self.t_2_1,border=10)

        # 用来记录早睡
        box3 = wx.BoxSizer(wx.HORIZONTAL)
        self.t_3 = wx.StaticText(self, label=self.clock_list[3])
        self.t_3.SetFont(font1)
        #self.img_3 = wx.Image()
        self.t_3_1 = wx.StaticText(self, label=u'共坚持')
        self.t_3_1.SetFont(font1)
        box3.Add(self.t_3, border=10)
        #box3.Add(self.img_3, border=10)
        box3.Add(self.t_3_1,  border=10)

        # 用来记录早睡
        box4 = wx.BoxSizer(wx.HORIZONTAL)
        self.t_4 = wx.StaticText(self, label=self.clock_list[4])
        self.t_4.SetFont(font1)
        #self.img_4 = wx.Image()
        self.t_4_1 = wx.StaticText(self, label=u'共坚持')
        self.t_4_1.SetFont(font1)
        box4.Add(self.t_4, border=10)
        #box4.Add(self.img_4, border=10)
        box4.Add(self.t_4_1,  border=10)

        # 用来记录早睡
        box5 = wx.BoxSizer(wx.HORIZONTAL)
        self.t_5 = wx.StaticText(self, label=self.clock_list[5])
        self.t_5.SetFont(font1)
        #self.img_5 = wx.Image()
        self.t_5_1 = wx.StaticText(self, label=u'共坚持')
        self.t_5.SetFont(font1)
        box5.Add(self.t_5, border=10)
        #box5.Add(self.img_5, border=10)
        box5.Add(self.t_5_1, border=10)

        boxsizer.Add(box1,border =10)
        boxsizer.Add(box2, border=10)
        boxsizer.Add(box3, border=10)
        boxsizer.Add(box4, border=10)
        boxsizer.Add(box5, border=10)

        self.SetSizer(boxsizer)



    def OnDateChanged(self, evt):
        #self.log.write("OnDateChanged: %s\n" % evt.GetDate())

        date1 = evt.GetDate()
        print(date1)