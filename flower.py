from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def stopFlower(button, root):
    button["state"] = "normal"
    root.destroy()

def callFlower(button):

    # flower root window

    root_flower = Tk()
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

    main_frame = Frame(root_flower, bg="yellow")
    main_frame.pack(fill=BOTH, expand=True)
    main_frame.pack_propagate(False)

    # image frame

    image_frame = Frame(main_frame, bg="red", width=200, height=200)
    image_frame.pack(side=TOP)
    image_frame.pack_propagate(False)



    file_flower = Image.open("./res/images/normal.png")
    res = file_flower.resize((200,200))
    flower = ImageTk.PhotoImage(res)
    flower_image = Label(image_frame, image=flower)
    flower_image.pack(expand=True, fill=BOTH)

    root_flower.mainloop()