import wx  



class Principal(wx.Frame): 

    

    def __init__(self, parent, title):
        # VARIABLES
        self.aux_connection = False

        wx.Frame.__init__(self, parent, title = title, size=(320, 130))
        self.InitUI() 
        self.Centre()
        self.Show()
            
    def InitUI(self):
        if (self.aux_connection == False):
            # Create elements
            sz = wx.BoxSizer(wx.VERTICAL)  
            btn_config_MQTT = wx.Button(self,-1, "MQTT Config")
            sz.Add(btn_config_MQTT,1,wx.EXPAND|wx.ALL, 100)
            # Events
            self.Bind(wx.EVT_BUTTON, self.click_MQTT, btn_config_MQTT)
        else:
            
            sz = wx.BoxSizer(wx.VERTICAL)  
            btn_out = wx.Button(self,-1, "Salir")
            sz.Add(btn_config_MQTT,1,wx.EXPAND|wx.ALL, 100)
            # Events
            self.Bind(wx.EVT_BUTTON, self.click_out, btn_out)
        print(self.aux_connection)
    def click_MQTT(self, event):
        print("It works")
        self.aux_connection = True
        MQTT_Config(None,"MQTT Config")

    def click_out(self, event):
        print("OUT")
        
        self.aux_connection = False
        
class MQTT_Config(wx.Frame):

    def __init__(self, parent, title):
    # VARIABLES
        self.aux_connection = False

        wx.Frame.__init__(self, parent, title = title, size=(320, 350))
        self.InitMQTT() 
        self.Centre()
        self.Show()
    def InitMQTT(self):
        # CONFIGURACION MQTT
        # Etiquetas ...
        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "Configuration MQTT", pos=(10,10), size=(200,25))
        self.lbl_broker = wx.StaticText(self, wx.ID_ANY, "Broker: ", pos=(10,40), size=(80,25))
        self.lbl_port = wx.StaticText(self, wx.ID_ANY, "Port: ", pos=(10,70), size=(80,25))
        self.lbl_user = wx.StaticText(self, wx.ID_ANY, "Username: ", pos=(10,100), size=(80,25))
        self.lbl_pass = wx.StaticText(self, wx.ID_ANY, "Password: ", pos=(10,130), size=(80,25))
        self.lbl_topic = wx.StaticText(self, wx.ID_ANY, "Topic: ", pos=(10,160), size=(80,25))
        # Inputs
        self.txt_broker = wx.TextCtrl(self, wx.EXPAND|wx.ALL, "Broker", pos=(100,40), size=(180,25))
        self.txt_port = wx.TextCtrl(self, wx.ID_ANY, pos=(100,70), size=(180,25))
        self.txt_user = wx.TextCtrl(self, wx.ID_ANY, pos=(100,100), size=(180,25))
        self.txt_pass = wx.TextCtrl(self, wx.ID_ANY, pos=(100,130), size=(180,25))
        self.txt_topic = wx.TextCtrl(self, wx.ID_ANY, pos=(100,160), size=(180,25))
        # Botones
        self.btn_connect = wx.Button(self, wx.ID_ANY, "Connect", pos=(55,210), size=(80,30))
        self.btn_disconnect = wx.Button(self, wx.ID_ANY, "Disconnect", pos=(140,210), size=(80,30))
        
        print(self.txt_broker)
        print(self.txt_port)
        
 
if __name__ == "__main__":                  # Especial function main
    ex = wx.App() 
    Principal(None,"Control Lights")        # Call Principal Window
    ex.MainLoop()
