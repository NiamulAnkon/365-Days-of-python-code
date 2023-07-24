#Classes and Objects in Python 
class Person:
  name = "Ankon"
  ocupation = "Web Devloper"
  networth = 57,390
  def info(self):
    print(f"{self.name} is a {self.ocupation}")

a = Person()
b = Person()
c = Person()

a.info()
b.info()
a.name = "Anonto"
a.ocupation = "0.00"

b.name = "Create"
b.ocupation = "AccountBalance is 0"

c.name = "Mikey"
c.ocupation = 100

a.info()
b.info()
c.info()