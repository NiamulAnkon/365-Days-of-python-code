import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDo List App")
        self.master.geometry("400x800")

        # Initialize tasks
        self.tasks = []
        self.load_tasks()

        # Create GUI elements
        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=20, width=50)
        self.task_listbox.pack(pady=10)

        self.refresh_task_list()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✓]" if task["completed"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            new_task = {"title": title, "completed": False}
            self.tasks.append(new_task)
            self.refresh_task_list()
            self.save_tasks()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            title = simpledialog.askstring("Edit Task", "Enter new task title:", initialvalue=self.tasks[task_index]["title"])
            if title:
                self.tasks[task_index]["title"] = title
                self.refresh_task_list()
                self.save_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            confirmed = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirmed:
                del self.tasks[task_index]
                self.refresh_task_list()
                self.save_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
