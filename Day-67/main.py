#Operator Overloading in Python
class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"


  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 

e1 = Vector(2,6,4)
print(e1)

e2 = Vector(1,3,2)
print(e2)

print(e1 + e2)
print(type(e1 + e2))