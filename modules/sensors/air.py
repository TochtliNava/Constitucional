import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT11
PIN = 4

def getAirHumidity():
    humedad, temperatura = Adafruit_DHT.read_retry(SENSOR, PIN)
    return humedad
