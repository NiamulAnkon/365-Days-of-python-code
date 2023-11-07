import tkinter as tk
from PIL import Image, ImageTk
import random


Window = tk.Tk()
Window.geometry("500x360")
Window.title("Dice Roll")

dice = ['Dice1.png', 'Dice2.png', 'Dice3.png', 'Dice4.png', 'Dice5.png', 'Dice6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(Window, image=image1)
label2 = tk.Label(Window, image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40, y = 100)
label2.place(x = 300, y = 100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.config(image= image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.config(image= image2)
    label2.image = image2

button = tk.Button(Window, text="Roll", bg="White", fg="Black", font="Times 20 bold", command=dice_roll)
button.place(x = 200, y = 0)



Window.mainloop()