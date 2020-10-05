/*
  SimpleMQTTClient.ino
  The purpose of this exemple is to illustrate a simple handling of MQTT and Wifi connection.
  Once it connects successfully to a Wifi network and a MQTT broker, it subscribe to a topic and send a message to it.
  It will also send a message delayed 5 seconds later.
*/

#include "EspMQTTClient.h"

EspMQTTClient client(
  "NETLIFE-FLIA. RODRIGUEZ",
  "172372rodriguez",
  "broker.mqttdashboard.com",  // MQTT Broker server ip
  "jazz23",   // Can be omitted if not needed
  "12345",   // Can be omitted if not needed
  "TestClient",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);

// the number of the LED pin
const int led1 = 2;  // 16 corresponds to GPIO16
const int led2 = 39;
const int led3 = 34;

// setting PWM properties
const int freq = 5000;
const int ledChannel1 = 0;
const int ledChannel2 = 0;
const int ledChannel3 = 0;
const int resolution = 8;

void setup()
{
  Serial.begin(115200);

  // Optionnal functionnalities of EspMQTTClient : 
  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater(); // Enable the web updater. User and password default to values of MQTTUsername and MQTTPassword. These can be overrited with enableHTTPWebUpdater("user", "password").
  client.enableLastWillMessage("TestClient/lastwill", "I am going offline");  // You can activate the retain flag by setting the third parameter to true
  
  // Output Configuration
  // configure LED PWM functionalitites
  ledcSetup(ledChannel1, freq, resolution);
  ledcSetup(ledChannel2, freq, resolution);
  ledcSetup(ledChannel2, freq, resolution);
  
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(led1, ledChannel1);
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(led2, ledChannel2);
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(led3, ledChannel3);
  
  pinMode(led1,OUTPUT);
  digitalWrite(led1,LOW);
  pinMode(led2,OUTPUT);
  digitalWrite(led2,LOW);
  pinMode(led3,OUTPUT);
  digitalWrite(led3,LOW);

}

// This function is called once everything is connected (Wifi and MQTT)
// WARNING : YOU MUST IMPLEMENT IT IF YOU USE EspMQTTClient
void onConnectionEstablished()
{
  // Subscribe to "mytopic/test" and display received message to Serial
  client.subscribe("dom/light1", [](const String & payload) {
    Serial.println(payload);
    uint32_t date = payload.toInt();
    date = ((date*1024)/100);
    ledcWrite(ledChannel1, date);
    Serial.println(date);
    
  });

  // Subscribe to "mytopic/wildcardtest/#" and display received message to Serial
  client.subscribe("dom/light2", [](const String & topic, const String & payload) {
    Serial.println(topic + ": " + payload);
    uint32_t date = payload.toInt();
    date = ((date*1024)/100);
    ledcWrite(ledChannel2, date);
    Serial.println(date);
  });
  // Subscribe to "mytopic/wildcardtest/#" and display received message to Serial
  client.subscribe("dom/light3", [](const String & topic, const String & payload) {
    Serial.println(topic + ": " + payload);
    uint32_t date = payload.toInt();
    date = ((date*1024)/100);
    ledcWrite(ledChannel3, date);
    Serial.println(date);
  });

  // Publish a message to "mytopic/test"
  client.publish("mytopic/test", "This is a message"); // You can activate the retain flag by setting the third parameter to true

  // Execute delayed instructions
  client.executeDelayed(5 * 1000, []() {
    client.publish("mytopic/test", "This is a message sent 5 seconds later");
  });
}

void loop()
{
  client.loop();
}
