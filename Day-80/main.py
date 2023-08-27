#Multiple Inheritance in Python
class Employee:
  def __init__(self, name):
    self.name = name

  def show(self):
    print(f"The name is: {self.name}")

class dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is: {self.dance}")

class dancerEmployee(Employee, dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

ed = dancerEmployee("Slowmotion", "IDK")
print(ed.name)
print(ed.dance)
ed.show()
print(dancerEmployee.mro())