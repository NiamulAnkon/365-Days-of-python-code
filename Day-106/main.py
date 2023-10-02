tasks = []

def add_task(task):
  tasks.append(task)
  print(f"Task: {task} added in todo list")

def see_task():
  if len(tasks) == 0:
    print("Sorry your task list is empty :(")

  else:
    print("The To-Do List: ")

  for index, task in enumerate(tasks, start= 1):
    print(f"{index}. \n {tasks}")

def remove_task(task_index):
  if 1 <= task_index <= len(tasks):
    removed_tasks = tasks.pop(task_index -1)
    print(f"Task {remove_task} removed from To-Do list...")

while True:
  print("\nTo-do List Application")
  print("1: Add task")
  print("2: View task")
  print("3: Remove task")
  print("4: Exit")

  usr_choice = input("Enter your action (1,2,3,4): ")

  if usr_choice == '1':
    task = input("Enter your task name you want to add to your To-Do list: ")
    add_task(task)

  elif usr_choice == '2':
    see_task()

  elif usr_choice == '3':
    task_index = int(input("Enter the index of the task you want to remove: "))
    remove_task(task_index)

  elif usr_choice == '4':
    print("GoodBye :)")
    break

  else:
    print("Invalid Choice type 1,2,3,4 pls")