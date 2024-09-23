#include <ThingSpeak.h>
#include <WiFi.h>
#include <DHT.h>
WiFiClient mosal;
DHT dht(32,DHT22);

void setup(){
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(27,OUTPUT);
  pinMode(25,INPUT);
  dht.begin();
  Serial.begin(115200);
  WiFi.begin("wifi","tumiayako");
  while(WiFi.status()!=WL_CONNECTED){
  delay(500);
  Serial.println("Please weit for wifi connection...");
  }
  ThingSpeak.begin(mosal);
  Serial.println("Wifi connected");
}
void loop(){

 
int n = 0;
while(true) {
n += 1;
  digitalWrite(27,LOW);
  delayMicroseconds(2);
  digitalWrite(27,HIGH);
  delayMicroseconds(10);
  digitalWrite(27,LOW);
 long duration=pulseIn(25,HIGH);
 float distance=duration*0.034/2;

   float t = dht.readTemperature();
   float h = dht.readHumidity();

//Read data
int y = ThingSpeak.readIntField(2653317,1,"YHEJKMD4TPE7L5DL");
if(y==10){
  digitalWrite(13,HIGH);
  digitalWrite(12,HIGH);
  Serial.println("All led on");
}

if(y==20){
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  Serial.println("All led off");
}

if(n==16) {
//sand data
ThingSpeak.setField(2,t);
ThingSpeak.setField(3,h);
ThingSpeak.setField(4,distance);
ThingSpeak.writeFields(2634942,"8LG6F6T1JQ3MUCBK");
Serial.println("temperature:"+String(t));
Serial.println("humidity:"+String(h));
Serial.println("distance:"+String(distance));
delay(1000);
n=0;
}
delay(1000);
Serial.println("Seconds:"+String(n));
}

}