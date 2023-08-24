#Single Inheritance in Python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")


d = Dog("Dog", "Bangladeshi")
d.make_sound()

a = Animal("Who cares", "idk")
a.make_sound()