from modules.sensors.arduino import com
import re

patron = r'{(\w+):(\d+(?:\.\d+)?)}'

def getAirHumidity():
    matches = re.findall(patron, com.readline().decode('ascii'))
    properties = {match[0]: match[1] for match in matches}
    return float(properties["HUMEDAD"])