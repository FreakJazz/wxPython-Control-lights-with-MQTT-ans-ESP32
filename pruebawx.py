###### IMPORT LYBRARIES ########
import ssl                          # Establish secure connection
import sys
import paho.mqtt.client as mqtt    # Connect with the MQTT Library
import time                         # Time Library  
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
        self.txt_broker = wx.TextCtrl(self, wx.EXPAND|wx.ALL, "broker.mqttdashboard.com", pos=(100,40), size=(180,25))
        self.txt_port = wx.TextCtrl(self, wx.ID_ANY, "1883", pos=(100,70), size=(180,25))
        self.txt_user = wx.TextCtrl(self, wx.ID_ANY, "jazz23", pos=(100,100), size=(180,25))
        self.txt_pass = wx.TextCtrl(self, wx.ID_ANY, "12345", pos=(100,130), size=(180,25))
        self.txt_topic = wx.TextCtrl(self, wx.ID_ANY, "lights", pos=(100,160), size=(180,25))
        # Botones
        self.btn_connect = wx.Button(self, wx.ID_ANY, "Connect", pos=(55,210), size=(80,30))
        self.btn_disconnect = wx.Button(self, wx.ID_ANY, "Disconnect", pos=(140,210), size=(80,30))

        #Eventos
        self.Bind(wx.EVT_BUTTON, self.fn_connect, self.btn_connect)
        self.Bind(wx.EVT_BUTTON, self.fn_disconnect, self.btn_disconnect)
        
        print(self.txt_broker)
        print(self.txt_port)
        self.lbl_prueba = wx.StaticText(self, wx.ID_ANY, "PRUEBA ", pos=(100,240), size=(123,25))

    ###### MQTT CONNECT FUNCTION ######
    def fn_connect(self, event):
        self.broker = self.txt_broker.GetValue()
        self.port = self.txt_port.GetValue()
        self.username = self.txt_user.GetValue()
        self.password = self.txt_pass.GetValue()
        self.topic = self.txt_topic.GetValue()

        if self.username == "" or self.password == "" or self.host == "" or self.port == "" or self.topic == "":
            wx.messagebox.showwarning("Warning", "You must enter all the required data")
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
            self.btn_connect.config(state = 'disable')
            self.btn_rf1.config(state = 'normal')
            self.lblconnect["text"]="Connected"
            self.broker1.config(state = 'disable')
            self.port1.config(state = 'disable')
            self.username1.config(state = 'disable')
            self.password1.config(state = 'disable')
            self.topic1.config(state = 'disable')

            self.lbl_prueba.SetLabelText(self.broker)

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
 
if __name__ == "__main__":                  # Especial function main
    ex = wx.App() 
    Principal(None,"Control Lights")        # Call Principal Window
    ex.MainLoop()
