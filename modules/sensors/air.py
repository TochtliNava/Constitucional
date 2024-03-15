from sensors.arduino import com

def getAirHumidity():
    val = com.readline()
    cad = val.decode('ascii')
    pos = cad.index(":")
    label = cad[:pos]
    value = cad[pos + 1:]
    if(label == "HUM"):
        return float(value)