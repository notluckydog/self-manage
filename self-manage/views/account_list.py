import sqlite3

import wx
import wx.grid
from openpyxl import load_workbook


class GridFrame(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #该面板用来展示最近的三十次消费记录
        self.x_time = []
        self.kind = []
        self.account = []
        self.remark = []

        self.get_data_db()
        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(30, 4)

        # We can set the sizes of individual rows and columns
        # in pixels
        '''grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)'''

        grid.SetColLabelValue(0,u'时间')
        grid.SetColLabelValue(1, u'消费种类')
        grid.SetColLabelValue(2, u'消费金额')
        grid.SetColLabelValue(3, u'备注')

        for i in range(0, len(self.x_time)):
            grid.SetCellValue(i, 0, self.x_time[i])
            grid.SetCellValue(i, 1, self.kind[i])
            grid.SetCellValue(i, 2, self.account[i])
            grid.SetCellValue(i, 3, self.remark[i])


        # And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')

        # We can specify that some cells are read.only
        #grid.SetCellValue(0, 3, 'This is read.only')
        #grid.SetReadOnly(0, 3)

        # Colours can be specified for grid cell contents
        '''grid.SetCellValue(3, 3, 'green on grey')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)'''

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        #grid.SetCellValue(0, 6, '3.1415')

        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(grid, 1, wx.EXPAND)
        self.Show()

        #self.Show()

    def get_data_db(self):
        #从数据库中获取数据
        try:
            # 尝试连接数据库
            conn = sqlite3.connect('my_record.db')
            # 创建游标
            cursor = conn.cursor()

            cursor.execute("SELECT XTime,KIND,ACCOUNT,REMARK FROM EXPENDITURES")

            # 循环获取前30条的数据
            batch = cursor.fetchmany(30)

            for row in batch:
                self.x_time.append(row[0])
                self.kind.append(row[1])
                self.account.append(str(row[2]))
                self.remark.append(row[3])

        except:
            dlg = wx.MessageDialog(self, '数据读取失败',
                                   '失败',
                                   wx.OK | wx.ICON_INFORMATION
                                   # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()

    


if __name__ == '__main__':

    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()
