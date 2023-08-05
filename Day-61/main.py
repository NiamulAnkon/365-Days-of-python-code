#Class Methods as Alternative Constructors in Python
class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @classmethod
  def frmostr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))


e1 = Employee("Ankon", 2000000)
print(e1.name)
print(e1.salary)
string = "Ankon-12000"
e2 = Employee.frmostr(string)
print(e2.name)
print(e2.salary)