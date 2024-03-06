import RPi.GPIO as GPIO

SENSOR = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR, GPIO.IN)

def getFire():
	return "Fuego!" if (GPIO.input(SENSOR) == GPIO.LOW) else "No hay fuego"
