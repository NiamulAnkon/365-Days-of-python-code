import time
class Student_Portal:
    def __init__(self):
        self.Students = []
        self.courses = []
        self.logged_Students = None
    def dashboard(self):
        while True:
            usr_chs = int(input("STUDENT PORTAL\n1.Register\n2.Login\n3.Exit\nEnter your choice: "))
            if usr_chs == 1:
                self.register()
            elif usr_chs == 2:
                self.login()
            elif usr_chs == 3:
                print("..........")
                break

    def register(self):
        print("Register \n")
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        new_students = {'name':name, 'username': username, 'email': email, 'password': password, 'courses': []}
        self.Students.append(new_students)
    
    def login(self):
        print("Login \n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for students in self.Students:
            if students["username"] == username and students["password"] == password:
                self.logged_Students = students
                self.start_menu()
                return
            

        print("Invalid Choice try again")

    def start_menu(self):
        while True:
            print("\nWelcome, {}!".format(self.logged_Students["name"]))
            print("1. Enroll in a Course")
            print("2. View Enrolled Courses")
            print("3. Logout")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.enroll_course()
            elif choice == 2:
                self.view_enrolled_courses()
            elif choice == 3:
                print("Logging out.")
                time.sleep(3)
                print("GoodBye")
                self.logged_Students = None
                break
            else:
                print("Invalid choice try again")
                time.sleep(5)
                continue
    def enroll_course(self):
        print("\nAvailable Courses:")
        for i, course in enumerate(self.courses, 1):
            print("{}. {}".format(i, course))

        course_index = int(input("Enter the number of the course to enroll: "))
        if 1 <= course_index <= len(self.courses):
            course = self.courses[course_index - 1]
            if course not in self.logged_Students["courses"]:
                self.logged_Students["courses"].append(course)
                print("Enrollment successful!")
            else:
                print("You are already enrolled in this course.")
        else:
            print("Invalid course number. Please try again.")

    def view_enrolled_courses(self):
        print("\nEnrolled Courses:")
        for i, course in enumerate(self.logged_Students["courses"], 1):
            print("{}. {}".format(i, course))

if __name__ == "__main__":
    student_protal = Student_Portal()
    student_protal.courses = ["Python", "Django", "Web Development", "Softwaer Development"]
    student_protal.dashboard()