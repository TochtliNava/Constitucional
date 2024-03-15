from modules.sensors.arduino import com
import re

patron = r'{(\w+):(\d+(?:\.\d+)?)}'

def isRaining():
    matches = re.findall(patron, com.readline().decode('ascii'))
    properties = {match[0]: match[1] for match in matches}
    return "SI" if properties["LLUVIA"] == "1" else "NO"
