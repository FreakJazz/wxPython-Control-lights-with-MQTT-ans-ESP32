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

class Principal(wx.Frame):
    def __init__(self, parent, title):
        
        wx.Frame.__init__(self, parent, title=title, size=(380,500))
        self.InitUI()
        self.Centre(True)
        self.Show(True)

    def InitUI(self):
        
        self.panel = wx.Panel(self)
        self.SetBackgroundColour("#FFFCF5")
        
        ##### FUNCTION PRINCIPAL #####
        # Light1
        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "LIGHT 1", pos=(10,10), size=(80,25))
        self.lbl_state1 = wx.StaticText(self, wx.ID_ANY, "State: ", pos=(10,40), size=(80,25))
        self.btn_light1 = wx.Button(self, wx.ID_ANY, "ON", pos=(300,70), size=(40,30))
        #self.sld1 = wx.Slider(self, -1, value=100, minValue=0, maxValue=250,style=wx.SL_HORIZONTAL)
        self.sld1 = wx.Slider(self, -1, 50, 0, 255, (10, 70), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        # Light2
        self.lbl_title2 = wx.StaticText(self, wx.ID_ANY, "LIGHT 2", pos=(10,150), size=(80,25))
        self.lbl_state2 = wx.StaticText(self, wx.ID_ANY, "State: ", pos=(10,180), size=(80,25))
        self.btn_light2 = wx.Button(self, wx.ID_ANY, "ON", pos=(300,210), size=(40,30))
        self.sld2 = wx.Slider(self, -1, 50, 0, 255, (10, 210), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        
        # Light3
        self.lbl_title3 = wx.StaticText(self, wx.ID_ANY, "LIGHT 3", pos=(10,290), size=(80,25))
        self.lbl_state3 = wx.StaticText(self, wx.ID_ANY, "State: ", pos=(10,320), size=(80,25))
        self.btn_light3 = wx.Button(self, wx.ID_ANY, "ON", pos=(300,340), size=(40,30))
        self.sld3 = wx.Slider(self, -1, 50, 0, 255, (10, 340), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar1, self.btn_light1)
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar2, self.btn_light2)
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar3, self.btn_light3)
        self.Bind(wx.EVT_SCROLL, self.OnSliderScroll1, self.sld1)
        self.Bind(wx.EVT_SCROLL, self.OnSliderScroll2, self.sld2)
        self.Bind(wx.EVT_SCROLL, self.OnSliderScroll3, self.sld3)

        # In order to get principal menu
        menubar = wx.MenuBar()
        # Elements of the principal menu
        fileMenu = wx.Menu() 
        aboutMenu = wx.Menu()
        helpMenu = wx.Menu()

        newitem = wx.MenuItem(fileMenu,wx.ID_NEW, text = "Connect",kind = wx.ITEM_NORMAL)  
        fileMenu.AppendItem(newitem)
        fileMenu.AppendSeparator()        
        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        fileMenu.AppendItem(quit)

        about = wx.MenuItem(aboutMenu,wx.ID_ABOUT, text = "About",kind = wx.ITEM_NORMAL)  
        aboutMenu.AppendItem(about)

        help1 = wx.MenuItem(helpMenu,wx.ID_ABOUT, text = "Help",kind = wx.ITEM_NORMAL)  
        helpMenu.AppendItem(help1)

        menubar.Append(fileMenu, '&Menu') 
        menubar.Append(aboutMenu, '&About')
        menubar.Append(helpMenu, '&Help')

        self.SetMenuBar(menubar)
        self.SetMenuBar(menubar) 
        #self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
        self.Bind(wx.EVT_MENU, self.menuhandler) 
    
    def OnSliderScroll1(self, event):
        self.obj1 = event.GetEventObject()
        self.val1 = self.obj1.GetValue()
    def OnSliderScroll2(self, event):
        self.obj2 = event.GetEventObject()
        self.val2 = self.obj2.GetValue()
    def OnSliderScroll3(self, event):
        self.obj3 = event.GetEventObject()
        self.val3 = self.obj3.GetValue()

    def menuhandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW: 
            self.config = MQTT_Config(None,"MQTT Config")
        if id == wx.ID_EXIT:
            qui = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',wx.YES_NO)
            ret = qui.ShowModal()
            if ret == wx.ID_YES:
                self.Close()
        print("config")
        print(self.config.get_host())

    def fn_Enviar1(self, event):
        print(self.val1)
        
    def fn_Enviar2(self, event):
        print(self.val2)
        
    def fn_Enviar3(self, event):
        print(self.val3)

