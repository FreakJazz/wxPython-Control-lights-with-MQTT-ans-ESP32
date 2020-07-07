#include <WiFi.h>
#include <PubSubClient.h>
 
WiFiClient espClient;
PubSubClient client(espClient);

// Select NODE
const char* host = "broker.mqttdashboard.com";         //'broker.mqttdashboard.com';
const int port = 1883;
const int keepalive = 60;
const char* clientid = "Clientjazz23";
const char* username = "jazz23";
const char* password = "12345";
const char* topic = "dom/light2";
const char* topic_subscribe1 = "dom/light1";
const char* topic_subscribe2 = "dom/light2";
const char* topic_subscribe3 = "dom/light3";

const char* ssid = "NETLIFE-FLIA. RODRIGUEZ";
const char* pass = "172372rodriguez";
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

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

void callback(char* topic, byte* payload, unsigned int length) {
  String incoming = "";
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] "); 
  for (int i=0;i<length;i++) {
    incoming += (char)payload[i];
    Serial.print(incoming);
  }

  //String(incoming).toInt();
  uint32_t date = incoming.toInt();

  date = ((date*1024)/100);
  Serial.println(date);
  if (topic==topic_subscribe1){
    Serial.println("entro en el 1");
    ledcWrite(ledChannel1, date);
    }
  if (topic==topic_subscribe2){
    Serial.println("entro en el 2");
    ledcWrite(ledChannel2, date);
    }
  if (topic==topic_subscribe3){
    Serial.println("entro en el 3");
    ledcWrite(ledChannel3, date);
    }
}

// Reconected MQTT fuction
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    //clientid += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientid, username, password)) {
      Serial.println("Connected");
      // Once connected, publish an announcement...
      client.publish(topic,"Hello");
      // ... and resubscribe
      client.subscribe(topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    } 
  }
}

void setup()
{
  // Serial comunication init
  Serial.begin(115200);
  // Wifi Connection
  delay(10);
  Serial.println(" Connecting SSID: ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");}
  Serial.println("");
  Serial.println("WIFI Connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // MQTT Connection
  client.setServer(host, port);
  client.setCallback(callback);
  // Allow the hardware to sort itself out
  delay(1500);

  // Output Configuration
  // configure LED PWM functionalitites
  ledcSetup(ledChannel1, freq, resolution);
  
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

void loop()
{
  if (!client.connected()) {
    reconnect();
  }

  if (client.connected()){
     while (client.connected()){
     //////////////
       delay(10);
       client.subscribe(topic_subscribe1,0);
       delay(10);
       client.subscribe(topic_subscribe2,2);
       delay(10);
       client.subscribe(topic_subscribe3,1);
    }
    
    }
  client.loop();
  
}


