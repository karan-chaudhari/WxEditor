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

        newi = wx.MenuItem(filemenu,1,'New\tCtrl+N','New File')
        newi.SetBitmap(wx.Bitmap('menuicons/new.png'))
        filemenu.Append(newi)
        
        openi = wx.MenuItem(filemenu,2,'Open\tCtrl+O','Open File')
        openi.SetBitmap(wx.Bitmap('menuicons/open.png'))
        filemenu.Append(openi)

        filemenu.AppendSeparator()
        
        savei = wx.MenuItem(filemenu,3,'Save\tCtrl+S','Save File')
        savei.SetBitmap(wx.Bitmap('menuicons/save.png'))
        filemenu.Append(savei)

        save_asi = wx.MenuItem(filemenu,4,'Save As\tCtrl+Shift+S','Save As')
        save_asi.SetBitmap(wx.Bitmap('menuicons/save-as.png'))
        filemenu.Append(save_asi)

        filemenu.AppendSeparator()
        
        exiti = wx.MenuItem(filemenu,5,'Exit\tAlt+F4','Exit')
        exiti.SetBitmap(wx.Bitmap('menuicons/exit.png'))
        filemenu.Append(exiti)

        editmenu = wx.Menu()
        menubar.Append(editmenu,'Edit')

        undoi = wx.MenuItem(filemenu,6,'Undo\tCtrl+Z','Undo')
        undoi.SetBitmap(wx.Bitmap('menuicons/undo.png'))
        editmenu.Append(undoi)

        redoi = wx.MenuItem(filemenu,7,'Redo\tCtrl+Y','Redo')
        redoi.SetBitmap(wx.Bitmap('menuicons/redo.png'))
        editmenu.Append(redoi)

        editmenu.AppendSeparator()

        cuti = wx.MenuItem(filemenu,8,'Cut\tCtrl+X','Cut')
        cuti.SetBitmap(wx.Bitmap('menuicons/cut.png'))
        editmenu.Append(cuti)

        copyi = wx.MenuItem(filemenu,9,'Copy\tCtrl+C','Copy')
        copyi.SetBitmap(wx.Bitmap('menuicons/copy.png'))
        editmenu.Append(copyi)

        pastei = wx.MenuItem(filemenu,10,'Paste\tCtrl+V','Paste')
        pastei.SetBitmap(wx.Bitmap('menuicons/paste.png'))
        editmenu.Append(pastei)

        select_alli = wx.MenuItem(filemenu,11,'Select All\tCtrl+A','Select All')
        select_alli.SetBitmap(wx.Bitmap('menuicons/select-all.png'))
        editmenu.Append(select_alli)

        self.SetMenuBar(menubar)

        # current directory and file name
        self.dirname = ''
        self.filename = ''

        # bind menu icons and functions
        self.Bind(wx.EVT_MENU, self.new, newi)
        self.Bind(wx.EVT_MENU, self.open_file, openi)
        self.Bind(wx.EVT_MENU, self.save, savei)
        self.Bind(wx.EVT_MENU, self.save_as, save_asi)
        self.Bind(wx.EVT_MENU, self.exit, exiti)

        self.Bind(wx.EVT_MENU, self.undo, undoi)
        self.Bind(wx.EVT_MENU, self.redo, redoi)
        self.Bind(wx.EVT_MENU, self.cut, cuti)
        self.Bind(wx.EVT_MENU, self.copy, copyi)
        self.Bind(wx.EVT_MENU, self.paste, pastei)
        self.Bind(wx.EVT_MENU, self.select_all, select_alli)

        # creating toolbar
        self.ToolBar = self.CreateToolBar()
        newt = self.ToolBar.AddTool(wx.ID_NEW,'',wx.Bitmap('toolicons/new.png'),'New')
        opent = self.ToolBar.AddTool(wx.ID_OPEN,'',wx.Bitmap('toolicons/open.png'),'Open')
        savet = self.ToolBar.AddTool(wx.ID_SAVE,'',wx.Bitmap('toolicons/save.png'),'Save')
        save_ast = self.ToolBar.AddTool(wx.ID_SAVEAS,'',wx.Bitmap('toolicons/save-as.png'),'Save As')
        exitt = self.ToolBar.AddTool(wx.ID_EXIT,'',wx.Bitmap('toolicons/exit.png'),'Exit')
        self.ToolBar.AddSeparator()
        font = wx.ComboBox(self.ToolBar,value='Times New Roman',choices=fonts,size=(150,-1),style=wx.CB_DROPDOWN)
        self.ToolBar.AddControl(font)
        fontsize = wx.ComboBox(self.ToolBar,value='10',choices=font_sizes,size=(50,-1),style=wx.CB_DROPDOWN)
        self.ToolBar.AddControl(fontsize)
        self.ToolBar.AddSeparator()
        undot = self.ToolBar.AddTool(wx.ID_UNDO,'',wx.Bitmap('toolicons/undo.png'),'Undo')
        redot = self.ToolBar.AddTool(wx.ID_REDO,'',wx.Bitmap('toolicons/redo.png'),'Redo')
        cutt = self.ToolBar.AddTool(wx.ID_CUT,'',wx.Bitmap('toolicons/cut.png'),'Cut')
        copyt = self.ToolBar.AddTool(wx.ID_COPY,'',wx.Bitmap('toolicons/copy.png'),'Copy')
        pastet = self.ToolBar.AddTool(wx.ID_PASTE,'',wx.Bitmap('toolicons/paste.png'),'Paste')
        select_allt = self.ToolBar.AddTool(wx.ID_SELECTALL,'',wx.Bitmap('toolicons/select-all.png'),'Select All')
        self.ToolBar.Realize()

        # bind tool icons and functions
        self.Bind(wx.EVT_MENU, self.new, newt)
        self.Bind(wx.EVT_MENU, self.open_file, opent)
        self.Bind(wx.EVT_MENU, self.save, savet)
        self.Bind(wx.EVT_MENU, self.save_as, save_ast)
        self.Bind(wx.EVT_MENU, self.exit, exitt)

        self.Bind(wx.EVT_MENU, self.undo, undot)
        self.Bind(wx.EVT_MENU, self.redo, redot)
        self.Bind(wx.EVT_MENU, self.cut, cutt)
        self.Bind(wx.EVT_MENU, self.copy, copyt)
        self.Bind(wx.EVT_MENU, self.paste, pastet)
        self.Bind(wx.EVT_MENU, self.select_all, select_allt)

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

        self.SetTitle("Untitled - WxEditor") 
        self.SetSize(900,700)   
        self.Center()

        # show line and column number
        self.Text.Bind(wx.EVT_KEY_UP,self.status)
        self.status(self)

    def new(self, e):
        self.dirname = ''
        self.filename = ''
        self.Text.SetValue('')
        self.SetTitle("Untitled - WxEditor")

    def open_file(self, e):
        try:
            dlg = wx.FileDialog(self,"Choose a file",self.dirname,"","*.*",wx.ID_OPEN)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                with open(os.path.join(self.dirname,self.filename),encoding='ANSI') as f:
                    self.Text.SetValue(f.read())
                    f.close()
                self.SetTitle(f"{self.filename} - WxEditor")    
            dlg.Destroy()        
        except:
            dlg = wx.MessageDialog(self,"Could not open the file","Error",wx.ICON_ERROR)            
            dlg.ShowModal()
            dlg.Destroy()

    def save(self, event=None):
        try:
            with open(os.path.join(self.dirname,self.filename),'w') as f:
                f.write(self.Text.GetValue())
                f.close()
        except:
            dlg = wx.FileDialog(self,"Save File",self.dirname,"","*.*",wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
            if (dlg.ShowModal()==wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                with open(os.path.join(self.dirname,self.filename),'w') as f:
                    f.write(self.Text.GetValue())
                    f.close()
                self.SetTitle(f"{self.filename} - WxEditor") 
            dlg.Destroy()    

    def save_as(self, e):
        try:
            dlg = wx.FileDialog(self,"Save As",self.dirname,self.filename,"*.*",wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
            if (dlg.ShowModal()==wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                with open(os.path.join(self.dirname,self.filename),'w') as f:
                    f.write(self.Text.GetValue())
                    f.close()
                self.SetTitle(f"{self.filename} - WxEditor")
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self,"Could not save file","Error",wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()            

    def exit(self, e):
        if self.Text.GetValue():
            dlg = wx.MessageDialog(self,"Do you want to save the changes?","Save?",wx.YES_NO|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if (result == wx.ID_YES):
                self.save()
                self.Close(True)     
            elif (result == wx.ID_NO):
                self.Close(True)      
            dlg.Destroy()    
        if not self.Text.GetValue():
            self.Close(True)            

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

    def select_all(self, e):
        self.Text.SelectAll()      

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