import json
from datetime import datetime, timedelta


class personal_task_manager():
    def __init__(self):
        self.tasks = {}

    def load_tasks(self):
        try:
            with open("tasks.json", 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = {}

    def save_tasks(self):
        with open("tasks.json", 'w') as file:
            json.dump(self.tasks, file)

    def display_tasks(self):
        print("=======Your Tasks =========")
        if not self.tasks:
            print("No tasks available")
        else:
            for task_id, task in self.tasks.items():
                print(f"{task_id}. {task['title']} (due: {task['due_date']}, priority: {task['priority']})")

    def add_task(self, title, due_date, priority):
        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = {
            "title": title,
            "due_date": due_date,
            "priority": priority
        }
        print(f"Task '{title}' added successfully!")

    def update_task(self, task_id, title=None, due_date=None, priority=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task["title"] = title or task["title"]
            task["due_date"] = due_date or task["due_date"]
            task["priority"] = priority or task["priority"]
            print(f"Task {task_id} updated successfully!")
        else:
            print("Task not found.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted successfully!")
        else:
            print("Task not found.")

    def run(self):
        self.load_tasks()

        while True:
            print("\n===== Personal Task Manager =====")
            print("1. Display Tasks")
            print("2. Add Task")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                title = input("Enter task title: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                priority = input("Enter priority: ")
                self.add_task(title, due_date, priority)
            elif choice == "3":
                task_id = input("Enter task ID to update: ")
                title = input("Enter new task title (press Enter to keep the same): ")
                due_date = input("Enter new due date (YYYY-MM-DD) (press Enter to keep the same): ")
                priority = input("Enter new priority (press Enter to keep the same): ")
                self.update_task(task_id, title, due_date, priority)
            elif choice == "4":
                task_id = input("Enter task ID to delete: ")
                self.delete_task(task_id)
            elif choice == "5":
                self.save_tasks()
                print("Exiting. Your tasks have been saved.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    task_manager = personal_task_manager()
    task_manager.run()
