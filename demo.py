from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def saludo(name):
    messagebox.showinfo("Saludos", f"Hola {name}")


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



file_logo = Image.open("logo.png")
res = file_logo.resize([200,200])
logo = ImageTk.PhotoImage(res)
logo_imagen = Label(image_frame, image=logo)
logo_imagen.pack(pady=180)

#   DEMO SIDE

menu_frame = Frame(main_frame, bg="olivedrab1")
menu_frame.pack(side=LEFT, fill=BOTH, expand=True)
menu_frame.pack_propagate(False)

label = Label(menu_frame, text="Seleccione un Demo", font=("Arial", 30), bg="olivedrab1", fg="black")
label.pack(side=TOP, pady=40)

#   butons grid

buttons = Frame(menu_frame, bg="olivedrab1")
buttons.pack(side=TOP)


button = Button(buttons, text="1", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=0, column=0, padx=15, pady=15)
button = Button(buttons, text="2", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=0, column=1)
button = Button(buttons, text="3", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=0, column=2, padx=15)
button = Button(buttons, text="4", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=1, column=0)
button = Button(buttons, text="5", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=1, column=1)
button = Button(buttons, text="6", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=1, column=2)
button = Button(buttons, text="7", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=2, column=0, pady=15)
button = Button(buttons, text="8", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=2, column=1)
button = Button(buttons, text="9", command=lambda: saludo("nora"), width=15, height=7)
button.grid(row=2, column=2)


root.mainloop()