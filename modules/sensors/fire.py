from modules.sensors.arduino import com
import re

patron = r'{(\w+):(\d+(?:\.\d+)?)}'

def getFire():
    matches = re.findall(patron, com.readline().decode('ascii'))
    properties = {match[0]: match[1] for match in matches}
    return "FUEGO" if properties["FLAMA"] == "1" else "No"