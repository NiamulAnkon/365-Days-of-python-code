#quick quiz:Implement a Cat class by using the animal class. Add some methods specific to cat
#Solution:
class Animals:
  def __init__(self, name, species):
    self.name = name
    self.species = species


class Cat(Animals):
  def __init__(self, name, breed):
    Animals.__init__(self, name = "pop", species = "idk")
    self.breed = breed

cat = Cat("pop", "idk")
print(f"The name of the cat is:{cat.name} \nThe breed is:{cat.breed}")