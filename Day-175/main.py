import tkinter as tk
from tkinter import messagebox
import random

class Flashcard_Quiz_Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard Quiz App")
        self.master.geometry("500x300")

        self.flashcards = [
            {"question": "What is python?", "answer": "programing language"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What has the largest datacenter?", "answer": "mongolia information park"},
        ]

        self.current_flashcard = None
        self.score = 0

        self.label_question = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.label_question.pack(pady=20)

        self.entry_answer = tk.Entry(self.master)
        self.entry_answer.pack(pady=10)

        self.button_next = tk.Button(self.master, text="Next Flashcard", command=self.next_flashcard)
        self.button_next.pack(pady=10)

        self.button_check = tk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.button_check.pack(pady=10)

    def next_flashcard(self):
        self.current_flashcard = random.choice(self.flashcards)
        self.label_question.config(text=self.current_flashcard["question"])
        self.entry_answer.delete(0, tk.END)

    def check_answer(self):
        if not self.current_flashcard:
            messagebox.showwarning("No Flashcard", "Please select a flashcard first.")
            return

        user_answer = self.entry_answer.get().strip().lower()
        correct_answer = self.current_flashcard["answer"].lower()

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", f"Correct! Your score: {self.score}")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect. The correct answer is: {correct_answer}")

        # Move to the next flashcard
        self.next_flashcard()

if __name__ == "__main__":
    root = tk.Tk()
    flashcard_app = Flashcard_Quiz_Application(root)
    root.mainloop()
