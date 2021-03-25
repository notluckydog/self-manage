#主页面视图

import wx
import wx.aui

from .left_panel import LeftPanel
from .right_panel import RightPanel
from .bottom_panel import BottomPanel


import os

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='天网系统',size=(800,600))
        self.aui_manager = wx.aui.AuiManager(self,wx.aui.AUI_MGR_TRANSPARENT_HINT)

        self.lay = BottomPanel(self)
        self.list = LeftPanel(self)
        self.detail = RightPanel(self)


        self.aui_manager.AddPane(self.lay,self._get_default_pane_info().Top().BestSize(-1,100))
        self.aui_manager.AddPane(self.list, self._get_default_pane_info().Left().Row(0).BestSize(300,-1))
        #self.aui_manager.AddPane(self.list_panel, self._get_default_pane_info().Left().Row(1).BestSize(250, -1).MinSize(150,-1))
        self.aui_manager.AddPane(self.detail, self._get_default_pane_info().CenterPane().Position(0).BestSize(400,-1))

        self.aui_manager.GetArtProvider().SetMetric(wx.aui.AUI_DOCKART_SASH_SIZE, 1)
        self.aui_manager.Update()

        self.Maximize(True)
        self._register_listeners()
        self.setupIcon()

    def setupIcon(self):
        ## 图标的实现
        self.img_path = './asset/image/美食（水果）.png'

        icon = wx.Icon(self.img_path, type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    def _get_default_pane_info(self):
        return wx.aui.AuiPaneInfo().CaptionVisible(False).PaneBorder(False).CloseButton(False).PinButton(False).Gripper(
            False)

    def on_frame_closing(self, e):
        self.aui_manager.UnInit()
        del self.aui_manager
        self.Destroy()

    def _register_listeners(self):
        self.Bind(wx.EVT_CLOSE, self.on_frame_closing)