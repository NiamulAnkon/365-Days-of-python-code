from tkinter import *
root = Tk()

root.geometry("500x300")
root.title("Registration Form")

def getvals():
    print("Accepeted")


Label(root, text="Regester here", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
Email = Label(root, text="Email")
Gender = Label(root, text="Gender")
Phone = Label(root, text="Phone Number")
Payment = Label(root, text="Payment Mood")

name.grid(row=1, column=2)
Email.grid(row=2, column=2)
Gender.grid(row=3, column=2)
Phone.grid(row=4, column=2)
Payment.grid(row=5, column=2)


name_value = StringVar
Email_value = StringVar
Gender_value = StringVar
Phone_value = StringVar
Payment_value = StringVar
check_value = IntVar


name_entry = Entry(root, textvariable=name_value)
Email_entry = Entry(root, textvariable=Email_value)
Gender_entry = Entry(root, textvariable=Gender_value)
Phone_entry = Entry(root, textvariable=Phone_value)
Payment_entry = Entry(root, textvariable=Payment_value)

name_entry.grid(row=1, column=3)
Email_entry.grid(row=2, column=3)
Gender_entry.grid(row=3, column=3)
Phone_entry.grid(row=4, column=3)
Payment_entry.grid(row=5, column=3)

check_button = Checkbutton(root, text="Remember me?", variable=check_value)
check_button.grid(row=6, column=3)



Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
