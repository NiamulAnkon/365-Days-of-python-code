from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

root = Tk()

root.title("Image Viewer")
root.geometry("400x450")


def show_image():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select image file",
        filetypes=(
            ("JPG File", "*.jpg"),
            ("PNG File", "*.png"),
            ("All Files", "*.*")
        )
    )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    Lbl.configure(image=img)
    Lbl.image = img



frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

Lbl = Label(root)
Lbl.pack()

btn = Button(frame, text="Select Image", command=show_image)
btn.pack(side=tk.LEFT)

btn2 = Button(frame, text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx=12)




root.mainloop()
