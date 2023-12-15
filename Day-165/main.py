import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FitnessTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness Tracker")
        self.master.geometry("800x600")

        self.user_profile = {"name": "", "age": 0, "weight": 0, "goal": 0}

        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack()

        self.label_age = tk.Label(self.master, text="Age:")
        self.label_age.pack()

        self.entry_age = tk.Entry(self.master)
        self.entry_age.pack()

        self.label_weight = tk.Label(self.master, text="Weight (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(self.master)
        self.entry_weight.pack()

        self.label_goal = tk.Label(self.master, text="Fitness Goal (hours per week):")
        self.label_goal.pack()

        self.entry_goal = tk.Entry(self.master)
        self.entry_goal.pack()

        self.button_save_profile = tk.Button(self.master, text="Save Profile", command=self.save_profile)
        self.button_save_profile.pack(pady=10)

        self.label_log_workout = tk.Label(self.master, text="Log Workout:")
        self.label_log_workout.pack()

        self.label_workout_type = tk.Label(self.master, text="Workout Type:")
        self.label_workout_type.pack()

        self.entry_workout_type = tk.Entry(self.master)
        self.entry_workout_type.pack
        self.label_duration = tk.Label(self.master, text="Duration (minutes):")
        self.label_duration.pack()

        self.entry_duration = tk.Entry(self.master)
        self.entry_duration.pack()

        self.button_log_workout = tk.Button(self.master, text="Log Workout", command=self.log_workout)
        self.button_log_workout.pack(pady=10)

        self.button_view_progress = tk.Button(self.master, text="View Progress", command=self.view_progress)
        self.button_view_progress.pack(pady=10)

    def save_profile(self):
        self.user_profile["name"] = self.entry_name.get()
        self.user_profile["age"] = int(self.entry_age.get())
        self.user_profile["weight"] = float(self.entry_weight.get())
        self.user_profile["goal"] = float(self.entry_goal.get())
        messagebox.showinfo("Profile Saved", "Your profile has been saved.")

    def log_workout(self):
        workout_type = self.entry_workout_type.get()
        duration = float(self.entry_duration.get())

        if duration <= 0:
            messagebox.showwarning("Invalid Duration", "Please enter a valid workout duration.")
            return

        print(f"Workout logged: {workout_type}, Duration: {duration} minutes")

        self.entry_workout_type.delete(0, tk.END)
        self.entry_duration.delete(0, tk.END)

    def view_progress(self):
        goal = self.user_profile["goal"]
        logged_hours = 2.5  

        fig, ax = plt.subplots()
        ax.bar(["Goal", "Logged"], [goal, logged_hours], color=['blue', 'green'])
        ax.set_ylabel('Hours')
        ax.set_title('Weekly Workout Progress')
        
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    fitness_tracker = FitnessTracker(root)
    root.mainloop()




