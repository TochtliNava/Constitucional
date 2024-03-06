from gpiozero import InputDevice

SENSOR = InputDevice(18)

def isRaining():
    return "Si" if not SENSOR.is_active else "No"
