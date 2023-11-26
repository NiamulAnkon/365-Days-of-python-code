import tkinter as tk
from tkinter import messagebox
import random
import string

class passwordgeneratorapp:
    def __init__(self, root):
        self.master = root
        self.master.title("Password Generator")
        self.master.geometry("800x500")
        lable_font = ("Arial", 40)
        entry_size = ("Arial", 30)
        result_size = ("Arial", 10)

        # Create GUI elements
        self.length_label = tk.Label(self.master, text="Password Length:", font=lable_font)
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.master, font=entry_size)
        self.length_entry.pack(pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(self.master, text="Include Uppercase", variable=self.uppercase_var)
        self.uppercase_checkbox.pack()

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_checkbox = tk.Checkbutton(self.master, text="Include Lowercase", variable=self.lowercase_var)
        self.lowercase_checkbox.pack()

        self.numbers_var = tk.BooleanVar()
        self.numbers_checkbox = tk.Checkbutton(self.master, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.pack()

        self.symbols_var = tk.BooleanVar()
        self.symbols_checkbox = tk.Checkbutton(self.master, text="Include Symbols", variable=self.symbols_var)
        self.symbols_checkbox.pack()

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=result_size)
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            include_uppercase = self.uppercase_var.get()
            include_lowercase = self.lowercase_var.get()
            include_numbers = self.numbers_var.get()
            include_symbols = self.symbols_var.get()

            characters = ""
            if include_uppercase:
                characters += string.ascii_uppercase
            if include_lowercase:
                characters += string.ascii_lowercase
            if include_numbers:
                characters += string.digits
            if include_symbols:
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("Warning", "Please select at least one character type.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")

if __name__ == "__main__":
    main = tk.Tk()
    software = passwordgeneratorapp(main)
    main.mainloop()
