from sensors.arduino import com

def getTemperature():
    val = com.readline()
    cad = val.decode('ascii')
    pos = cad.index(":")
    label = cad[:pos]
    value = cad[pos + 1:]
    if(label == "TEMP"):
        return float(value)
  