import wx
import wx.dataview as dv

class LeftPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)


        self.InitUi()

    def InitUi(self):
        #新建树形
        self.SetBackgroundColour('black')

        self.tree = dv.DataViewTreeCtrl(self)

        self.root = self.tree.AppendContainer(dv.NullDataViewItem,
                                              u"功能列表")

        self.function = ['打卡','记账','监控','工具','游戏']
        self.clock = ['每日打卡','每月记录']
        self.account = ['每日记账','消费流水','月度情况','年度情况']
        self.monitor = ['实时数据','24小时趋势']
        self.tool = ['绘画板','计算器',]
        self.game = ['俄罗斯方块','贪吃蛇']
        self.icon_function = wx.Image


        child1 = self.tree.AppendContainer(self.root,u'打卡')
        child2 = self.tree.AppendContainer(self.root,u'记账')
        child3 = self.tree.AppendContainer(self.root,u'监控')
        child4 = self.tree.AppendContainer(self.root,u'工具')
        child5 = self.tree.AppendContainer(self.root,u'游戏')

        for x in range(len(self.clock)):
            self.tree.AppendContainer(child1,self.clock[x])

        for x in range(len(self.account)):
            self.tree.AppendContainer(child2,self.account[x])

        for x in range(len(self.monitor)):
            self.tree.AppendContainer(child3,self.monitor[x])

        for x in range(len(self.tool)):
            self.tree.AppendContainer(child4,self.tool[x])

        for x in range(len(self.game)):
            self.tree.AppendContainer(child5,self.game[x])

        font1 = wx.Font(16,wx.DEFAULT,style = wx.NORMAL,weight = wx.BOLD,underline =False)
        self.tree.SetFont(font1)

        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnTreeClick,self.tree)

        # Set the layout so the treectrl fills the panel
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(self.tree, 1, wx.EXPAND)

    def OnTreeClick(self,e):
        self.item = e.GetItem()
        print(self.item)







