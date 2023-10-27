import pyautogui
from tkinter import *


def ss_taker():
    add_Data = entry.get()
    path = add_Data + "\\test.png"
    print(path)
    ss = pyautogui.screenshot()
    ss.save(path)



win = Tk()
win.title("SS Taker")
win.geometry("700x400")
win.config(bg="Gray")
win.resizable(False, False)

entry = Entry(win, font=('Time New Roman', 30))
entry.place(x=20, height=70, width=660, y=50)

button = Button(win, text="Done", font=('Time New Roman', 50), command=ss_taker)
button.place(x=250, y=140, height=100, width=200)



win.mainloop()