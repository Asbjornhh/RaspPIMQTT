#include <dht11.h>
#define DHT11PIN 4
#define LED_PIN 8

dht11 DHT11;



void  setup()
{
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  Serial.println();

  int chk = DHT11.read(DHT11PIN);

if((float)DHT11.humidity > 40){
  digitalWrite(LED_PIN, HIGH);
}else{
  digitalWrite(LED_PIN, LOW);
}
  Serial.print("Humidity (%): ");
  Serial.println((float)DHT11.humidity, 2);

  Serial.print("Temperature  (C): ");
  Serial.println((float)DHT11.temperature, 2);

  delay(2000);

}