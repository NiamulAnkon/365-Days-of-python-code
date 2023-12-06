import calendar
from tkinter import *

root = Tk()
root.title("Calendar")
root.geometry("700x600")

current_year = 2023
cal = calendar.calendar(current_year)

l_1 = Label(root, text=cal)
l_1.pack()

def next_year():
    global current_year
    current_year += 1
    cal_next_year = calendar.calendar(current_year)
    l_1.config(text=cal_next_year)

btn_1 = Button(root, text="Next Year", command=next_year)
btn_1.pack(padx=10)

root.mainloop()