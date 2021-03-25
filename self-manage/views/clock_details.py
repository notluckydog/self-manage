import wx
import os
import wx.adv

class ClockDetail(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

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

        self.SetSizer(boxsizer)



    def OnDateChanged(self, evt):
        #self.log.write("OnDateChanged: %s\n" % evt.GetDate())

        date1 = evt.GetDate()
        print(date1)