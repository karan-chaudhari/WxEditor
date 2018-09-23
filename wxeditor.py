import wx

class WxEditor(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(WxEditor,self).__init__(*args,**kwargs)
        self.InitUI()
  
    def InitUI(self):
        menubar = wx.MenuBar()

        filemenu = wx.Menu()
        menubar.Append(filemenu,'File')
        filemenu.Append(wx.ID_NEW,'New\tCtrl+N')
        filemenu.Append(wx.ID_OPEN,'Open\tCtrl+O')
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_SAVE,'Save\tCtrl+S')
        filemenu.Append(wx.ID_SAVEAS,'Save As\tCtrl+Shift+S')
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,'Exit\tAlt+F4')

        editmenu = wx.Menu()
        menubar.Append(editmenu,'Edit')
        editmenu.Append(wx.ID_UNDO,'Undo\tCtrl+Z')
        editmenu.Append(wx.ID_REDO,'Undo\tCtrl+Y')
        editmenu.AppendSeparator()
        editmenu.Append(wx.ID_CUT,'Undo\tCtrl+X')
        editmenu.Append(wx.ID_COPY,'Undo\tCtrl+C')
        editmenu.Append(wx.ID_PASTE,'Undo\tCtrl+V')

        self.SetMenuBar(menubar)

        self.SetTitle('WxEditor') 
        self.SetSize(500,500)   
        self.Center()

def main():
    app = wx.App()
    wxeditor = WxEditor(None)
    wxeditor.Show()
    app.MainLoop()        

if __name__=='__main__':
    main()    