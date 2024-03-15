from sensors.arduino import com

def getFire():
    val = com.readline()
    cad = val.decode('ascii')
    pos = cad.index(":")
    label = cad[:pos]
    value = cad[pos + 1:]
    if(label == "FLAMA"):
        return "Fuego!" if value == 1 else "Seguro"
