from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import numpy as np
import time

from modules.sensors.temperature import getTemperature
from res.colors import colors

data = np.array([])
cond = False

def stop(button, root):
    button["state"] = "normal"
    root.destroy()

def plotTemperature(button):

    def plot():
        global data

        a = getTemperature()

        if(len(data) < 60):
            data = np.append(data,a)
        else:
            data[0:59] = data[1:60]
            data[59] = a
        
        lines.set_xdata(np.arange(0, len(data)))
        lines.set_ydata(data)

        canvas.draw()
        root.after(1000, plot)

    root = Toplevel()
    root.title('Temperatura')
    root.configure(bg=colors.LIGHT_BLUE)
    root.geometry("625x425")
    root.protocol("WM_DELETE_WINDOW", lambda:stop(button, root))

    #--------------------------------------
    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title("Temperatura")
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Temperatura (C°)')
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 100)
    lines = ax.plot([],[])[0]

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=10, y=10, width=600, height=400)
    canvas.draw()

    root.after(1000, func=plot)
    root.mainloop()
