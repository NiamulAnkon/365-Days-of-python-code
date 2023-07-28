#Inheritance in Python
class Employee:
  def __init__(self, name, id,):
    self.name = name
    self.id = id

  def show_details(self):
    print(f"The name of employee: {self.id} is {self.name}")


class Programer(Employee):
  def show_language(self):
    print(f"The name of Programer : {self.id} is {self.name}")

e = Programer("Ankon", 2)
e.show_language()
e1 = Employee("Anonto", 1)
e1.show_details()