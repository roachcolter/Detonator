#include <ESP8266WiFi.h>

const char* ssid="WifiBomb";
const char* password="burgerkeju";
const int led= D1;
const int buz= D2;
WiFiServer server(80);
String header;
void setup() {
  // put your setup code here, to run once:
  digitalWrite(led, HIGH);
  pinMode(led,OUTPUT);
  Serial.begin(115200);                                                                                                                                                                                                                                                                                                                                                                                               
  Serial.print("Setting AP (Access Point)…");
  // Remove the password parameter, if you want the AP (Access Point) to be open
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);
  
  server.begin();
}

void loop() {
  WiFiClient client;
  client=server.available();

  if (client ==1){
    String request=client.readStringUntil('\n');
    client.flush();
    Serial.println(request);
    
    if (request.indexOf("buz1") != -1){
      digitalWrite(buz,HIGH);
      delay(5);
      digitalWrite(buz, LOW);
      client.println("HTTP/1.1 200 OK");
    }

    if (request.indexOf("buz2") != -1){
      digitalWrite(buz,HIGH);
      delay(0.25);
      digitalWrite(buz, LOW);
      client.println("HTTP/1.1 200 OK");
    }

    if (request.indexOf("buz3") != -1){
      digitalWrite(buz,HIGH);
      delay(0.125);
      digitalWrite(buz, LOW);
      client.println("HTTP/1.1 200 OK");
    }

    if (request.indexOf("buz4") != -1){
      digitalWrite(buz,HIGH);
      delay(3);
      digitalWrite(buz, LOW);
      client.println("HTTP/1.1 200 OK");
    }

    if (request.indexOf("ledon") != -1){
      digitalWrite(led,HIGH);
      client.println("HTTP/1.1 200 OK");
      Serial.println("CURRENT IS OFF");
    }

    if (request.indexOf("ledoff") != -1){
      digitalWrite(led,LOW);
      client.println("HTTP/1.1 200 OK");
      Serial.println("DETONATING");
    }
    Serial.println("                              ");
  }
}
