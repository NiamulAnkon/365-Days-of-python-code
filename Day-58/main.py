#Instance variables vs Class variables in Python
class Employee:
  companyName = "apul"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Ankon")
emp1.raise_amount = 0.3
emp1.companyName = "Apple BD" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Anonto")
emp2.companyName = "Apple"
emp2.showDetails()
