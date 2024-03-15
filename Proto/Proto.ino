#include <Ticker.h>
#include "DHT.h"

#define LLUVIA 2
#define T11 3
#define DHTTYPE DHT11
#define FLAMA 4
#define LUZ 5

DHT dht(T11, DHTTYPE);

void printLluvia() {
  int valor = digitalRead(LLUVIA);
  valor = map(valor, 1, 0, 0, 1);
  Serial.println("LLUVIA:"+String(valor));
}

void printLuz() {
  int valor = digitalRead(LUZ);
  valor = map(valor, 1, 0, 0, 1);
  Serial.println("LUZ:"+String(valor));
}

void printFlama() {
  int valor = digitalRead(FLAMA);
  valor = map(valor, 1, 0, 0, 1);
  Serial.println("FLAMA:"+String(valor));
}

void printHumedad(){
  float h = dht.readHumidity();
  // Leemos la temperatura en grados centígrados (por defecto)
  Serial.println("HUM:"+String(h));
}

void printTemp(){
  float t = dht.readTemperature();
  Serial.println("TEMP:"+String(t));
}

Ticker ticLLuvia(printLluvia, 200);
Ticker ticTemp(printTemp, 300);
Ticker ticHum(printHumedad, 400);
Ticker ticFire(printFlama, 500);
Ticker ticLuz(printLuz, 600);

void setup() {
  Serial.begin(9600);
  pinMode(LLUVIA, INPUT);
  pinMode(FLAMA, INPUT);
  pinMode(LUZ, INPUT);
  // put your setup code here, to run once:
  dht.begin();
  ticLLuvia.start();
  ticHum.start();
  ticTemp.start();
  ticFire.start();
  ticLuz.start();
}

void loop() {
  // put your main code here, to run repeatedly:
  ticLLuvia.update();
  ticHum.update();
  ticTemp.update();
  ticFire.update();
  ticLuz.update();
}
