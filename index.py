''' This program works with MQTT conection of 
IOT in order to turn on light in ESP32 from 
a desktop app with wxPython'''

###### IMPORT LYBRARIES ########
import ssl                          # Establish secure connection
import sys
import paho.mqtt.client as mqtt    # Connect with the MQTT Library
import time                         # Time Library
import wx
#print (wx.version())

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
        self.lbl_state1 = wx.StaticText(self, wx.ID_ANY, "The light 1 is ON ", pos=(10,40), size=(150,25))
        self.btn_light1 = wx.Button(self, wx.ID_ANY, label="ON", pos=(300,70), size=(40,30))
        #self.sld1 = wx.Slider(self, -1, value=100, minValue=0, maxValue=250,style=wx.SL_HORIZONTAL)
        self.sld1 = wx.Slider(self, -1, 50, 0, 100, (10, 70), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.btn_light1.Disable()
        self.sld1.Disable()

        # Light2
        self.lbl_title2 = wx.StaticText(self, wx.ID_ANY, "LIGHT 2", pos=(10,150), size=(80,25))
        self.lbl_state2 = wx.StaticText(self, wx.ID_ANY, "The light 1 is ON", pos=(10,180), size=(150,25))
        self.btn_light2 = wx.Button(self, wx.ID_ANY,label = "ON", pos=(300,210), size=(40,30))
        self.sld2 = wx.Slider(self, -1, 50, 0, 100, (10, 210), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.btn_light2.Disable()
        self.sld2.Disable()

        # Light3
        self.lbl_title3 = wx.StaticText(self, wx.ID_ANY, "LIGHT 3", pos=(10,290), size=(80,25))
        self.lbl_state3 = wx.StaticText(self, wx.ID_ANY, "The light 1 is ON", pos=(10,320), size=(150,25))
        self.btn_light3 = wx.Button(self, wx.ID_ANY, label = "ON", pos=(300,340), size=(40,30))
        self.sld3 = wx.Slider(self, -1, 50, 0, 100, (10, 340), (250, -1),wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.btn_light3.Disable()
        self.sld3.Disable()

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

        help1 = wx.MenuItem(helpMenu,wx.ID_HELP, text = "Help",kind = wx.ITEM_NORMAL)  
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
        val = self.val1
        topic = "dom/light1"
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class

    def OnSliderScroll2(self, event):
        self.obj2 = event.GetEventObject()
        self.val2 = self.obj2.GetValue()
        val = self.val2
        topic = "dom/light2"
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class

    def OnSliderScroll3(self, event):
        self.obj3 = event.GetEventObject()
        self.val3 = self.obj3.GetValue()
        val = self.val3
        topic = "dom/light3"
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class

    def menuhandler(self, event):
        id = event.GetId()
        # Connect with MQTT
        if id == wx.ID_NEW: 
            self.mqtt_class  = MQTT_Config(None,"MQTT Config")      #to get the class mqtt
        # Exit 
        if id == wx.ID_EXIT:
            qui = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',wx.YES_NO)
            ret = qui.ShowModal()
            if ret == wx.ID_YES:
                self.Close()
        # Help Window
        if id == wx.ID_HELP: 
            Help_wind(None,"Help")
        # About Window
        if id == wx.ID_ABOUT: 
            About_wind(None,"About")
        #print(self.config.get_host())

    def fn_Enviar1(self, event):
        state1 = self.btn_light1.GetLabel()
        if (state1== "ON"):
            self.sld1.Enable()
            self.btn_light1.SetLabel("OFF")
            self.lbl_prueba.SetLabelText("The light 1 is ON")
            val = 100
            
        if (state1== "OFF"):
            self.sld1.Disable()
            self.btn_light1.SetLabel("ON")
            self.lbl_prueba.SetLabelText("The light 1 is OFF")
            val = 0
        topic = "dom/light1"
        #self.btn_light1.Enable()
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class
        
    def fn_Enviar2(self, event):
        state2 = self.btn_light2.GetLabel()
        if (state2== "ON"):
            self.sld2.Enable()
            self.btn_light2.SetLabel("OFF")
            self.lbl_prueba.SetLabelText("The light 2 is ON")
            val = 100
            
        if (state2== "OFF"):
            self.sld2.Disable()
            self.btn_light2.SetLabel("ON")
            self.lbl_prueba.SetLabelText("The light 2 is OFF")
            val = 0
        topic = "dom/light2"
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class
        
    def fn_Enviar3(self, event):
        state3 = self.btn_light3.GetLabel()
        if (state3== "ON"):
            self.sld3.Enable()
            self.btn_light3.SetLabel("OFF")
            self.lbl_prueba.SetLabelText("The light 3 is ON")
            val = 100
            
        if (state3== "OFF"):
            self.sld3.Disable()
            self.btn_light3.SetLabel("ON")
            self.lbl_prueba.SetLabelText("The light 3 is OFF")
            val = 0
        topic = "dom/light3"
        self.mqtt_class.send_mqtt(val, topic)           # Send data to mqtt class

################ MQTT WINDOW ##################
class MQTT_Config(wx.Frame):
    
    def __init__(self, parent, title):
        # VARIABLES
        self.aux_connection = False
        wx.Frame.__init__(self, parent, title = title, size=(320, 300))
        self.InitMQTT() 
        self.Centre()
        self.Show()

    def InitMQTT(self):
        self.panel = wx.Panel(self)
        self.SetBackgroundColour("#FFFCF5")
        self.connect = 0
        # CONFIGURACION MQTT
        # Etiquetas ...
        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "Configuration MQTT", pos=(10,10), size=(300,80))
        self.lbl_broker = wx.StaticText(self, wx.ID_ANY, "Broker: ", pos=(10,40), size=(80,25))
        self.lbl_port = wx.StaticText(self, wx.ID_ANY, "Port: ", pos=(10,70), size=(80,25))
        self.lbl_user = wx.StaticText(self, wx.ID_ANY, "Username: ", pos=(10,100), size=(80,25))
        self.lbl_pass = wx.StaticText(self, wx.ID_ANY, "Password: ", pos=(10,130), size=(80,25))
        self.lbl_topic = wx.StaticText(self, wx.ID_ANY, "Topic: ", pos=(10,160), size=(80,25))
        # Inputs
        self.txt_broker = wx.TextCtrl(self, wx.ID_ANY, "broker.mqttdashboard.com", pos=(100,40), size=(180,25))
        self.txt_port = wx.TextCtrl(self, wx.ID_ANY, "1883", pos=(100,70), size=(180,25))
        self.txt_user = wx.TextCtrl(self, wx.ID_ANY, "jazz23", pos=(100,100), size=(180,25))
        self.txt_pass = wx.TextCtrl(self, wx.ID_ANY, "12345", pos=(100,130), size=(180,25))
        self.txt_topic = wx.TextCtrl(self, wx.ID_ANY, "lights", pos=(100,160), size=(180,25))
        # Buttons
        self.btn_connect = wx.Button(self, wx.ID_ANY, "Connect", pos=(70,200), size=(80,30))
        self.btn_disconnect = wx.Button(self, wx.ID_ANY, "Disconnect", pos=(170,200), size=(80,30))
        #Events
        self.Bind(wx.EVT_BUTTON, self.fn_connect, self.btn_connect)
        self.Bind(wx.EVT_BUTTON, self.fn_disconnect, self.btn_disconnect)
        # Fonts style
        print(self.txt_broker)
        print(self.txt_port)
        self.lbl_prueba = wx.StaticText(self, wx.ID_ANY, "State: ", pos=(10,240), size=(123,25))
        self.lbl_prueba = wx.StaticText(self, wx.ID_ANY, "Disconnected", pos=(100,240), size=(123,25))
        
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
            self.connect = 1
            frame.btn_light1.Enable()
            frame.sld1.Enable()
            frame.btn_light2.Enable()
            frame.sld2.Enable()
            frame.btn_light3.Enable()
            frame.sld3.Enable()
            self.txt_broker.Disable()
            self.txt_port.Disable()
            self.txt_user.Disable()
            self.txt_pass.Disable()
            self.txt_topic.Disable()
  
    def send_mqtt(self, val, topic):
        self.val = val
        self.topic = topic
        self.client.subscribe(self.topic, qos=0)
        self.client.publish(self.topic,self.val)

    ####### FUNCTION DISCONNECT ######
    def fn_disconnect(self, event):
        self.client.disconnect()
        self.lbl_prueba.SetLabelText("Disconnected")
        frame.btn_light1.Disable()
        frame.sld1.Disable()
        frame.btn_light2.Disable()
        frame.sld2.Disable()
        frame.btn_light3.Disable()
        frame.sld3.Disable()
        self.txt_broker.Enable()
        self.txt_port.Enable()
        self.txt_user.Enable()
        self.txt_pass.Enable()
        self.txt_topic.Enable()
        
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

############## Window About #################
class About_wind(wx.Frame):
        
    def __init__(self, parent, title):
    # VARIABLES
        self.aux_connection = False
        wx.Frame.__init__(self, parent, title = title, size=(400, 250))
        self.InitMQTT() 
        self.Centre()
        self.Show()
    def InitMQTT(self):
        self.panel = wx.Panel(self)
        self.SetBackgroundColour("#FFFCF5")
        text = "This project shows the control of three lights from wxPython to ESP32 through MQTT, the lights are connected to the analog ports of the ESP32 card to control the intensity of the lights to the desktop applications"
        text2 = "https://github.com/FreakJazz, https://www.linkedin.com/in/jazm%C3%ADn-rodr%C3%ADguez/"
        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "About", pos=(10,10), size=(300,80))

        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text, pos=(10,40), size=(380,60))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, "Making for: Jazmin Rodriguez", pos=(10,120), size=(380,40))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, "Contact:", pos=(10,155), size=(380,20))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text2, pos=(10,170), size=(380,60)) 

