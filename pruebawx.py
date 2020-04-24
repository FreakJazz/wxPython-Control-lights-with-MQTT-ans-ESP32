import wx  

class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title, size = (250,150))  
        self.InitUI() 
         
   def InitUI(self):    
        # In order to get principal menu
        menubar = wx.MenuBar() 
        # Elements of the principal menu
        fileMenu = wx.Menu() 
        aboutMenu = wx.Menu()
        helpMenu = wx.Menu()

        newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "Connect",kind = wx.ITEM_NORMAL)  
        fileMenu.AppendItem(newitem) 
            
        fileMenu.AppendSeparator()
            
        editMenu = wx.Menu() 
        copyItem = wx.MenuItem(editMenu, 100,text = "copy",kind = wx.ITEM_NORMAL)
         
        fileMenu.AppendMenu(wx.ID_ANY, "Control Light", editMenu) 

        fileMenu.AppendSeparator() 
        
        fileMenu.AppendSeparator() 
            
        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
            
        fileMenu.AppendItem(quit) 
        menubar.Append(fileMenu, '&Menu') 
        menubar.Append(aboutMenu, '&About')
        menubar.Append(helpMenu, '&Help')

        self.SetMenuBar(menubar)
		
        self.SetMenuBar(menubar) 
        self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
        self.Bind(wx.EVT_MENU, self.menuhandler) 
        self.SetSize((350, 250)) 
        self.Centre() 
        self.Show(True)
		
   def menuhandler(self, event): 
      id = event.GetId() 
      if id == wx.ID_NEW: 
         self.text.AppendText("new"+"\n")
			
ex = wx.App() 
Mywin(None,'MenuBar demo') 
ex.MainLoop()