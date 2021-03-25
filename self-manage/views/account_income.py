import wx

from .generic_bitmap_button import GenericBitmapButton
import wx.adv
import time
from .my_Validator import MyNumberValidator
from wx import NewIdRef
from openpyxl import load_workbook
import images
import wx.lib.buttons as buttons
from .my_Validator import MyNumberValidator
from wx import NewId


imcome = ['薪资','退款','理财','兼职','还钱','借入','意外所得','报销','投资','其他']
ID_00 = NewId()
ID_01 = NewId()
ID_02 = NewId()
ID_03 = NewId()
ID_04 = NewId()
ID_05 = NewId()
ID_06 = NewId()
ID_07 = NewId()
ID_08 = NewId()
ID_09 = NewId()


class InCome(wx.Panel):
    
    def __init__(self,parent):
        super().__init__(parent)

        self.n_time = time.strftime('%Y-%m-%d', time.localtime())
        self.n_kind = imcome[0]
        self.n_acount = 0
        self.n_remark = '无'
        self.initUi()
        #self.Center()

    def initUi(self):
        self.SetBackgroundColour("white")

        box1 = wx.GridSizer(4,5,5,10)
        self.t_0= wx.StaticText(self,label = imcome[0])
        self.bt_0 = GenericBitmapButton(self,'_20',id = ID_00)
        self.bt_0.Bind(wx.EVT_BUTTON,self.KindSelect)

        self.t_1 = wx.StaticText(self, label=imcome[1])
        self.bt_1 = GenericBitmapButton(self, '_21',id= ID_01)
        self.bt_1.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_2 = wx.StaticText(self, label=imcome[2])
        self.bt_2 = GenericBitmapButton(self, '_22',id= ID_02)
        self.bt_2.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_3 = wx.StaticText(self, label=imcome[3])
        self.bt_3 = GenericBitmapButton(self, '_23',id= ID_03)
        self.bt_3.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_4 = wx.StaticText(self, label=imcome[4])
        self.bt_4 = GenericBitmapButton(self, '_24',id= ID_04)
        self.bt_4.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_5 = wx.StaticText(self, label=imcome[5])
        self.bt_5 = GenericBitmapButton(self, '_25',id= ID_05)
        self.bt_5.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_6 = wx.StaticText(self, label=imcome[6])
        self.bt_6 = GenericBitmapButton(self, '_26',id= ID_06)
        self.bt_6.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_7 = wx.StaticText(self, label=imcome[7])
        self.bt_7 = GenericBitmapButton(self, '_27',id= ID_07)
        self.bt_7.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_8 = wx.StaticText(self, label=imcome[8])
        self.bt_8 = GenericBitmapButton(self, '_28',id= ID_08)
        self.bt_8.Bind(wx.EVT_BUTTON, self.KindSelect)

        self.t_9 = wx.StaticText(self, label=imcome[9])
        self.bt_9 = GenericBitmapButton(self, '_29',id= ID_09)
        self.bt_9.Bind(wx.EVT_BUTTON, self.KindSelect)

        box1.AddMany([(self.bt_0,0,wx.EXPAND),(self.bt_1,0,wx.EXPAND),
                      (self.bt_2,0,wx.EXPAND),(self.bt_3,0,wx.EXPAND),
                      (self.bt_4,0,wx.EXPAND),
                      (self.t_0, 0, wx.LEFT),
                      (self.t_1, 0, wx.LEFT),(self.t_2, 0, wx.LEFT),
                      (self.t_3, 0, wx.LEFT),(self.t_4, 0, wx.LEFT),

                      (self.bt_5,0,wx.EXPAND),(self.bt_6,0,wx.EXPAND),
                      (self.bt_7,0,wx.EXPAND),(self.bt_8,0,wx.EXPAND),
                      (self.bt_9,0,wx.EXPAND),
                      (self.t_5, 0, wx.EXPAND),(self.t_6, 0, wx.EXPAND),
                      (self.t_7, 0, wx.EXPAND),
                      (self.t_8, 0, wx.EXPAND), (self.t_9, 0, wx.EXPAND),
                      ])

        box2 = wx.BoxSizer(wx.HORIZONTAL)

        self.time1 = wx.adv.DatePickerCtrl(self,style = wx.adv.DP_DROPDOWN
                                      | wx.adv.DP_SHOWCENTURY
                                      )

        self.Bind(wx.adv.EVT_DATE_CHANGED,self.OnDateSelect,self.time1)

        self.t_acount = wx.TextCtrl(self, -1,"金额",validator = MyNumberValidator())
        self.Bind(wx.EVT_TEXT,self.EvtText1,self.t_acount)

        box2.Add(self.time1,flag=wx.LEFT,border=10)
        box2.Add(self.t_acount,flag = wx.RIGHT|wx.EXPAND,border =10)

        self.t_remarks = wx.TextCtrl(self,-1, "备注",size = (50,100))
        self.Bind(wx.EVT_TEXT, self.EvtText2, self.t_remarks)

        self.bt_commit = wx.Button(self,-1,"提交")
        self.Bind(wx.EVT_BUTTON,self.Commit,self.bt_commit)

        box3 = wx.BoxSizer(wx.VERTICAL)

        box3.Add(box1,flag=wx.ALIGN_CENTER)
        box3.Add(box2,flag = wx.ALIGN_CENTER)
        box3.Add(self.t_remarks,flag=wx.EXPAND|wx.ALL,border=10)
        box3.Add(self.bt_commit,flag = wx.RIGHT)

        self.SetSizer(box3)

    def EvtText1(self,e):
        self.n_acount= float(e.GetString())

    def EvtText2(self,e):
        self.n_remark = e.GetString()

    def OnDateSelect(self,e):
        self.n_time = str(e.GetDate())

    def KindSelect(self,e):
        if e.GetId() == ID_00:
            self.n_kind = imcome[0]
        if e.GetId == ID_01:
            self.n_kind =imcome[1]
        if e.GetId == ID_02:
            self.n_kind =imcome[2]
        if e.GetId == ID_03:
            self.n_kind =imcome[3]
        if e.GetId == ID_04:
            self.n_kind =imcome[4]
        if e.GetId == ID_05:
            self.n_kind =imcome[5]
        if e.GetId == ID_06:
            self.n_kind =imcome[6]
        if e.GetId == ID_07:
            self.n_kind =imcome[7]
        if e.GetId == ID_08:
            self.n_kind =imcome[8]
        if e.GetId == ID_09:
            self.n_kind =imcome[9]

    def Commit(self,e):

        print(self.n_time)
        print(self.n_acount)

        print(self.n_remark)
        print(self.n_kind)

        try:

            wb= load_workbook('./data/account.xlsx')
            ws=wb['支出']
            #print("文件打开成功")
            #i_row = 1
            #i_column = 1
            b=1
            a=ws.cell(row = 1,column = 1)
            #print('单元格获取成功')
            #c=ws['A1']
            #print(c.value)

        except:
            dlg = wx.MessageDialog(self, '文件打开失败',
                                   '失败',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
            
        while a.value:
                #使用遍历的方式来对单元格进行检查
                #如果获取的单元格的内容为空，则表示可以写入
                #b参数为行数
            #print(b)
            #print(type(a.value))
            #print (len(a))
            

            b+=1
            #i_column +=1
            #print('行数是'+str(b))
            a=ws['A'+str(b)]
            #print(a.value)
            
            if b>=200:
                
                break
                #a = ws.cell(row = i_row,column = i_column)

            

        try:

            ws['A'+str(b)]=self.n_time
            #print('1')
            ws['B'+str(b)]=self.n_kind
            #print('2')
            ws['C'+str(b)]=self.n_acount
            #print('3')
            ws['D'+str(b)]=self.n_remark
            #print('4')

            wb.save('./data/account.xlsx')

        except:
            dlg = wx.MessageDialog(self, '数据写入失败',
                                   '失败',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        #print('文件写入成功')

       




def main():

    app = wx.App()
    ex = InCome(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

    

