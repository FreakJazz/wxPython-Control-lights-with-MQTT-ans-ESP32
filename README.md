<a name="top"></a>
# wxPython-Control-lights-with-MQTT-and-ESP32

![Topic Configuration](https://github.com/FreakJazz/Connection-MQTT-with-Python/blob/master/images/hiveMQ.JPG)
![Topic Configuration](https://github.com/FreakJazz/Connection-MQTT-with-Python/blob/master/images/publicMQTT.JPG)

<a name="item1"></a>
 ## Description

This project shows the control of three lights from wxPython to ESP32 through MQTT

<a name="item2"></a>
## Contents
- [Description](#item1)
- [Contents](#item2)
- [Library Installation](#item3)
- [Broker](#item4)
- [Programation](#item5)
- [Results](#item6)
- [Contributing](#item6)

[Up](#top)

<a name="item3"></a>
## Library Installation

In order to create a MQTT connection with Python 
We have to install *pip install paho-mqtt*
[Paho Library](https://pypi.org/project/paho-mqtt/)

### Installation
The latest stable version is available in the Python Package Index (PyPi) and can be installed using

``` pip install paho-mqtt
```

Or with virtualenv:

``` 
virtualenv paho-mqtt
source paho-mqtt/bin/activate
pip install paho-mqtt 
```
INCLUIR LA INST WX

[Up](#top)

<a name="item4"></a>
## Broker

After that, We need to open a Broker HIVEMQ
[Broker Address](https://www.hivemq.com/public-mqtt-broker/)

The following parameters must be considered to establish the connection
![Topic Configuration](https://github.com/FreakJazz/Connection-MQTT-with-Python/blob/master/images/broker.JPG/)

- **Host:**     broker.mqttdashboard.com
- **Port:**     1883 (Web Port)
- **ClientID:** This parameter is given by the user
- **Username:** This parameter is given by the user
- **Password:** This parameter is given by the user
- **Topic:**    This parameter is given by the user

[Up](#top)

<a name="item5"></a>
## Programation

### Python

#### Configure

In order to create a desktop application, the Tkinter Framework which is already installed in Python was used, so only the necessary libraries will be called to make the application.

``` python
###### IMPORT LYBRARIES ########
import ssl                          # Establish secure connection
import sys
import paho.mqtt.client as mqtt    # Connect with the MQTT Library
import time                         # Time Library  
from tkinter import *
from tkinter import ttk, font       # Import Tkinter Lybrary
from tkinter import messagebox
import getpass
```
#### Main

``` python
# Main program
if __name__ == "__main__":
    topic = str(input("Topic:   "))     # Input the topic in ""
    state = str(input("Data:   "))     # Input the data in ""
    print(topic)
    print(state)
    client.subscribe(topic, qos=0) 
    client.publish(topic, state)
    client.loop()

```

#### MQTT

Connection is stablish with:

```python
host = "broker.mqttdashboard.com"
port 1883;
keepalive = 60;
clientid = "ClientID";
username = "Your Username";
password = "Your Password";
topic = "YourTopic/#";
```
***The same parameters entered in the broker must be established***

Connection Function

``` python
####### FUNCTION ON CONNECT ######
def on_connect(client, userdata, flags, rc):
    print('Connected(%s)',client._client_id)
    client.subscribe(topic, qos=0) 
    client.publish(topic,'Connected')
```

Message Function

``` python
####### FUNCTION ON MESSAGE ######
def on_message(client, userdata, message):
    print('----------------------')
    print('topic: %s',  message.topic)
    print('payload: %s', message.payload)
    print('qos: %d', message.qos)
    print(message.payload.decode("utf-8"))
```

