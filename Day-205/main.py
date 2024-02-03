import json
import datetime

class CompaninonFitnessApp:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            pass

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file, indent=2)

    def register_user(self, username, age, weight, height, fitness_goal):
        if username not in self.users:
            self.users[username] = {
                'age': age,
                'weight': weight,
                'height': height,
                'fitness_goal': fitness_goal,
                'workouts': [],
                'meals': [],
                'water_intake': [],
            }
            self.save_users()
            print(f"User {username} registered successfully!")
        else:
            print(f"User {username} already exists. Please choose a different username.")

    def login(self, username):
        if username in self.users:
            self.current_user = username
            print(f"Logged in as {username}.")
        else:
            print(f"User {username} does not exist. Please register first.")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")

    def record_workout(self, workout_type, duration, calories_burned):
        if self.current_user:
            timestamp = str(datetime.datetime.now())
            workout_data = {'timestamp': timestamp, 'type': workout_type, 'duration': duration, 'calories': calories_burned}
            self.users[self.current_user]['workouts'].append(workout_data)
            self.save_users()
            print("Workout recorded successfully.")
        else:
            print("Please log in to record a workout.")

    # Add similar methods for recording meals, water intake, etc.

    def show_user_stats(self):
        if self.current_user:
            user_data = self.users[self.current_user]
            print(f"User: {self.current_user}")
            print(f"Age: {user_data['age']}, Weight: {user_data['weight']}, Height: {user_data['height']}")
            print(f"Fitness Goal: {user_data['fitness_goal']}")
            print("\nWorkouts:")
            for workout in user_data['workouts']:
                print(f"{workout['timestamp']} - {workout['type']}: {workout['duration']} minutes, {workout['calories']} calories")
            # Add similar sections for meals, water intake, etc.
        else:
            print("Please log in to view user stats.")

# Usage Example:
app_companinon = CompaninonFitnessApp()
app_companinon.load_users()

# User Registration (Run this only once)
# app.register_user('john_doe', 25, 70, 175, 'Weight Loss')

# User Login
app_companinon.login('john_doe')

# Record Workout
app_companinon.record_workout('Running', 30, 300)

# Show User Stats
app_companinon.show_user_stats()

# Logout
app_companinon.logout()
