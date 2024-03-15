#include <Ticker.h>
#include "DHT.h"

#define LLUVIA 2
#define T11 3
#define DHTTYPE DHT11
#define FLAMA 4
#define LUZ 5

DHT dht(T11, DHTTYPE);

void printData(){
  int lluvia = digitalRead(LLUVIA);
  lluvia = map(lluvia, 1, 0, 0, 1);
  int luz = digitalRead(LUZ);
  luz = map(luz, 1, 0, 0, 1);
  int flama = digitalRead(FLAMA);
  flama = map(flama, 1, 0, 0, 1);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.println("{LLUVIA:"+String(lluvia)+"}{LUZ:"+String(luz)+"}{FLAMA:"+String(flama)+"}{HUMEDAD:"+String(h)+"}{TEMP:"+String(t)+"}");
}

Ticker ticData(printData, 1);

void setup() {
  Serial.begin(9600);
  pinMode(LLUVIA, INPUT);
  pinMode(FLAMA, INPUT);
  pinMode(LUZ, INPUT);
  // put your setup code here, to run once:
  dht.begin();
  ticData.start();
}

void loop() {
  // put your main code here, to run repeatedly:
  ticData.update();
  Serial.read();
}
