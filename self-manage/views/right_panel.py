import wx
from .account_expenditure  import Expenditure
from .account_income import InCome
from .clock_daily import ClockDaily
from .clock_details import ClockDetail
from pubsub import pub
from .account_month import AccountMonth
from .acount_list import Account_List
from .account_year import AccountYear
from .tool_pic_to_pdf import Pic_to_PDF
from .tool_QR import QR
from .tool_Drawing import DoodleFrame
from .tool_LEDClock import LEDClock,LEDClK
from .game_Tetris import Tetris
from .game_run import GameRun


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
            self.panel =Account_List(self)

        if self.update == 13:
            self.panel = AccountMonth(self)
        if self.update ==14:
            self.panel = AccountYear(self)

        if self.update ==30:
            self.panel = DoodleFrame(self)

        if self.update ==31:
            pass

        if self.update ==32:
            self.panel = QR(self)

        if self.update ==33:
            self.panel = Pic_to_PDF(self)

        if self.update ==34:
            self.panel = LEDClock(self)

        if self.update ==40:
            self.panel = Tetris(self)

        if self.update ==41:
            pass

        if self.update ==42:
            self.panel = GameRun(self)


        # panel = RecordClock(self)
        # panel = Expenditure(self)
        #self.Sizer.Destroy()
        #self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.panel, 1, wx.EXPAND)
        self.Show()

