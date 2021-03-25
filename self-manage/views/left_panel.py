import wx
import wx.dataview as dv
from pubsub import pub

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        self.update =0


        self.InitUi()

    def InitUi(self):
        panel = RecordDetail(self)
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(panel, 1, wx.EXPAND)


class RecordDetail(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)
        pub.sendMessage('ui_update',note =0)

        self.InitUi()

    def InitUi(self):
        # 新建树形
        self.SetBackgroundColour('black')

        self.tree = wx.TreeCtrl(self,-1, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                               #| wx.TR_EDIT_LABELS
                               | wx.TR_MULTIPLE)
                               #| wx.TR_HIDE_ROOT

        self.root = self.tree.AddRoot(u"功能列表")

        self.function = ['打卡', '记账', '监控', '工具', '游戏']
        self.clock = ['每日打卡', '每月记录']
        self.account = ['每日支出','每日收入', '消费流水', '月度情况', '年度情况']
        self.monitor = ['实时数据', '24小时趋势']
        self.tool = ['绘画板', '计算器', ]
        self.game = ['俄罗斯方块', '贪吃蛇']
        self.icon_function = wx.Image

        child1 = self.tree.AppendItem(self.root, u'打卡')
        child2 = self.tree.AppendItem(self.root, u'记账')
        child3 = self.tree.AppendItem(self.root, u'监控')
        child4 = self.tree.AppendItem(self.root, u'工具')
        child5 = self.tree.AppendItem(self.root, u'游戏')

        for x in range(len(self.clock)):
            self.tree.AppendItem(child1, self.clock[x])

        for x in range(len(self.account)):
            self.tree.AppendItem(child2, self.account[x])

        for x in range(len(self.monitor)):
            self.tree.AppendItem(child3, self.monitor[x])

        for x in range(len(self.tool)):
            self.tree.AppendItem(child4, self.tool[x])

        for x in range(len(self.game)):
            self.tree.AppendItem(child5, self.game[x])

        font1 = wx.Font(16, wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False)
        self.tree.SetFont(font1)

        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.OnTreeClick, self.tree)

        # Set the layout so the treectrl fills the panel
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.tree, 1, wx.EXPAND)

    def OnTreeClick(self, e):

        item =self.tree.GetItemText(e.GetItem())

        if item in self.clock :
            self.update = 0+self.clock.index(item)
            print(self.update)
            return self.update

        if item in self.account:
            self.update = 10+self.account.index(item)
            print(self.update)
            return self.update

        if item in self.monitor:
            self.update = 20+self.monitor.index(item)
            print(self.update)
            return self.update

        if item in self.tool:
            self.update = 30+self.tool.index(item)
            print(self.update)
            return self.update

        if item in self.game:
            self.update = 40+self.game.index(item)
            print(self.update)
            return self.update

        pub.sendMessage('ui_update',note=self.update)

    #def updatedisplay(self):
        #pub.sendMessage(self.update,'ui_update')









