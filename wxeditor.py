import wx
import wx.stc as stc
import wx.ribbon as RB
import os, time

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

        undoi = wx.MenuItem(editmenu,6,'Undo\tCtrl+Z','Undo')
        undoi.SetBitmap(wx.Bitmap('menuicons/undo.png'))
        editmenu.Append(undoi)

        redoi = wx.MenuItem(editmenu,7,'Redo\tCtrl+Y','Redo')
        redoi.SetBitmap(wx.Bitmap('menuicons/redo.png'))
        editmenu.Append(redoi)

        editmenu.AppendSeparator()

        cuti = wx.MenuItem(editmenu,8,'Cut\tCtrl+X','Cut')
        cuti.SetBitmap(wx.Bitmap('menuicons/cut.png'))
        editmenu.Append(cuti)

        copyi = wx.MenuItem(editmenu,9,'Copy\tCtrl+C','Copy')
        copyi.SetBitmap(wx.Bitmap('menuicons/copy.png'))
        editmenu.Append(copyi)

        pastei = wx.MenuItem(editmenu,10,'Paste\tCtrl+V','Paste')
        pastei.SetBitmap(wx.Bitmap('menuicons/paste.png'))
        editmenu.Append(pastei)

        editmenu.AppendSeparator()

        select_alli = wx.MenuItem(editmenu,11,'Select All\tCtrl+A','Select All')
        select_alli.SetBitmap(wx.Bitmap('menuicons/select-all.png'))
        editmenu.Append(select_alli)

        deletei = wx.MenuItem(editmenu,12,'Delete\tCtrl+D','Delete')
        deletei.SetBitmap(wx.Bitmap('menuicons/delete.png'))
        editmenu.Append(deletei)

        go_to_linei = editmenu.Append(wx.ID_ANY,"Go To Line\tCtrl+G",'Go To Line')

        findi = wx.MenuItem(editmenu,13,'Find\tCtrl+F','Find')
        findi.SetBitmap(wx.Bitmap('menuicons/find.png'))
        editmenu.Append(findi)

        datei = editmenu.Append(wx.ID_ANY,"Date/Time\tF5","Date/Time")

        viewmenu = wx.Menu()
        menubar.Append(viewmenu,'View')
        self.linenumberi = viewmenu.Append(wx.ID_ANY,'Show/Hide Line Number','Show/Hide Line Number',wx.ITEM_CHECK)
        self.statusbari = viewmenu.Append(wx.ID_ANY,'Show/Hide Status Bar','Show/Hide Status Bar',wx.ITEM_CHECK)

        viewmenu.Check(self.linenumberi.GetId(),True)
        viewmenu.Check(self.statusbari.GetId(),True)

        self.SetMenuBar(menubar)

        # current directory and file name
        self.dirname = ''
        self.filename = ''

        # set Default pos and size
        self.pos = 0
        self.size = 0

        # show and hide line number
        self.linenumberEnable = True

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
        self.Bind(wx.EVT_MENU, self.delete, deletei)
        self.Bind(wx.EVT_MENU, self.go_to_line, go_to_linei)
        self.Bind(wx.EVT_MENU, self.find_button, findi)
        self.Bind(wx.EVT_MENU, self.date_time, datei)

        self.Bind(wx.EVT_FIND, self.find)

        self.Bind(wx.EVT_MENU, self.show_hide_linenumber, self.linenumberi)
        self.Bind(wx.EVT_MENU, self.show_hide_statusbar, self.statusbari)

        # creating ribbon toolbar
        self.ribbon = RB.RibbonBar(self, wx.ID_ANY)

        home = RB.RibbonPage(self.ribbon, wx.ID_ANY, "",wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        file_panel = RB.RibbonPanel(home,wx.ID_ANY,"File",wx.NullBitmap,wx.DefaultPosition,wx.DefaultSize,RB.RIBBON_PANEL_DEFAULT_STYLE)
        ToolBar = RB.RibbonToolBar(file_panel, wx.ID_ANY)
        
        ToolBar.AddTool(wx.ID_NEW,wx.Bitmap('toolicons/new.png'),help_string='New')
        ToolBar.AddTool(wx.ID_OPEN,wx.Bitmap('toolicons/open.png'),help_string='Open')
        ToolBar.AddSeparator()
        ToolBar.AddTool(wx.ID_SAVE,wx.Bitmap('toolicons/save.png'),help_string='Save')
        ToolBar.AddTool(wx.ID_SAVEAS,wx.Bitmap('toolicons/save-as.png'),help_string='Save As')
        ToolBar.AddSeparator()
        ToolBar.AddTool(wx.ID_EXIT,wx.Bitmap('toolicons/exit.png'),help_string='Exit')

        sizer_panel = RB.RibbonPanel(home,wx.ID_ANY,"Font Sizer")

        comboBox_1 = wx.ComboBox(sizer_panel,wx.ID_ANY,"",wx.DefaultPosition,wx.DefaultSize,fonts,wx.CB_READONLY)
        comboBox_2 = wx.ComboBox(sizer_panel,wx.ID_ANY,"",wx.DefaultPosition,wx.DefaultSize,font_sizes,wx.CB_READONLY)

        comboBox_1.Select(7)
        comboBox_2.Select(0)

        comboBox_1.SetMinSize(wx.Size(150,-1))
        comboBox_2.SetMinSize(wx.Size(150,-1))

        combobox = wx.BoxSizer(wx.VERTICAL)
        combobox.Add(comboBox_1,0,wx.ALL|wx.EXPAND,3)
        combobox.Add(comboBox_2,0,wx.ALL|wx.EXPAND,3)
        sizer_panel.SetSizer(combobox)

        edit_panel = RB.RibbonPanel(home,wx.ID_ANY,"Edit",wx.NullBitmap,wx.DefaultPosition,wx.DefaultSize,RB.RIBBON_PANEL_DEFAULT_STYLE)
        ToolBar = RB.RibbonToolBar(edit_panel, wx.ID_ANY)

        ToolBar.AddTool(wx.ID_UNDO,wx.Bitmap('toolicons/undo.png'),help_string='Undo')
        ToolBar.AddTool(wx.ID_REDO,wx.Bitmap('toolicons/redo.png'),help_string='Redo')
        ToolBar.AddSeparator()
        ToolBar.AddTool(wx.ID_CUT,wx.Bitmap('toolicons/cut.png'),help_string='Cut')
        ToolBar.AddTool(wx.ID_COPY,wx.Bitmap('toolicons/copy.png'),help_string='Copy')
        ToolBar.AddTool(wx.ID_PASTE,wx.Bitmap('toolicons/paste.png'),help_string='Paste')
        ToolBar.AddSeparator()
        ToolBar.AddTool(wx.ID_SELECTALL,wx.Bitmap('toolicons/select-all.png'),help_string='Select All')
        ToolBar.AddTool(wx.ID_DELETE,wx.Bitmap('toolicons/delete.png'),help_string='Delete')
        ToolBar.AddTool(wx.ID_FIND,wx.Bitmap('toolicons/find.png'),help_string='Find')

        self.ribbon.Realize()

        # bind ribbon toolbar icons and functions
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.new, id=wx.ID_NEW)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.open_file, id=wx.ID_OPEN)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.save, id=wx.ID_SAVE)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.save_as, id=wx.ID_SAVEAS)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.exit, id=wx.ID_EXIT)

        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.undo, id=wx.ID_UNDO)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.redo, id=wx.ID_REDO)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.cut, id=wx.ID_CUT)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.copy, id=wx.ID_COPY)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.paste, id=wx.ID_PASTE)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.select_all, id=wx.ID_SELECTALL)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.delete, id=wx.ID_DELETE)
        self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.find_button, id=wx.ID_FIND)

        # creating textarea
        self.Text = stc.StyledTextCtrl(self,style=wx.TE_MULTILINE|wx.TE_WORDWRAP)

        # Hide horizontal scrollbar
        self.Text.SetUseHorizontalScrollBar(show=0) 

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
        self.Maximize(True)
        self.SetSize(900,700)
        self.Center()

        # attach ribbon panel with ribbon page 
        ribbonBox = wx.BoxSizer(wx.VERTICAL)
        ribbonBox.Add(self.ribbon, 0, wx.EXPAND)
        ribbonBox.Add(self.Text, 1, wx.EXPAND)
        self.SetSizer(ribbonBox)

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

    def delete(self, e):
        self.Text.Clear()

    def go_to_line(self, e):
        dlg = wx.TextEntryDialog(self,"Insert line number","Go To Line","",wx.TextEntryDialogStyle)
        if dlg.ShowModal()==wx.ID_OK:
            if dlg.GetValue().isdigit():
                self.Text.GotoLine(int(dlg.GetValue())-1)
            elif dlg.GetValue().isalnum():
                dlg_error = wx.MessageDialog(self,"Please enter line number","Error",wx.ICON_ERROR)
                if dlg_error.ShowModal()==wx.ID_OK:
                    while dlg.ShowModal()==wx.ID_OK:
                        if not dlg.GetValue():
                            dlg_error.ShowModal()
                        if dlg.GetValue().isdigit():
                            self.Text.GotoLine(int(dlg.GetValue())-1)
                            break 
                        if dlg.GetValue().isalnum():
                            dlg_error.ShowModal()    
            elif not dlg.GetValue():
                dlg_error = wx.MessageDialog(self,"Please enter line number","Error",wx.ICON_ERROR)
                if dlg_error.ShowModal()==wx.ID_OK:
                    while dlg.ShowModal()==wx.ID_OK:
                        if not dlg.GetValue():
                            dlg_error.ShowModal()                
                        if dlg.GetValue().isdigit():
                            self.Text.GotoLine(int(dlg.GetValue())-1)
                            break
                        if dlg.GetValue().isalnum():
                            dlg_error.ShowModal()    

    def find_button(self,e):
        self.txt = self.Text.GetValue()
        self.Data = wx.FindReplaceData()
        dlg = wx.FindReplaceDialog(self.Text,self.Data,'Find')
        dlg.Show()

    def find(self,e):
        self.Text.StartStyling(pos=0,mask=0xFF)
        self.Text.SetStyling(length=len(self.txt),style=0)
        find_text = e.GetFindString()
        self.size = len(find_text)
        while True:
            self.pos = self.txt.find(find_text,self.pos)
            if self.pos < 0:
                break
            self.Text.StyleSetSpec(1,'fore:#000000,back:#C0C0C0')
            self.Text.StartStyling(pos=self.pos,mask=0xFF)
            self.Text.SetStyling(length=self.size,style=1)
            self.pos += 1
        self.pos = 0    

    def date_time(self,e):
        date_time = time.strftime("%d %b %Y , %r ", time.localtime())
        self.Text.AddText(date_time)

    def show_hide_linenumber(self,e):
        if self.linenumberi.IsChecked():
            self.Text.SetMarginWidth(1,self.leftMarginWidth)
            self.Text.SetMargins(10,0)
            self.linenumberEnable = True
        else:
            self.Text.SetMarginWidth(1,0)
            self.Text.SetMargins(0,0)
            self.linenumberEnable = False    

    def show_hide_statusbar(self,e):
        if self.statusbari.IsChecked():
            self.CreateStatusBar()
            self.status(self)
        else:
            self.StatusBar.Destroy()    

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