from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from soil import getSoilMoisture
import numpy as np
import time

data = np.array([])
cond = False

def stop(button, root):
    button["state"] = "normal"
    root.destroy()

def plotSoil(button):

    def plot():
        global data

        a = getSoilMoisture()

        if(len(data) < 100):
            data = np.append(data,float(a[0:4]))
        else:
            data[0:99] = data[1:100]
            data[99] = float(a[0:4])
        
        lines.set_xdata(np.arange(0, len(data)))
        lines.set_ydata(data)

        canvas.draw()

    root = Toplevel()
    root.title('Humedad del suelo')
    root.configure(bg="light blue")
    root.geometry("900x500")
    root.protocol("WM_DELETE_WINDOW", lambda:stop(button, root))

    #--------------------------------------
    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title("Lectura sensor HM11")
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Humedad')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    lines = ax.plot([],[])[0]

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=10, y=10, width=600, height=400)
    canvas.draw()

    root.after(1, plot)
    root.mainloop()