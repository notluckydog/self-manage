import wx


class GameRun(wx.Panel):
    def __int__(self,parent):
        super.__init__(parent)
        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour('white')
        self.b_start = wx.Button(self,size = (50,20),label = u'开始游戏')
        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(50)
        box.Add(self.b_start,flag = wx.ALIGN_CENTER)

        self.SetSizer(box)