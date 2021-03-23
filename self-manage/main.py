# -*- coding: utf-8 -*-

import wx
from views.main_frame import MainFrame
from views.login import Login

class NoteApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__=='__main__':
    app = NoteApp()
    app.MainLoop()
    print('1')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
