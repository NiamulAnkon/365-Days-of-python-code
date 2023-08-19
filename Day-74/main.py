#ToDo List
class Tasks:
  def __init__(self, description, priority):
    self.description = description
    self.priority = priority

  def display_info(self):
    print(f"The Description is:{self.description} \nThe priority is {self.priority}")

class ToDoList:
  def __init__(self):
    self.tasks = []

  def add_tasks(self, task):
    self.tasks.append(task)

  def list_tasks(self):
    for task in self.tasks:
      print(f"The description is: {task.description}")
      print(f"The priority is: {task.priority}")

if __name__ == "__main__":
  ToDoList = ToDoList()

task1 = Tasks("Coding", "Ankon")
task2 = Tasks("Editing", "Ankon")

ToDoList.add_tasks(task1)
ToDoList.add_tasks(task2)

print("Tasks in Todos are:")
ToDoList.list_tasks()