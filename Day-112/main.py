from tkinter import Tk, font
from tkinter import Label
import time
import sys

master_screen = Tk()
master_screen.title("digital clock")


def get_time():
  timeVar = time.strftime("%I, %M, %S %p")
  clock.config(text=timeVar)
  clock.after(200,get_time)


clock = Label(master_screen, font=("calibary", 90), bg="Black", fg="Aqua")
clock.pack()

get_time()

master_screen.mainloop()
