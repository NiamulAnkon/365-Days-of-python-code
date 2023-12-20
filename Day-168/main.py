import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta

class HabitTrackerApp:
    def __init__(self, master_root):
        self.master_root = master_root
        self.master_root.title("Habit Tracker")
        self.master_root.geometry("600x400")

        self.db_connection = sqlite3.connect("habit_tracker.db")
        self.create_table()

        self.label_habit = tk.Label(self.master_root, text="Enter Habit:")
        self.label_habit.pack()

        self.entry_habit = tk.Entry(self.master_root)
        self.entry_habit.pack()

        self.button_add_habit = tk.Button(self.master_root, text="Add Habit", command=self.add_habit)
        self.button_add_habit.pack(pady=10)

        self.calendar_frame = tk.Frame(self.master_root)
        self.calendar_frame.pack()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS habits 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           name TEXT, 
                           date DATE, 
                           completed BOOLEAN)''')
        self.db_connection.commit()

    def add_habit(self):
        habit_name = self.entry_habit.get()

        if habit_name:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO habits (name, date, completed) VALUES (?, ?, ?)",
                           (habit_name, datetime.today().strftime('%Y-%m-%d'), 0))
            self.db_connection.commit()

            self.show_calendar()

            self.entry_habit.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Habit", "Please enter a habit.")

    def show_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT DISTINCT date FROM habits ORDER BY date DESC")
        dates = [date[0] for date in cursor.fetchall()]

        for date in dates:
            tk.Label(self.calendar_frame, text=date, width=10, borderwidth=1, relief="solid").pack(side=tk.LEFT)

            cursor.execute("SELECT name, completed FROM habits WHERE date = ?", (date,))
            habits_data = {name: completed for name, completed in cursor.fetchall()}

            for habit_name in habits_data:
                color = "green" if habits_data[habit_name] else "red"
                tk.Label(self.calendar_frame, text=habit_name, width=10, borderwidth=1, relief="solid", bg=color).pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    habit_tracker_app = HabitTrackerApp(root)
    habit_tracker_app.show_calendar()
    root.mainloop()