############## Window Help #################
class Help_wind(wx.Frame):
        
    def __init__(self, parent, title):
        # VARIABLES
        self.aux_connection = False
        wx.Frame.__init__(self, parent, title = title, size=(400, 250))
        self.InitMQTT() 
        self.Centre()
        self.Show()
    def InitMQTT(self):
        self.panel = wx.Panel(self)
        self.SetBackgroundColour("#FFFCF5")
        text = "1. You must connect the MQTT with the page http://www.hivemq.com/demos/websocket-client/ or the broker of your personal liking"
        text1 = "2. Subscribe to topics you have configured, send the values of each of the lights"
        text3 = "Enjoy!"
        text2 = "For more information check the repository on Github https://github.com/FreakJazz/wxPython-Control-lights-with-MQTT-and-ESP32"

        self.lbl_title1 = wx.StaticText(self, wx.ID_ANY, "Help", pos=(10,10), size=(300,80))

        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text, pos=(10,40), size=(380,60))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text1, pos=(10,100), size=(380,40))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text3, pos=(10,140), size=(380,20))
        self.lbl_text = wx.StaticText(self, wx.ID_ANY, text2, pos=(10,170), size=(380,60)) 

# Main program
if __name__ == "__main__":                  # Especial function main
    app = wx.App(False)                     # Call framework WX
    frame = Principal(None, "Lights Control with ESP32")   # Create frame 
    app.MainLoop()                          