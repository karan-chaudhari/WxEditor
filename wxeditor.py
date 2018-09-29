import wx
import wx.stc as stc
import os

class WxEditor(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(WxEditor,self).__init__(*args,**kwargs)
        self.InitUI()
  
    def InitUI(self):
        fonts = ["Arial","Courier New","Consolas","Clarendon","Comic Sans Ms",
                "MS Sans Serif","MS Serif","Times New Roman",
                "Serif","Symbol","System","Verdana"]

        font_sizes = ['10','11','12','13','14','15','16','17','18']

        # creating menubar
        menubar = wx.MenuBar()

        filemenu = wx.Menu()
        menubar.Append(filemenu,'File')

        newi = wx.MenuItem(filemenu,1,'New\tCtrl+N')
        newi.SetBitmap(wx.Bitmap('menuicons/new.png'))
        filemenu.Append(newi)
        
        openi = wx.MenuItem(filemenu,2,'Open\tCtrl+O')
        openi.SetBitmap(wx.Bitmap('menuicons/open.png'))
        filemenu.Append(openi)

        filemenu.AppendSeparator()
        
        savei = wx.MenuItem(filemenu,3,'Save\tCtrl+S')
        savei.SetBitmap(wx.Bitmap('menuicons/save.png'))
        filemenu.Append(savei)

        save_asi = wx.MenuItem(filemenu,4,'Save As\tCtrl+Shift+S')
        save_asi.SetBitmap(wx.Bitmap('menuicons/save-as.png'))
        filemenu.Append(save_asi)

        filemenu.AppendSeparator()
        
        exiti = wx.MenuItem(filemenu,5,'Exit\tAlt+F4')
        exiti.SetBitmap(wx.Bitmap('menuicons/exit.png'))
        filemenu.Append(exiti)

        editmenu = wx.Menu()
        menubar.Append(editmenu,'Edit')

        undoi = wx.MenuItem(filemenu,6,'Undo\tCtrl+Z')
        undoi.SetBitmap(wx.Bitmap('menuicons/undo.png'))
        editmenu.Append(undoi)

        redoi = wx.MenuItem(filemenu,7,'Redo\tCtrl+Y')
        redoi.SetBitmap(wx.Bitmap('menuicons/redo.png'))
        editmenu.Append(redoi)

        editmenu.AppendSeparator()

        cuti = wx.MenuItem(filemenu,8,'Cut\tCtrl+X')
        cuti.SetBitmap(wx.Bitmap('menuicons/cut.png'))
        editmenu.Append(cuti)

        copyi = wx.MenuItem(filemenu,9,'Copy\tCtrl+C')
        copyi.SetBitmap(wx.Bitmap('menuicons/copy.png'))
        editmenu.Append(copyi)

        pastei = wx.MenuItem(filemenu,10,'Paste\tCtrl+V')
        pastei.SetBitmap(wx.Bitmap('menuicons/paste.png'))
        editmenu.Append(pastei)

        self.SetMenuBar(menubar)

        # current directory and file name
        self.dirname = ''
        self.filename = ''

        # bind menu icons and functions
        self.Bind(wx.EVT_MENU, self.new, newi)
        self.Bind(wx.EVT_MENU, self.open_file, openi)

        self.Bind(wx.EVT_MENU, self.undo, undoi)
        self.Bind(wx.EVT_MENU, self.redo, redoi)
        self.Bind(wx.EVT_MENU, self.cut, cuti)
        self.Bind(wx.EVT_MENU, self.copy, copyi)
        self.Bind(wx.EVT_MENU, self.paste, pastei)

        # creating toolbar
        self.ToolBar = self.CreateToolBar()
        newt = self.ToolBar.AddTool(wx.ID_NEW,'',wx.Bitmap('toolicons/new.png'))
        opent = self.ToolBar.AddTool(wx.ID_OPEN,'',wx.Bitmap('toolicons/open.png'))
        savet = self.ToolBar.AddTool(wx.ID_SAVE,'',wx.Bitmap('toolicons/save.png'))
        save_ast = self.ToolBar.AddTool(wx.ID_SAVEAS,'',wx.Bitmap('toolicons/save-as.png'))
        self.ToolBar.AddSeparator()
        font = wx.ComboBox(self.ToolBar,value='Times New Roman',choices=fonts,size=(150,-1),style=wx.CB_DROPDOWN)
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

        # bind tool icons and functions
        self.Bind(wx.EVT_MENU, self.new, newt)
        self.Bind(wx.EVT_MENU, self.open_file, opent)

        self.Bind(wx.EVT_MENU, self.undo, undot)
        self.Bind(wx.EVT_MENU, self.redo, redot)
        self.Bind(wx.EVT_MENU, self.cut, cutt)
        self.Bind(wx.EVT_MENU, self.copy, copyt)
        self.Bind(wx.EVT_MENU, self.paste, pastet)

        # creating textarea
        self.Text = stc.StyledTextCtrl(self,style=wx.TE_MULTILINE|wx.TE_WORDWRAP) 

        # creating line number
        self.Text.SetMarginType(1,stc.STC_MARGIN_NUMBER)

        # set margin 10 pixels between line number and text
        self.Text.SetMargins(10,0)

        # set margin width
        self.leftMarginWidth = 35
        self.Text.SetMarginWidth(1,self.leftMarginWidth)

        # creating status bar 
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((220,220,220))

        self.SetTitle("Untitled" + " - WxEditor") 
        self.SetSize(900,700)   
        self.Center()

        # show line and column number
        self.Text.Bind(wx.EVT_KEY_UP,self.status)
        self.status(self)

    def new(self, e):
        self.dirname = ''
        self.Text.SetValue('')
        self.SetTitle("Untitled" + " - WxEditor")

    def open_file(self, e):
        try:
            dlg = wx.FileDialog(self,"Choose a file",self.dirname,"","*.*",wx.ID_OPEN)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                with open(os.path.join(self.dirname,self.filename),encoding='ANSI') as f:
                    content = f.read()
                    self.Text.SetValue(content)
                    self.SetTitle(self.filename + " - WxEditor")
                    f.close()
            dlg.Destroy()        
        except:
            dlg = wx.MessageDialog(self,"Could not open the file","Error",wx.ICON_ERROR)            
            dlg.ShowModal()
            dlg.Destroy()

    def undo(self, e):
        self.Text.Undo()

    def redo(self, e):
        self.Text.Redo()    

    def cut(self, e):
        self.Text.Cut()

    def copy(self, e):
        self.Text.Copy()

    def paste(self, e):
        self.Text.Paste()            

    def status(self, e):
        line = self.Text.GetCurrentLine()+1
        column = self.Text.GetColumn(self.Text.GetCurrentPos())
        stat = "Line %s, Column %s" % (line, column)
        self.StatusBar.SetStatusText(stat,0)
 
def main():
    app = wx.App()
    wxeditor = WxEditor(None)
    wxeditor.Show()
    app.MainLoop()        

if __name__=='__main__':
    main()    