from sensors.arduino import com

def getLight():
    val = com.readline()
    cad = val.decode('ascii')
    pos = cad.index(":")
    label = cad[:pos]
    value = cad[pos + 1:]
    if(label == "LUZ"):
        return "Si" if value == 1 else "No"