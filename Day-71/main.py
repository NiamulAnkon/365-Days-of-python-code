#School and Student Management
class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def info(self):
    print(f"The name of the student is: {self.name} \nThe age of the student is: {self.age} \nThe Grade of the student is: {self.grade}")


class School:
  def __init__(self, name):
    self.name = name
    self.students = []

  def enroll_student(self, student):
    self.students.append(student)

  def list_students(self):
    for student in self.students:
      print(student.name)


if __name__ == "__main__":
  school = School("ADARSHA HIGH SCHOOL")

  Student1 = Student("Ankon", 14, 6)
  Student2 = Student("Anonto", 24, 16)

  school.enroll_student(Student1)
  school.enroll_student(Student2)

  print("Enrolled Students:")
  school.list_students()