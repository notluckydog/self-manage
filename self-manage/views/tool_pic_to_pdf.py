import wx
import os
import img2pdf
from .Dialogs import AddSuccess,WriteFail

wildcard = "jpg   (*.jpg)|*.jpg|"     \
           "png   (*.png)|*.png|" \
           "All files (*.*)|*.*"

wildcard1 = "pdf    (*.pdf)|*.pdf|"   \
           "All files (*.*)|*.*"


class Pic_to_PDF(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        self.path_file = []
        self.file_name = '李白'
        self.path_save = ' '

        self.initUi()
        self.Center()

    def initUi(self):
        self.SetBackgroundColour('white')
        box1 = wx.BoxSizer(wx.VERTICAL)
        box1.AddSpacer(50)

        self.bt_file_choice = wx.Button(self,-1,label = u'选择照片')
        self.bt_file_choice.Bind(wx.EVT_BUTTON,self.file_choice)
        box1.Add(self.bt_file_choice,flag = wx.ALIGN_CENTER,border = 10)
        box1.AddSpacer(10)



        self.bt_file_save = wx.Button(self,-1,label = u'保存路径')
        self.bt_file_save.Bind(wx.EVT_BUTTON,self.path_chose,self.bt_file_save)
        box1.Add(self.bt_file_save,flag = wx.ALIGN_CENTER,border = 10)
        box1.AddSpacer(10)

        self.bt_sumit = wx.Button(self,-1,label=u'提交')
        self.bt_sumit.Bind(wx.EVT_BUTTON,self.summit,self.bt_sumit)
        box1.Add(self.bt_sumit,flag = wx.ALIGN_CENTER,border = 10)


        self.SetSizer(box1)

    def file_choice(self,e):
        dlg = wx.FileDialog(
             self,message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
        )


        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            self.path_file = dlg.GetPaths()

        dlg.Destroy()

    def path_chose(self,e):
        dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard=wildcard1, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )

        dlg.SetFilterIndex(2)

        if dlg.ShowModal() == wx.ID_OK:
            self.path_save = dlg.GetPath()


        dlg.Destroy()

    def summit(self,e):
        # specify paper size (A4)
        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        try:
            with open(self.path_save+".pdf", "wb") as f:
                f.write(img2pdf.convert(self.path_file, layout_fun=layout_fun))

            dlg = AddSuccess(None, -1)
            dlg.ShowModal()
            dlg.Destroy()

        except:
            dlg = WriteFail(None, -1)
            dlg.ShowModal()
            dlg.Destroy()




