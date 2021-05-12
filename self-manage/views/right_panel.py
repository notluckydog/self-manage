import wx
from .account_expenditure  import Expenditure
from .account_income import InCome
from .clock_daily import ClockDaily
from .clock_details import ClockDetail
from pubsub import pub
from .account_month import AccountMonth
from .account_list import GridFrame
from .account_year import AccountYear
from .tool_pic_to_pdf import Pic_to_PDF
from .tool_QR import QR
from .tool_Drawing import DoodleFrame
from .tool_LEDClock import LEDClock



class RightPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        self.update =0
        pub.subscribe(self.get_update,'ui_update')
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel = ClockDaily(self)
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.panel, 1, wx.EXPAND)

    def get_update(self,note):
        #通过pub将传递的数字发送给右侧面板，根据面板的不同展示
        self.update = note

        if self.panel:
            #如果已经存在面板，那么先销毁该面板
            self.panel.Destroy()

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

            self.panel =GridFrame(self)

        if self.update == 13:
            self.panel = AccountMonth(self)

        if self.update ==14:
            self.panel = AccountYear(self)

        if self.update ==20:
            self.panel = DoodleFrame(self)

        if self.update ==21:
            self.panel = QR(self)

        if self.update ==22:
            self.panel = Pic_to_PDF(self)

        if self.update ==23:
            self.panel = LEDClock(self)

        self.Sizer.Add(self.panel, 1, wx.EXPAND)
        self.Show()

