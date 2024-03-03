from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from modules.flower import callFlower
from res.colors import colors

def alert():
    messagebox.showinfo("Alerta","Modulo no terminado")

def startFlower():
    flower_button["state"] = "disable"
    callFlower(flower_button)

# Main screen setup

root = Tk()
root.title("Demo")

window_width = 1000
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

# Main page

#   MAIN SIDE

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

#   IMAGE SIDE

image_frame = Frame(main_frame, bg="#f0f0f0")
image_frame.pack(side=LEFT, fill=BOTH, expand=True)
image_frame.pack_propagate(False)



file_logo = Image.open("./res/images/logo.png")
res = file_logo.resize((200,200))
logo = ImageTk.PhotoImage(res)
logo_imagen = Label(image_frame, image=logo)
logo_imagen.pack(pady=180)

#   DEMO SIDE

menu_frame = Frame(main_frame, bg=colors.GREEN)
menu_frame.pack(side=LEFT, fill=BOTH, expand=True)
menu_frame.pack_propagate(False)

label = Label(menu_frame, text="Seleccione una Demo", font=("Arial", 30, "bold"), bg=colors.GREEN, fg="black")
label.pack(side=TOP, pady=40)

    #   butons grid

buttons = Frame(menu_frame, bg=colors.GREEN, width=405, height=310)
buttons.pack(side=TOP)
buttons.pack_propagate(False)


flower_button = Button(buttons, text="Flor", font=("Helvetica", 20), command=startFlower, bg="#F5DD61", fg="white")
flower_button.pack(side=TOP, fill=X, expand=True)

motion_button = Button(buttons, text="Movimiento", font=("Helvetica", 20), command=alert, bg="#FAA300", fg="white")
motion_button.pack(side=TOP, fill=X, expand=True)

soon_button = Button(buttons, text="Proximamente", font=("Helvetica", 20), command=alert, bg="#F4538A", fg="white")
soon_button.pack(side=TOP, fill=X, expand=True)



root.mainloop()