from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import RPi.GPIO as GPIO

from res.colors import colors

RED = 13
GREEN = 19
BLUE = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

R = GPIO.PWM(RED, 100)
G = GPIO.PWM(GREEN, 100)
B = GPIO.PWM(BLUE, 100)

R.start(100)
G.start(100)
B.start(100)

color = 100

def stopLed(button, root):
	R.ChangeDutyCycle(100)
	G.ChangeDutyCycle(100)
	B.ChangeDutyCycle(100)
	button["state"] = "normal"
	root.destroy()

def callLed(button):
	
	def update(color):
		if(color > 1):
			color = color - 1
			R.ChangeDutyCycle(color + 1)
			G.ChangeDutyCycle(color)
			B.ChangeDutyCycle(color - 1) 
		root.after(1, lambda:update(color))
		        
         

    # flower root window

	root = Toplevel()
	root.title("LED")
	root.protocol("WM_DELETE_WINDOW", lambda:stopLed(button, root))

	window_width = 700
	window_height = 700

	screen_width = root.winfo_screenwidth()
	scren_height = root.winfo_screenheight()

	center_x = int(screen_width/2 - window_width/2)
	center_y = int(scren_height/2 - window_height/2)

	root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
	root.resizable(False, False)

	
    
    # Main frame

	main_frame = Frame(root, bg=colors.GRAY_200)
	main_frame.pack(fill=BOTH, expand=True)
	main_frame.pack_propagate(False)
    
	root.after(1, lambda:update(color))
	root.mainloop()
