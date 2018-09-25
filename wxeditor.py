import wx

MENU_ICON = 1

class WxEditor(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(WxEditor,self).__init__(*args,**kwargs)
        self.InitUI()
  
    def InitUI(self):
        fonts = ['Times New Roman', 'Times', 'Courier', 'Courier New', 'Helvetica',
                'Sans', 'verdana', 'utkal', 'aakar', 'Arial']

        font_sizes = ['10','11','12','13','14','15','16','17','18']

        menubar = wx.MenuBar()

        filemenu = wx.Menu()
        menubar.Append(filemenu,'File')

        newi = wx.MenuItem(filemenu,MENU_ICON,'New\tCtrl+N')
        newi.SetBitmap(wx.Bitmap('menuicons/new.png'))
        filemenu.Append(newi)
        
        openi = wx.MenuItem(filemenu,MENU_ICON,'Open\tCtrl+O')
        openi.SetBitmap(wx.Bitmap('menuicons/open.png'))
        filemenu.Append(openi)

        filemenu.AppendSeparator()
        
        savei = wx.MenuItem(filemenu,MENU_ICON,'Save\tCtrl+S')
        savei.SetBitmap(wx.Bitmap('menuicons/save.png'))
        filemenu.Append(savei)

        save_asi = wx.MenuItem(filemenu,MENU_ICON,'Save As\tCtrl+Shift+S')
        save_asi.SetBitmap(wx.Bitmap('menuicons/save-as.png'))
        filemenu.Append(save_asi)

        filemenu.AppendSeparator()
        
        exiti = wx.MenuItem(filemenu,MENU_ICON,'Exit\tAlt+F4')
        exiti.SetBitmap(wx.Bitmap('menuicons/exit.png'))
        filemenu.Append(exiti)

        editmenu = wx.Menu()
        menubar.Append(editmenu,'Edit')

        undoi = wx.MenuItem(filemenu,MENU_ICON,'Undo\tCtrl+Z')
        undoi.SetBitmap(wx.Bitmap('menuicons/undo.png'))
        editmenu.Append(undoi)

        redoi = wx.MenuItem(filemenu,MENU_ICON,'Redo\tCtrl+Y')
        redoi.SetBitmap(wx.Bitmap('menuicons/redo.png'))
        editmenu.Append(redoi)

        editmenu.AppendSeparator()

        cuti = wx.MenuItem(filemenu,MENU_ICON,'Cut\tCtrl+X')
        cuti.SetBitmap(wx.Bitmap('menuicons/cut.png'))
        editmenu.Append(cuti)

        copyi = wx.MenuItem(filemenu,MENU_ICON,'Copy\tCtrl+C')
        copyi.SetBitmap(wx.Bitmap('menuicons/copy.png'))
        editmenu.Append(copyi)

        pastei = wx.MenuItem(filemenu,MENU_ICON,'Paste\tCtrl+V')
        pastei.SetBitmap(wx.Bitmap('menuicons/paste.png'))
        editmenu.Append(pastei)

        self.SetMenuBar(menubar)

        self.ToolBar = self.CreateToolBar()
        newt = self.ToolBar.AddTool(wx.ID_NEW,'',wx.Bitmap('toolicons/new.png'))
        opent = self.ToolBar.AddTool(wx.ID_OPEN,'',wx.Bitmap('toolicons/open.png'))
        savet = self.ToolBar.AddTool(wx.ID_SAVE,'',wx.Bitmap('toolicons/save.png'))
        save_ast = self.ToolBar.AddTool(wx.ID_SAVEAS,'',wx.Bitmap('toolicons/save-as.png'))
        self.ToolBar.AddSeparator()
        font = wx.ComboBox(self.ToolBar,value='Times',choices=fonts,size=(150,-1),style=wx.CB_DROPDOWN)
        self.ToolBar.AddControl(font)
        fontsize = wx.ComboBox(self.ToolBar,value='10',choices=font_sizes,size=(50,-1),style=wx.CB_DROPDOWN)
        self.ToolBar.AddControl(fontsize)
        self.ToolBar.AddSeparator()
        undot = self.ToolBar.AddTool(wx.ID_UNDO,'',wx.Bitmap('toolicons/undo.png'))
        redot = self.ToolBar.AddTool(wx.ID_REDO,'',wx.Bitmap('toolicons/redo.png'))
        cutt = self.ToolBar.AddTool(wx.ID_CUT,'',wx.Bitmap('toolicons/cut.png'))
        copyt = self.ToolBar.AddTool(wx.ID_COPY,'',wx.Bitmap('toolicons/copy.png'))
        pastet = self.ToolBar.AddTool(wx.ID_PASTE,'',wx.Bitmap('toolicons/paste.png'))
        self.ToolBar.Realize()

        self.SetTitle('WxEditor') 
        self.SetSize(900,700)   
        self.Center()

def main():
    app = wx.App()
    wxeditor = WxEditor(None)
    wxeditor.Show()
    app.MainLoop()        

if __name__=='__main__':
    main()    