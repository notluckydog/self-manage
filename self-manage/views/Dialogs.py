import wx


class AddSuccess(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self, parent, id, "添加成功 ", size=(350, 350))
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        str = wx.StaticText(self, -1, u"添加成功")
        but = wx.Button(self, wx.ID_OK)
        sizer2.Add(str, flag=wx.ALIGN_CENTER, border=10)
        sizer2.Add(but, flag=wx.ALIGN_CENTER)
        path = './assets/image/微笑.png'
        image = wx.StaticBitmap(self,
                                wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY))
        sizer1.Add(image,flag = wx.ALIGN_CENTER, border=10)
        sizer1.Add(sizer2,flag = wx.ALIGN_CENTER, border=10)

        self.SetSizer(sizer1)

class NotExsit(wx.Dialog):
    def __init__(self, parent, id):
        wx.Dialog.__init__(self, parent, id, "文件不存在", size=(350, 350))
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2=wx.BoxSizer(wx.VERTICAL)
        str = wx.StaticText(self, -1, u"文件不存在")
        but = wx.Button(self, wx.ID_OK)
        sizer2.Add(str, flag=wx.ALIGN_CENTER, border=10)
        sizer2.Add(but, flag=wx.ALIGN_CENTER)
        path='./assets/image/悲伤.png'
        image = wx.StaticBitmap(self,
                                      wx.ID_ANY, wx.Bitmap(path, wx.BITMAP_TYPE_ANY))
        sizer1.Add(image,flag = wx.ALIGN_CENTER,border=10)
        sizer1.Add(sizer2,flag = wx.ALIGN_CENTER,border=10)

        self.SetSizer(sizer1)