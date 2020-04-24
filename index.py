''' This program works with MQTT conection of 
IOT in order to turn on light in ESP32 from 
a desktop app with wxPython'''

###### IMPORT LYBRARIES ########
import ssl                          # Establish secure connection
import sys
import paho.mqtt.client as mqtt    # Connect with the MQTT Library
import time                         # Time Library
import wx
print (wx.version())

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        # Define Window
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
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
            
        controllightMenu = wx.Menu() 
        copyItem = wx.MenuItem(controllightMenu, 100,text = "copy",kind = wx.ITEM_NORMAL)   
        fileMenu.AppendMenu(wx.ID_ANY, "Control Light", controllightMenu) 

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

        # CONFIGURACION MQTT
        # Etiquetas ...
        self.labelA = wx.StaticText(self, wx.ID_ANY, "A", pos=(10,10), size=(80,25))
        self.labelB = wx.StaticText(self, wx.ID_ANY, "B", pos=(10,40), size=(80,25))
        self.labelR = wx.StaticText(self, wx.ID_ANY, "Resultado", pos=(10,70), size=(80,25))
        
        # Inputs
        self.A = wx.TextCtrl(self, wx.ID_ANY, pos=(100,10), size=(180,25))
        self.B = wx.TextCtrl(self, wx.ID_ANY, pos=(100,40), size=(180,25))
        self.R = wx.TextCtrl(self, wx.ID_ANY, pos=(100,70), size=(180,25))

        # Botones
        self.suma = wx.Button(self, wx.ID_ANY, "+", pos=(55,120), size=(40,30))
        self.resta = wx.Button(self, wx.ID_ANY, "-", pos=(105,120), size=(40,30))
        self.multiplicacion = wx.Button(self, wx.ID_ANY, "*", pos=(155,120), size=(40,30))
        self.division = wx.Button(self, wx.ID_ANY, "/", pos=(205,120), size=(40,30))

        self.Centre(True)

        # Active Window
        self.Show(True)

        self.SetSize((350, 250)) 
        self.Centre() 
        self.Show(True)
		
    def menuhandler(self, event): 
        id = event.GetId() 
        if id == wx.ID_NEW: 
            self.text.AppendText("new"+"\n")
        
# Main program
if __name__ == "__main__":                  # Especial function main
    app = wx.App(False)                     # Call framework WX
    frame = MyFrame(None, 'Lights Control with ESP32')   # Create frame 
    app.MainLoop()                          