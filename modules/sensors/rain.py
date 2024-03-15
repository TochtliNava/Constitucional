from sensors.arduino import com

def isRaining():
    val = com.readline()
    cad = val.decode('ascii')
    pos = cad.index(":")
    label = cad[:pos]
    value = cad[pos + 1:]
    if(label == "LLUVIA"):
        return "Si" if value == 1 else "No"
