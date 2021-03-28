import wx
import time
from utils.weather import weatherforlifestyle
from wx.lib.ticker import Ticker
import wx.lib.analogclock as ac

class BottomPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour('#F0F0F0')

        # Box1用来显示天气等相关信息
        '''Box1 = wx.BoxSizer(wx.VERTICAL)
        canshu = weatherforlifestyle()

        icon = canshu[0]
        text = canshu[1]
        temp = canshu[2]
        file = './assets/image/color-64/' + str(icon) + ".png"

        print(file)

        weather_image = wx.StaticBitmap(self,
                                        wx.ID_ANY, wx.Bitmap(file, wx.BITMAP_TYPE_ANY))
        Box1.Add(weather_image, flag=wx.ALIGN_CENTER, border=8)

        weather_text = wx.StaticText(self, label=str(text))
        Box1.Add(weather_text, flag=wx.RIGHT | wx.ALIGN_CENTER, border=8)

        weather_temp = wx.StaticText(self, label=str(text) + '   ' + str(temp) + "℃")
        Box1.Add(weather_temp, flag=wx.RIGHT | wx.ALIGN_CENTER)

        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d ', t)
        str2 = wx.StaticText(self, label=st)
        Box1.Add(str2, flag=wx.RIGHT | wx.ALIGN_CENTER)'''

        # 音乐播放按钮，手动开启
        play = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                               wx.BU_AUTODRAW | wx.BORDER_NONE)
        play.SetBitmap(wx.Bitmap('./assets/image/音乐.png', wx.BITMAP_TYPE_ANY))
        play.Bind(wx.EVT_BUTTON, self.MusicPlay)

        c1 = ac.AnalogClock(self, size=(150, 150))
        str3 = wx.StaticText(self, label='   ', size=(150, 20))

        self.ticker = Ticker(self)
        text_message = ' 功能尚未开放'

        # self.SetTickDirection("rtl")
        # self.SetTickFont(self.ticker.GetFont())
        self.ticker.SetText(text_message)
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        #sizer1.Add(sizer, flag=wx.LEFT, border=10)
        sizer1.AddSpacer(10)
        sizer1.Add(str3, border=30)
        sizer1.AddSpacer(20)
        sizer1.Add(play, border=10)
        sizer1.AddSpacer(20)

        sizer1.Add(self.ticker,flag = wx.EXPAND|wx.RIGHT, border=30)
        sizer1.AddSpacer(20)
        #sizer1.Add(Box1,flag = wx.RIGHT, border=10)
        sizer1.Add(c1, flag=wx.RIGHT, border=10)

        sizer2 =wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(sizer1,flag = wx.ALIGN_RIGHT|wx.RIGHT,border=10)

        self.SetSizer(sizer2)

    def MusicPlay(self):
        pass
