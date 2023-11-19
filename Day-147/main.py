import tkinter as tk
from tkinter import ttk, messagebox
import json
import hashlib
import os
from cryptography.fernet import Fernet
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

DATA_FILE = "secure_budget_data.json"
KEY_FILE = "secure_secret.key"

class SecureBudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Application")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.logged_in = False

        # Check if the key file exists, if not, create a new key
        if not os.path.exists(KEY_FILE):
            key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as key_file:
                key_file.write(key)

        # Create tabs
        self.tabs = ttk.Notebook(root)
        self.expense_tab = ttk.Frame(self.tabs)
        self.budget_tab = ttk.Frame(self.tabs)
        self.visualization_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.expense_tab, text="Log Expense")
        self.tabs.add(self.budget_tab, text="Set Budget")
        self.tabs.add(self.visualization_tab, text="Visualize Budget vs Expenses")
        self.tabs.pack(expand=1, fill="both")

        # Login Tab
        self.login_frame = ttk.Frame(self.root)
        self.login_label = ttk.Label(self.login_frame, text="Login to access the application:")
        self.login_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.username_entry = ttk.Entry(self.login_frame, textvariable=self.username)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.password_entry = ttk.Entry(self.login_frame, textvariable=self.password, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.login_frame.pack()

    def encrypt_data(self, data, key):
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(json.dumps(data).encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data, key):
        cipher_suite = Fernet(key)
        decrypted_data = json.loads(cipher_suite.decrypt(encrypted_data).decode())
        return decrypted_data

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(KEY_FILE, "rb") as key_file:
                key = key_file.read()

            with open(DATA_FILE, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = self.decrypt_data(encrypted_data, key)
            return decrypted_data
        return {"expenses": [], "budgets": {}}

    def save_data(self, data):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()

        encrypted_data = self.encrypt_data(data, key)

        with open(DATA_FILE, "wb") as file:
            file.write(encrypted_data)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        # Dynamically generate the hashed password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # You can replace the following logic with a proper user authentication system.
        if username == "user" and hashed_password == "a42a3a170a76939b81973f04f69a1f9e3ba7b351ec7db442536ca4b3ee5c12d2":
            self.logged_in = True
            self.login_frame.destroy()
            self.create_budget_tabs()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def create_budget_tabs(self):
        # Log Expense Tab
        self.expense_category_label = tk.Label(self.expense_tab, text="Expense Category:")
        self.expense_category_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.expense_category_entry = tk.Entry(self.expense_tab)
        self.expense_category_entry.grid(row=0, column=1, padx=10, pady=10)

        self.expense_amount_label = tk.Label(self.expense_tab, text="Expense Amount:")
        self.expense_amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.expense_amount_entry = tk.Entry(self.expense_tab)
        self.expense_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.expense_notes_label = tk.Label(self.expense_tab, text="Additional Notes:")
        self.expense_notes_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.expense_notes_entry = tk.Entry(self.expense_tab)
        self.expense_notes_entry.grid(row=2, column=1, padx=10, pady=10)

        self.log_expense_button = tk.Button(self.expense_tab, text="Log Expense", command=self.log_expense)
        self.log_expense_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Set Budget Tab
        self.budget_category_label = tk.Label(self.budget_tab, text="Budget Category:")
        self.budget_category_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.budget_category_entry = tk.Entry(self.budget_tab)
        self.budget_category_entry.grid(row=0, column=1, padx=10, pady=10)

        self.budget_amount_label = tk.Label(self.budget_tab, text="Budget Amount:")
        self.budget_amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.budget_amount_entry = tk.Entry(self.budget_tab)
        self.budget_amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.set_budget_button = tk.Button(self.budget_tab, text="Set Budget", command=self.set_budget)
        self.set_budget_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Visualization Tab
        self.visualize_button = tk.Button(self.visualization_tab, text="Visualize Budget vs Expenses", command=self.visualize_budget_vs_expenses)
        self.visualize_button.pack(pady=20)

        # Load data after successful login
        self.data = self.load_data()

    def log_expense(self):
        if not self.logged_in:
            messagebox.showerror("Access Denied", "Please log in to access this feature.")
            return

        category = self.expense_category_entry.get()
        amount = self.expense_amount_entry.get()
        notes = self.expense_notes_entry.get()

        if not category or not amount:
            messagebox.showerror("Error", "Please enter both expense category and amount.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        expense = {"date": str(datetime.now()), "category": category, "amount": amount, "notes": notes}
        self.data["expenses"].append(expense)
        self.save_data(self.data)
        messagebox.showinfo("Success", "Expense logged successfully.")

    def set_budget(self):
        if not self.logged_in:
            messagebox.showerror("Access Denied", "Please log in to access this feature.")
            return

        category = self.budget_category_entry.get()
        budget_amount = self.budget_amount_entry.get()

        if not category or not budget_amount:
            messagebox.showerror("Error", "Please enter both budget category and amount.")
            return

        try:
            budget_amount = float(budget_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        self.data["budgets"][category] = budget_amount
        self.save_data(self.data)
        messagebox.showinfo("Success", f"Budget for {category} set to ${budget_amount}.")

    def visualize_budget_vs_expenses(self):
        if not self.logged_in:
            messagebox.showerror("Access Denied", "Please log in to access this feature.")
            return

        budgets = self.data["budgets"]
        expenses = self.data["expenses"]

        if not budgets or not expenses:
            messagebox.showerror("Error", "Cannot visualize without budgets and expenses.")
            return

        categories = list(budgets.keys())
        budget_amounts = [budgets.get(category, 0) for category in categories]
        expense_amounts = [sum(expense['amount'] for expense in expenses if expense['category'] == category) for category in categories]

        fig, ax = plt.subplots()
        ax.bar(categories, budget_amounts, label='Budget')
        ax.bar(categories, expense_amounts, label='Expenses')
        ax.set_xlabel('Categories')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Budget vs Expenses')
        ax.legend()

        # Embed Matplotlib figure in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureBudgetApp(root)
    root.mainloop()
