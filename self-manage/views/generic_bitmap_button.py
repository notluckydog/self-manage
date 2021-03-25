# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import wx
import images

class GenericBitmapButton(wx.BitmapButton):
    def __init__(self, parent, image_id,id):
        bitmap = getattr(images, image_id).GetBitmap()
        super().__init__(parent,bitmap=bitmap,style=wx.NO_BORDER,id = id)
        if wx.Platform == "__WXMSW__":
            self.SetBackgroundColour(parent.GetBackgroundColour())