#Constructors in Python
class person:
  def __init__(self, name, occ):
    print("Hey i am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}.")

a = person("Ankon", "Devloper")
b = person("Anonto", "Multitalented")

a.info()
b.info()