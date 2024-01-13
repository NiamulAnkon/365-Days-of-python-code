import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x400")

        self.secret_number = random.randint(1, 100)
        self.guesses_left = 10

        self.instruction_label = tk.Label(self.master, text="Guess the number between 1 and 100:")
        self.instruction_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def submit_guess(self):
        try:
            user_guess = int(self.guess_entry.get())

            if user_guess == self.secret_number:
                self.result_label.config(text="Congratulations! You guessed the correct number.")
                self.guess_button.config(state=tk.DISABLED)
            elif user_guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")

            self.guesses_left -= 1

            if self.guesses_left == 0:
                self.result_label.config(text=f"Sorry, you ran out of guesses. The correct number was {self.secret_number}.")
                self.guess_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()