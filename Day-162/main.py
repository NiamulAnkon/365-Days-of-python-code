import tkinter as tk
from tkinter import messagebox

def generate_ticket():
    usr_name = entry_name.get()
    usr_number = entry_number.get()
    set_date = entry_date.get()
    wtg = entry_destination.get()

    if not (usr_name and usr_number and set_date and wtg):
        messagebox.showwarning("Incomplete Information", "Please fill in all the fields.")
        return

    ticket_info = f"\n\nYour Ticket is ready \nName: {usr_name} \nNumber: {usr_number} \nThe Date: {set_date} \nThe Destination: {wtg}"
    messagebox.showinfo("Ticket Information", ticket_info)

root = tk.Tk()
root.title("Ticket Buy")
root.geometry("700x500")

label_name = tk.Label(root, text="Enter your name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_number = tk.Label(root, text="Enter your phone number:")
label_number.pack()

entry_number = tk.Entry(root)
entry_number.pack()

label_date = tk.Label(root, text="Enter the date:")
label_date.pack()

entry_date = tk.Entry(root)
entry_date.pack()

label_destination = tk.Label(root, text="Enter where you want to go:")
label_destination.pack()

entry_destination = tk.Entry(root)
entry_destination.pack()

buy_button = tk.Button(root, text="Buy Ticket", command=generate_ticket)
buy_button.pack()

root.mainloop()
