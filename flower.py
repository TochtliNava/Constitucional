from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

root_flower = Tk()

def stopFlower():
    root_flower.destroy()

def callFlower():
    root_flower.title("Flor")
    root_flower.protocol("WM_DELETE_WINDOW", stopFlower)
    root_flower.mainloop()