class MQTT_Config(wx.Frame):
    
    def __init__(self, parent, title):
    # VARIABLES
        self.aux_connection = False

        wx.Frame.__init__(self, parent, title = title, size=(320, 350))
        self.InitMQTT() 
        self.Centre()
        self.Show()
    def InitMQTT(self):

        self.panel = wx.Panel(self)
        self.SetBackgroundColour("#FFFCF5")
        # CONFIGURACION MQTT
        # Etiquetas ...
        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "Configuration MQTT", pos=(10,10), size=(300,80))
        self.lbl_broker = wx.StaticText(self, wx.ID_ANY, "Broker: ", pos=(10,40), size=(80,25))
        self.lbl_port = wx.StaticText(self, wx.ID_ANY, "Port: ", pos=(10,70), size=(80,25))
        self.lbl_user = wx.StaticText(self, wx.ID_ANY, "Username: ", pos=(10,100), size=(80,25))
        self.lbl_pass = wx.StaticText(self, wx.ID_ANY, "Password: ", pos=(10,130), size=(80,25))
        self.lbl_topic = wx.StaticText(self, wx.ID_ANY, "Topic: ", pos=(10,160), size=(80,25))
        # Inputs
        self.txt_broker = wx.TextCtrl(self, wx.EXPAND|wx.ALL, "broker.mqttdashboard.com", pos=(100,40), size=(180,25))
        self.txt_port = wx.TextCtrl(self, wx.ID_ANY, "1883", pos=(100,70), size=(180,25))
        self.txt_user = wx.TextCtrl(self, wx.ID_ANY, "jazz23", pos=(100,100), size=(180,25))
        self.txt_pass = wx.TextCtrl(self, wx.ID_ANY, "12345", pos=(100,130), size=(180,25))
        self.txt_topic = wx.TextCtrl(self, wx.ID_ANY, "lights", pos=(100,160), size=(180,25))
        # Botones
        self.btn_connect = wx.Button(self, wx.ID_ANY, "Connect", pos=(55,210), size=(80,30))
        self.btn_disconnect = wx.Button(self, wx.ID_ANY, "Disconnect", pos=(140,210), size=(80,30))
        self.btn_Enviar1 = wx.Button(self, wx.ID_ANY, "Enviar1", pos=(10,270), size=(80,30))
        self.btn_Enviar2 = wx.Button(self, wx.ID_ANY, "Enviar2", pos=(90,270), size=(80,30))
        self.btn_Enviar3 = wx.Button(self, wx.ID_ANY, "Enviar3", pos=(180,270), size=(80,30))
        #Eventos
        self.Bind(wx.EVT_BUTTON, self.fn_connect, self.btn_connect)
        self.Bind(wx.EVT_BUTTON, self.fn_disconnect, self.btn_disconnect)
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar1, self.btn_Enviar1)
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar2, self.btn_Enviar2)
        self.Bind(wx.EVT_BUTTON, self.fn_Enviar3, self.btn_Enviar3)

        # Fonts style
        print(self.txt_broker)
        print(self.txt_port)
        self.lbl_prueba = wx.StaticText(self, wx.ID_ANY, "Disconnected", pos=(120,240), size=(123,25))

    ###### MQTT CONNECT FUNCTION ######
    def fn_connect(self, event):
        self.host = self.txt_broker.GetValue()
        self.port = int(self.txt_port.GetValue())
        self.username = self.txt_user.GetValue()
        self.password = self.txt_pass.GetValue()
        self.topic = self.txt_topic.GetValue()
        self.keepalive = 60
        self.clientid = "Clientjazz23"

        if self.username == "" or self.password == "" or self.host == "" or self.port == "" or self.topic == "":
            wx.MessageBox("You must enter all the required data", "Warning",style=wx.OK|wx.ICON_QUESTION)
            
        # elif self.username == "jazz23" and self.password == "12345":
            # self.lblconnect["text"]="SOME DATA ENTERED IS NOT CORRECT \n TRY AGAIN"
        else: 
            ##### FUNCTION PRINCIPAL #####
            self.client = mqtt.Client()     # Client Identifier
            self.client.on_connect = self.on_connect      # Conecction Function 
            self.client.on_message = self.on_message      # Message Function
            self.client.connect(self.host, self.port, self.keepalive)     # Host, terminal, keep alive
            self.client.username_pw_set(self.username,self.password)    # Username and Password
            #client.loop_forever()
            self.client.loop()
            

            self.lbl_prueba.SetLabelText("Connected")
  
    def send_mqtt(self, val, topic):
        self.val1 = val
        self.topic = topic
        self.client.subscribe(self.topic, qos=0)
        self.client.publish(self.topic,self.val)


    ####### FUNCTION DISCONNECT ######
    def fn_disconnect(self, event):
        self.client.disconnect()
        

    ####### FUNCTION ON CONNECT ######
    def on_connect(self,client, userdata, flags, rc):
        print('Connected(%s)',self.client._client_id)
        client.subscribe(self.topic, qos=0) 
        client.publish(self.topic,'Se establecio la conexion')

    ####### FUNCTION ON MESSAGE ######
    def on_message(self,client, userdata, message):
        print('----------------------')
        print('topic: %s',  message.topic)
        print('payload: %s', message.payload)
        print('qos: %d', message.qos)
        print(message.payload.decode("utf-8"))

    def fn_Enviar1(self, event):
        self.topic = "dom/light1"
        self.client.subscribe(self.topic, qos=0) 
        self.client.publish(self.topic, "soy la luz 1")
    def fn_Enviar2(self, event):
        self.topic = "dom/light2"
        self.client.subscribe(self.topic, qos=0) 
        self.client.publish(self.topic, "soy la luz 2")
    def fn_Enviar3(self, event):
        self.topic = "dom/light3"
        self.client.subscribe(self.topic, qos=0) 
        self.client.publish(self.topic, "soy la luz 3")
         
# Main program
if __name__ == "__main__":                  # Especial function main
    app = wx.App(False)                     # Call framework WX
    frame = Principal(None, "Lights Control with ESP32")   # Create frame 
    app.MainLoop()                          