from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x700")
root.title("Age Calculator")

def calculate_age():
    today = date.today()
    birthday = date(int(yearValue.get()), int(monthValue.get()), int(dayValue.get()))
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    Label(text=f"{nameValue.get()} your age is {age}", font=30).place(x=300, y=500)

photo = PhotoImage(file="Age calculator  .png")
myimage = Label(image=photo)
myimage.pack(padx=15, pady=15)

Label(text="Name", font=23).place(x=200, y=250)
Label(text="Year", font=23).place(x=200, y=300)
Label(text="Month", font=23).place(x=200, y=350)
Label(text="Day", font=23).place(x=200, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

name_entery = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
name_entery.place(x=300, y=250)
Year_entery = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
Year_entery.place(x=300, y=300)
month_entery = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
month_entery.place(x=300, y=350)
day_entery = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
day_entery.place(x=300, y=400)

Button(text="Check Age", font=20, bg="Black", fg="White", width=11, height=2, command=calculate_age).place(x=300, y=450)



root.mainloop()