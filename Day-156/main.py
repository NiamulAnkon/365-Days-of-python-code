import tkinter as tk
from tkinter import messagebox

def withdraw():
    global balance
    try:
        withdraw_amount = int(withdraw_entry.get())
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            update_balance()
            messagebox.showinfo("Success", f"Withdrawal successful. Your current balance is {balance}")
        else:
            messagebox.showerror("Error", "Insufficient funds. Withdrawal canceled.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def add_money():
    global balance
    try:
        add_amount = int(add_entry.get())
        balance += add_amount
        update_balance()
        messagebox.showinfo("Success", f"Money added successfully. Your current balance is {balance}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def send_money():
    global balance
    try:
        send_amount = int(send_entry.get())
        if send_amount <= balance:
            receiver_name = receiver_entry.get()
            balance -= send_amount
            update_balance()
            messagebox.showinfo("Success", f"Money sent to {receiver_name}. Your current balance is {balance}")
        else:
            messagebox.showerror("Error", "Insufficient funds. Transfer canceled.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def update_balance():
    balance_label.config(text=f"Your current balance is {balance}")

window = tk.Tk()
window.title("Banking App")
window.geometry("700x500")

balance = 50000

balance_label = tk.Label(window, text=f"Your current balance is {balance}", font=("Arial", 20))
balance_label.pack(pady=10)

withdraw_label = tk.Label(window, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = tk.Entry(window)
withdraw_entry.pack()
withdraw_button = tk.Button(window, text="Withdraw", command=withdraw)
withdraw_button.pack(pady=5)

add_label = tk.Label(window, text="Add Amount:")
add_label.pack()
add_entry = tk.Entry(window)
add_entry.pack()
add_button = tk.Button(window, text="Add Money", command=add_money)
add_button.pack(pady=5)

send_label = tk.Label(window, text="Send Amount:")
send_label.pack()
send_entry = tk.Entry(window)
send_entry.pack()

receiver_label = tk.Label(window, text="Receiver Name:")
receiver_label.pack()
receiver_entry = tk.Entry(window)
receiver_entry.pack()

send_button = tk.Button(window, text="Send Money", command=send_money)
send_button.pack(pady=5)

window.mainloop()