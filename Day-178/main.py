import tkinter as tk
from tkinter import *
import random
import time
import pygame
import threading

class New_Year_eve_Celebration_App:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual New Year's Eve Celebration App")
        self.master.geometry("800x800")

        self.countdown_label = tk.Label(self.master, text="", font=("Helvetica", 24))
        self.countdown_label.grid(row=0, column=0, pady=20)

        self.frame = tk.Frame(self.master)
        self.frame.grid(row=1, column=0)
    
        self.canvas = tk.Canvas(self.frame, bg="black", width=800, height=500)
        self.canvas.grid(row=0, column=0)

        self.start_button = tk.Button(self.frame, text="Start Celebration", command=self.start_celebration)
        self.start_button.grid(row=2, column=0, pady=10)

        pygame.mixer.init()

    def start_celebration(self):
        self.start_button.config(state=tk.DISABLED)
        self.countdown(10)

    def countdown(self, seconds):
        if seconds == 0:
            self.countdown_label.config(text="Happy New Year!")
            threading.Thread(target=self.play_fireworks_sound).start()
            threading.Thread(target=self.fireworks_animation).start()
            return

        self.countdown_label.config(text=f"Countdown: {seconds}")
        self.master.after(1000, self.countdown, seconds - 1)

    def play_fireworks_sound(self):
        pygame.mixer.music.load("new-year-fireworks-sound3-180204.mp3")
        pygame.mixer.music.play()

    def fireworks_animation(self):
        for _ in range(30):
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            size = random.randint(5, 20)
            color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "white"])

            self.canvas.create_oval(x, y, x + size, y + size, fill=color)
            time.sleep(0.2)

        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    new_year_app = New_Year_eve_Celebration_App(root)
    root.mainloop()
