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

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Salir de la aplicación')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        self.SetSize((300, 200))
        self.SetTitle('Menú simple')
        self.Centre()
        self.Show(True)
    def OnQuit(self, e):
        self.Close()

# Main program
if __name__ == "__main__":                  # Especial function main
    app = wx.App(False)                     # Call framework WX
    frame = MyFrame(None, 'Lights Control with ESP32')   # Create frame 
    app.MainLoop()                          