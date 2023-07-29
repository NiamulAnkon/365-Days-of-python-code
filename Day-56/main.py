#Exercise Library Management System in Python
class Exercise:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ExerciseLibrary:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise_name):
        for exercise in self.exercises:
            if exercise.name == exercise_name:
                self.exercises.remove(exercise)
                return True
        return False

    def view_exercises(self):
        if not self.exercises:
            print("Exercise library is empty.")
        else:
            print("Exercise Library:")
            for exercise in self.exercises:
                print(f"Name: {exercise.name}\nDescription: {exercise.description}\n")

def main():
    exercise_library = ExerciseLibrary()

    while True:
        print("\nExercise Library Management System")
        print("1. Add Exercise")
        print("2. Remove Exercise")
        print("3. View Exercises")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter the exercise name: ")
            description = input("Enter the exercise description: ")
            exercise = Exercise(name, description)
            exercise_library.add_exercise(exercise)
            print("Exercise added successfully.")

        elif choice == "2":
            exercise_name = input("Enter the exercise name to remove: ")
            if exercise_library.remove_exercise(exercise_name):
                print("Exercise removed successfully.")
            else:
                print("Exercise not found in the library.")

        elif choice == "3":
            exercise_library.view_exercises()

        elif choice == "4":
            print("Exiting Exercise Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
