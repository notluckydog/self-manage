#本文件用来显示登陆页面
#本文还需要实现人脸登录功能，键盘点击按钮W后台自动打开摄像头并进行识别，如果识别成功则登录成功
#人脸识别函数为face
import wx
import time
import os
#from dialog_detail import AboutDialog
#from dialog_detail import LoginDialog

ID_ABOUT = 201
username = "admin"
password = "admin"

class Login(wx.Frame):
    def __init__(self,parent=None,id=-1,UpdateUI=None,):
        super(Login,self).__init__(parent,size=(450,400),title=u'登录',
                                   style=wx.MINIMIZE|wx.SYSTEM_MENU|wx.CLOSE_BOX|wx.CAPTION)

        self.UpdateUI = UpdateUI
        self.is_login = False
        self.InitUI()


        ## 状态栏的创建
        self.setupStatusBar()
        # 显示菜单栏
        #self.setupMenuBar()
        ## 图标的实现
        self.setupIcon()

        self.Center()

    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour("white")
        #vbox = wx.BoxSizer(wx.VERTICAL)

        #ImageBox = wx.BoxSizer(wx.VERTICAL)

        #self.LoadImages()
        Box4 = wx.BoxSizer(wx.VERTICAL)

        Box1= wx.BoxSizer(wx.HORIZONTAL)
        str1 = wx.StaticText(panel,label = u"用户名:")
        self._text1 = wx.TextCtrl(panel)
        Box1.Add(str1,flag= wx.RIGHT,border=8)
        Box1.Add(self._text1,proportion =1)
        Box4.Add(Box1,border=6)

        Box4.Add((-1,10))

        Box2 = wx.BoxSizer(wx.HORIZONTAL)
        str2=wx.StaticText(panel,label=u"密   码:")
        self._text2=wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        Box2.Add(str2,flag = wx.RIGHT,border = 8)
        Box2.Add(self._text2,proportion =1)
        Box4.Add(Box2,border=6)

        Box4.Add((-1,10))




        Box3 = wx.BoxSizer(wx.HORIZONTAL)
        commit = wx.Button(panel,label=u"提交",size=(50, 30))
        commit.Bind(wx.EVT_BUTTON,self.Commit)
        Box3.Add(commit,flag =wx.Top,border = 6)
        Box4.Add(Box3,flag=wx.ALIGN_CENTER,border=16)

        Box4.Add((-1,10))

        Box5 = wx.BoxSizer(wx.VERTICAL)

        Login_image = wx.StaticBitmap(panel,
                                      wx.ID_ANY,wx.Bitmap("./image/地球_1.png",wx.BITMAP_TYPE_ANY))

        Box5.Add(Login_image,border =10)

        Box = wx.BoxSizer(wx.HORIZONTAL)
        Box.Add(Box5,flag=wx.ALIGN_CENTER)
        Box.Add(Box4,flag=wx.ALIGN_CENTER)





        panel.SetSizer(Box)

    def Commit(self,e):
        user_name=self._text1.GetValue()
        pass_word = self._text2.GetValue()
        if user_name==username:
            if pass_word==password:
                self.UpdateUI(1)

        else:
            print('fail')
            '''dlg = LoginDialog(None,-1)
            dlg.Show()'''

    def IS_Login(self):
        if self.is_login == True:
            return 1

    def OnKeyDown(self,e):
        #当用户按下键盘上enter按钮是默认为提交提交信息
        key = e.GetKeyCode()

        if key == wx.WXK_NUMPAD_ENTER:
            self.Commit()



    def setupIcon(self):
        ## 图标的实现
        self.img_path = os.path.abspath("./image/美食（水果）.png")
        print(self.img_path)
        icon = wx.Icon(self.img_path, type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

    def setupMenuBar(self):
        menubar = wx.MenuBar()
        aboutMenu = wx.Menu()
        aboutMenu.Append(ID_ABOUT, u'关于(&A)', 'More information about this program')
        menubar.Append(aboutMenu, u'帮助(&H)')
        self.SetMenuBar(menubar)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)

    def OnMenuAbout(self, event):
        dlg = AboutDialog(None, -1)
        dlg.ShowModal()
        dlg.Destroy()




    def setupStatusBar(self):

        sb = self.CreateStatusBar(2)
        self.SetStatusWidths([-1, -2])
        self.SetStatusText("Ready", 0)
        # timer
        self.timer = wx.PyTimer(self.Notify)  # derived from wx.Timer
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    #状态栏中显示时间格式
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d   %H:%M:%S', t)
        self.SetStatusText(st, 1)


def main():
    app = wx.App()
    lo= Login(None)
    lo.Show()
    app.MainLoop()

if __name__=='__main__':
    main()




