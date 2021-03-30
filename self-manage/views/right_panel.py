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
        '''self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.get_update,self.timer)
        self.timer.Start(milliseconds=-1, oneShot=True)'''
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel = ClockDaily(self)
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

