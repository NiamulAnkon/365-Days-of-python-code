#super keyword in Python
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
      print("Ankon is a coder")
      super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang

Siyam = Employee("Siyam", 122)
Ankon = Programer("Ankon", 12, "Python")
print(Siyam.name)
print(Ankon.name)
print(Ankon.id)
print(Ankon.lang)