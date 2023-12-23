import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class TaskSchedulerApp:
    def __init__(self, master_root):
        self.master_root = master_root
        self.master_root.title("Task Scheduler")
        self.master_root.geometry("500x600")

        self.db_connection = sqlite3.connect("tasks_database.db")
        self.create_table()

        self.label_title = tk.Label(self.master_root, text="Task Title:")
        self.label_title.pack()

        self.entry_title = tk.Entry(self.master_root)
        self.entry_title.pack()

        self.label_description = tk.Label(self.master_root, text="Task Description:")
        self.label_description.pack()

        self.entry_description = tk.Entry(self.master_root)
        self.entry_description.pack()

        self.label_due_date = tk.Label(self.master_root, text="Due Date (YYYY-MM-DD):")
        self.label_due_date.pack()

        self.entry_due_date = tk.Entry(self.master_root)
        self.entry_due_date.pack()

        self.button_add_task = tk.Button(self.master_root, text="Add Task", command=self.add_task)
        self.button_add_task.pack(pady=10)

        self.task_listbox = tk.Listbox(self.master_root)
        self.task_listbox.pack(expand=True, fill="both")

        self.load_tasks()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           title TEXT, 
                           description TEXT, 
                           due_date DATE, 
                           completed BOOLEAN)''')
        self.db_connection.commit()

    def add_task(self):
        title = self.entry_title.get()
        description = self.entry_description.get()
        due_date_str = self.entry_due_date.get()

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Invalid Date Format", "Please enter a valid date in the format YYYY-MM-DD.")
            return

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)",
                       (title, description, due_date, False))
        self.db_connection.commit()

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, title, description, due_date, completed FROM tasks")

        for row in cursor.fetchall():
            task_str = f"{row[1]} - {row[2]} - Due: {row[3]} - {'Completed' if row[4] else 'Not Completed'}"
            self.task_listbox.insert(tk.END, task_str)

if __name__ == "__main__":
    root = tk.Tk()
    task_scheduler_app = TaskSchedulerApp(root)
    root.mainloop()
