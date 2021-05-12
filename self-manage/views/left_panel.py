import wx
import wx.dataview as dv
from pubsub import pub

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        #self.update =0
        pub.sendMessage('ui_update', note=0)


        self.InitUi()

    def InitUi(self):
        panel = RecordDetail(self)
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(panel, 1, wx.EXPAND)


class RecordDetail(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        self.update =0
        #通过pypubsub来进行组件间通信
        pub.sendMessage('ui_update',note =0)

        self.InitUi()

    def InitUi(self):
        # 新建树形
        self.SetBackgroundColour('black')

        self.tree = wx.TreeCtrl(self,-1, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                               #| wx.TR_EDIT_LABELS
                               | wx.TR_MULTIPLE
                               | wx.TR_HIDE_ROOT)

        self.root = self.tree.AddRoot(u"功能列表")

        self.function = ['打卡', '记账', '监控', '工具', '游戏']
        self.clock = ['每日打卡', '每月记录']
        self.account = ['每日支出','每日收入', '消费流水', '月度情况', '年度情况']

        self.tool = ['绘画板','二维码生成器','图片转PDF','电子时钟' ]

        self.icon_function = wx.Image

        child1 = self.tree.AppendItem(self.root, u'打卡')
        child2 = self.tree.AppendItem(self.root, u'记账')
        child3 = self.tree.AppendItem(self.root, u'工具')


        for x in range(len(self.clock)):
            self.tree.AppendItem(child1, self.clock[x])

        for x in range(len(self.account)):
            self.tree.AppendItem(child2, self.account[x])

        for x in range(len(self.tool)):
            self.tree.AppendItem(child3, self.tool[x])



        font1 = wx.Font(16, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False)
        self.tree.SetFont(font1)

        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.OnTreeClick, self.tree)

        # Set the layout so the treectrl fills the panel
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.tree, 1, wx.EXPAND)

    def OnTreeClick(self, e):
        #绑定事件，用来处理点击条目做出的动作
        item =self.tree.GetItemText(e.GetItem())

        if item in self.clock :
            self.update = 0+self.clock.index(item)
            pub.sendMessage('ui_update', note=self.update)
            return self.update

        if item in self.account:
            self.update = 10+self.account.index(item)
            pub.sendMessage('ui_update', note=self.update)
            return self.update

        if item in self.tool:
            self.update = 20+self.tool.index(item)
            pub.sendMessage('ui_update', note=self.update)
            return self.update











