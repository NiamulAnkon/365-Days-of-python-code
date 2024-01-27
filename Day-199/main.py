import json
import os

class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classes = {}

    def save_data(self):
        data = {
            "students": self.students,
            "teachers": self.teachers,
            "classes": self.classes
        }

        with open("school_data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        if os.path.exists("school_data.json"):
            with open("school_data.json", "r") as file:
                data = json.load(file)
                self.students = data.get("students", [])
                self.teachers = data.get("teachers", [])
                self.classes = data.get("classes", {})

    def add_student(self, name, age, class_name):
        student = {"name": name, "age": age, "class": class_name}
        self.students.append(student)
        if class_name not in self.classes:
            self.classes[class_name] = {"students": []}
        self.classes[class_name]["students"].append(student)
        print(f"Student {name} added successfully!")

    def add_teacher(self, name, subject):
        teacher = {"name": name, "subject": subject}
        self.teachers.append(teacher)
        print(f"Teacher {name} added successfully!")

    def show_students(self, class_name):
        if class_name in self.classes:
            students = self.classes[class_name]["students"]
            print(f"Students in {class_name}:")
            for student in students:
                print(student)
        else:
            print(f"No students found for class {class_name}")

if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.load_data()

    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Show Students in Class")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            class_name = input("Enter class name: ")
            system.add_student(name, age, class_name)

        elif choice == "2":
            name = input("Enter teacher name: ")
            subject = input("Enter taught subject: ")
            system.add_teacher(name, subject)

        elif choice == "3":
            class_name = input("Enter class name: ")
            system.show_students(class_name)

        elif choice == "4":
            system.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")