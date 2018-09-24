import wx

MENU_ICON = 1

class WxEditor(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(WxEditor,self).__init__(*args,**kwargs)
        self.InitUI()
  
    def InitUI(self):
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