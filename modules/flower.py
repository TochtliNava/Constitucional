from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from modules.plotSoil import plotSoil
from modules.soil import getSoilMoisture
from modules.rain import isRaining
from modules.air import plotAir
from res.colors import colors

def callPlotSoil(button_soil):
        button_soil["state"] = "disable"
        plotSoil(button_soil)

def callPlotAir(button_air):
     button_air["state"] = "disable"
     plotAir(button_air)

def stopFlower(button, root):
    button["state"] = "normal"
    root.destroy()

def callFlower(button):

    def update():
        label_soil.config(text=str(getSoilMoisture()))
        label_rain.config(text=isRaining())
        root_flower.after(1000, update)
         

    # flower root window

    root_flower = Toplevel()
    root_flower.title("Flor")
    root_flower.protocol("WM_DELETE_WINDOW", lambda:stopFlower(button, root_flower))

    window_width = 700
    window_height = 700

    screen_width = root_flower.winfo_screenwidth()
    scren_height = root_flower.winfo_screenheight()

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(scren_height/2 - window_height/2)

    root_flower.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root_flower.resizable(False, False)

    
    # Main frame

    main_frame = Frame(root_flower, bg=colors.GRAY_600)
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
    data.grid_propagate(False)

    button_soil = Button(data, command=lambda: callPlotSoil(button_soil), text="Humedad Suelo", font=("Arial", 20))
    button_soil.grid(row=0, column=0, padx=10, pady=10)

    label_soil = Label(data, text=str(getSoilMoisture()), font=("Arial", 20))
    label_soil.grid(row=0, column=2, padx=10, pady=10)

    label_isRain = Label(data, text="Lluvia", font=("Arial", 20))
    label_isRain.grid(row=1, column=0, padx=10, pady=10)

    label_rain = Label(data, text=isRaining(), font=("Arial", 20))
    label_rain.grid(row=1, column=2, padx=10, pady=10)

    root_flower.after(1000, update)
    root_flower.mainloop()