import time

import wx
import wx.lib.gizmos as gizmos  # Formerly wx.gizmos in Classic

class LEDClock(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('white')
        led = gizmos.LEDNumberCtrl(self, -1,(300,200), (480, 100),
                              gizmos.LED_ALIGN_CENTER|gizmos.LED_DRAW_FADED)
        #gizmos.LED_ALIGN_CENTER|
        led.SetForegroundColour('white')
        led.SetBackgroundColour('black')

        self.clock = led
        self.OnTimer(None)

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(50)
        box.Add(self.clock,flag = wx.ALIGN_CENTER)


    def OnTimer(self, evt):
        t = time.localtime(time.time())
        st = time.strftime("%H:%M:%S", t)
        self.clock.SetValue(st)


    def ShutdownDemo(self):
        self.timer.Stop()
        del self.timer

class LEDClK(wx.Panel):
    def __int__(self,parent):
        super.__init__(parent)

        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour('black')

        font1 = wx.Font(36, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False)

        self.t_time = wx.StaticText(self)
        self.t_time.SetFont(font1)

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(50)
        box.Add(self.t_time,flag = wx.ALIGN_CENTER)

        self.SetSizer(box)

    def OnTimer(self,e):
        t = time.localtime(time.time())
        st = time.strftime("%H:%M:%S", t)
        self.t_time.SetValue(st)

