import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, master_root):
        self.master_root = master_root
        self.master_root.title("Quiz Game")
        self.master_root.geometry("500x300")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "London", "Rome"], "correct_answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct_answer": "4"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct_answer": "Mars"},
            {"question": "What is the full from of oop", "options": ["object oriented progrsming", "o o p", "oi oi pro", "ouh ouh piss"], "correct_answer": "4"}
            
        ]

        self.score = 0
        self.current_question_index = 0

        self.label_question = tk.Label(self.master_root, text="", font=("Helvetica", 12))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.master_root, text="", variable=self.radio_var, value="", command=self.check_answer)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = tk.Button(self.master_root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            question_text = question_data["question"]
            options = question_data["options"]

            random.shuffle(options)

            self.label_question.config(text=question_text)
            for i in range(4):
                self.radio_buttons[i].config(text=options[i], value=options[i])

            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Game Over", f"Quiz completed!\nYour score: {self.score}")

    def check_answer(self):
        selected_option = self.radio_var.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        self.radio_var.set("")
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizGame(root)
    root.mainloop()
