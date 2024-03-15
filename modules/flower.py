from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from modules.plot.plotSoil import plotSoil
from modules.sensors.soil import getSoilMoisture
from modules.sensors.rain import isRaining
from modules.plot.plotAir import plotAir
from modules.sensors.air import getAirHumidity
from modules.sensors.light import getLight
from modules.plot.plotTemperature import plotTemperature
from modules.sensors.temperature import getTemperature
from modules.sensors.fire import getFire
from res.colors import colors

def callPlotSoil(button_soil):
    button_soil["state"] = "disable"
    plotSoil(button_soil)

def callPlotAir(button_air):
    button_air["state"] = "disable"
    plotAir(button_air)

def callPlotTemperature(button_temp):
    button_temp["state"] = "disable"
    plotTemperature(button_temp)

def stopFlower(button, root):
    button["state"] = "normal"
    root.destroy()

def callFlower(button):

    def update():
        label_soil.config(text=str(getSoilMoisture()))
        label_rain.config(text=isRaining())
        label_air.config(text=str(getAirHumidity()))
        label_light_val.config(text=str(getLight()))
        label_fire_val.config(text=getFire())
        root.after(10, update)
         

    # flower root window

    root = Toplevel()
    root.title("Flor")
    root.protocol("WM_DELETE_WINDOW", lambda:stopFlower(button, root))

    window_width = 700
    window_height = 700

    screen_width = root.winfo_screenwidth()
    scren_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(scren_height/2 - window_height/2)

    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(False, False)

    
    # Main frame

    main_frame = Frame(root, bg=colors.GRAY_600)
    main_frame.pack(fill=BOTH, expand=True)
    main_frame.pack_propagate(False)

    # image frame

    image_frame = Frame(main_frame, bg=colors.GRAY_600, width=200, height=200)
    image_frame.pack(side=TOP)
    image_frame.pack_propagate(False)

    file_flower = Image.open("./res/images/normal.png")
    res = file_flower.resize(size=(200,200))
    src = ImageTk.PhotoImage(res)
    flower_image = Label(image_frame, image=src)
    flower_image.grid(row=0, column=1, padx=10, pady=40)

    # data grid

    data = Frame(main_frame, width=600, height=300, bg=colors.GRAY_200)
    data.pack(side=TOP, ipadx=20, expand=True)
    #data.grid_propagate(False)

    button_soil = Button(data, command=lambda: callPlotSoil(button_soil), text="Humedad Suelo", font=("Arial", 20))
    button_soil.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    label_soil = Label(data, text=str(getSoilMoisture()), font=("Arial", 20))
    label_soil.grid(row=0, column=2, padx=10, pady=10)

    button_air = Button(data, command=lambda: callPlotAir(button_air), text="Humedad Aire", font=("Arial", 20))
    button_air.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    label_air = Label(data, text=str(getAirHumidity()), font=("Arial", 20))
    label_air.grid(row=1, column=2, padx=10, pady=10)
    
    button_temp = Button(data, command=lambda: callPlotTemperature(button_temp), text="Temperatura Aire", font=("Arial", 20))
    button_temp.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    label_temp = Label(data, text=str(getTemperature()), font=("Arial", 20))
    label_temp.grid(row=2, column=2, padx=10, pady=10)

    label_isRain = Label(data, text="Lluvia", font=("Arial", 20))
    label_isRain.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    label_rain = Label(data, text=isRaining(), font=("Arial", 20))
    label_rain.grid(row=3, column=2, padx=10, pady=10)
    
    label_light = Label(data, text="Luz", font=("Arial", 20))
    label_light.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    label_light_val = Label(data, text=str(getLight()), font=("Arial", 20))
    label_light_val.grid(row=4, column=2, padx=10, pady=10)
    
    label_fire = Label(data, text="Fuego", font=("Arial", 20))
    label_fire.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    label_fire_val = Label(data, text=getFire(), font=("Arial", 20))
    label_fire_val.grid(row=5, column=2, padx=10, pady=10)
    

    root.after(10, update)
    root.mainloop()
