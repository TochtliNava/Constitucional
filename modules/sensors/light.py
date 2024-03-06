import random
import RPi.GPIO as GPIO

SENSOR = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def getLight():
    if(GPIO.input(SENSOR) == 1):
        return "No hay luz"
    else:
        return "Si hay luz"
