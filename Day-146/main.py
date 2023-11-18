import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budgeting Application")

        self.data = {"expenses": [], "budgets": {}}

        # Create tabs
        self.tabs = ttk.Notebook(root)
        self.expense_tab = ttk.Frame(self.tabs)
        self.budget_tab = ttk.Frame(self.tabs)
        self.visualization_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.expense_tab, text="Log Expense")
        self.tabs.add(self.budget_tab, text="Set Budget")
        self.tabs.add(self.visualization_tab, text="Visualize Budget vs Expenses")
        self.tabs.pack(expand=1, fill="both")

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

    def log_expense(self):
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
        messagebox.showinfo("Success", "Expense logged successfully.")

    def set_budget(self):
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
        messagebox.showinfo("Success", f"Budget for {category} set to ${budget_amount}.")

    def visualize_budget_vs_expenses(self):
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
    app = BudgetApp(root)
    root.mainloop()
