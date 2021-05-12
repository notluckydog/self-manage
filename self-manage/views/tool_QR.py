import wx

import qrcode
from PIL import Image
import time
import os
import wx.lib.imagebrowser as ib
from pyzbar import pyzbar
wildcard = "jpg   (*.jpg)|*.jpg|"     \
           "png   (*.png)|*.png|" \
           "All files (*.*)|*.*"


class QR(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        self.info = ' '
        self.fileImage='  '
        self.code = '  '
        self.initUi()
        self.Center()

    def initUi(self):
        self.SetBackgroundColour('white')

        self.t_info1 = wx.TextCtrl(self, -1, u"输入信息")
        self.Bind(wx.EVT_TEXT, self.TextChange1, self.t_info1)

        self.bt_commit1 = wx.Button(self, -1, u'生成二维码')
        self.Bind(wx.EVT_BUTTON, self.Commit1, self.bt_commit1)

        box3 = wx.BoxSizer(wx.HORIZONTAL)
        box3.Add(self.t_info1,flag = wx.EXPAND,border = 10)
        box3.AddSpacer(100)
        box3.Add(self.bt_commit1,flag = wx.RIGHT,border = 10)

        self.t_info = wx.TextCtrl(self,-1,u"输入信息")
        self.Bind(wx.EVT_TEXT,self.TextChange,self.t_info)

        self.bt_image = wx.Button(self,-1,u'选择图片')
        self.Bind(wx.EVT_BUTTON, self.ImageUp, self.bt_image)

        self.bt_commit = wx.Button(self,-1,u'生成二维码')
        self.Bind(wx.EVT_BUTTON, self.Commit, self.bt_commit)

        box1 = wx.BoxSizer(wx.HORIZONTAL)


        box1.AddSpacer(5)
        box1.Add(self.t_info,flag = wx.EXPAND,border=10)
        box1.AddSpacer(5)
        box1.Add(self.bt_image,flag = wx.RIGHT,border=10)
        box1.AddSpacer(10)
        box1.Add(self.bt_commit,flag = wx.RIGHT,border = 10)

        self.t_code = wx.TextCtrl(self, -1, u"识别信息",style =wx.TE_READONLY)


        self.bt_image2 = wx.Button(self, -1, u'选择图片')
        self.Bind(wx.EVT_BUTTON, self.ImageUp, self.bt_image2)

        self.bt_commit2 = wx.Button(self, -1, u'识别二维码')
        self.Bind(wx.EVT_BUTTON, self.Commit2, self.bt_commit2)

        box2 =wx.BoxSizer(wx.HORIZONTAL)
        box2.AddSpacer(5)
        box2.Add(self.t_code, flag=wx.EXPAND, border=10)
        box2.AddSpacer(5)
        box2.Add(self.bt_image2, flag=wx.RIGHT, border=10)
        box2.AddSpacer(10)
        box2.Add(self.bt_commit2, flag=wx.RIGHT, border=10)

        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(50)
        box.Add(box3,flag = wx.ALIGN_CENTER,border = 10)
        box.AddSpacer(10)
        box.Add(box1,flag = wx.ALIGN_CENTER,border =10)
        box.AddSpacer(10)
        box.Add(box2,flag = wx.ALIGN_CENTER,border = 10)


        self.SetSizer(box)

    def TextChange(self,e):
        self.info = e.GetString()

    def ImageUp(self,e):
        dir = os.getcwd()
        initial_dir = os.path.join(dir, 'bitmaps')
        dlg = ib.ImageDialog(self, initial_dir)

        dlg.Centre()

        if dlg.ShowModal() == wx.ID_OK:
            self.fileImage = dlg.GetFile()

        else:

            pass

        dlg.Destroy()


    def Commit(self,e):
        qr = qrcode.QRCode(
            version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data(self.info)
        qr.make(fit=True)

        img = qr.make_image()
        img = img.convert("RGBA")

        icon = Image.open(self.fileImage)  # 这里是二维码中心的图片

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)

        x_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        img.save(x_time+'.png')
        img.show()

    def Commit2(self,e):
        """
            获取二维码的结果
            :param image_input: 输入图片数据
            :param binary_max: 二值化的最大值
            :param binary_step: 每次递增的二值化步长
            :return: pyzbar 预测的结果
            """
        # 把输入图像灰度化

        self.icon = Image.open(self.fileImage)
        self.code = pyzbar.decode(self.icon)
        temp = self.code[0][0]


        self.t_code.SetValue(temp)

    def TextChange1(self,e):
        self.info = e.GetString()

    def Commit1(self,e):
        img = qrcode.make(self.info)
        x_time = time.strftime('img'+"%Y%m%d_%H%M%S", time.localtime())

        img.save(x_time+ '.png')
        img.show()