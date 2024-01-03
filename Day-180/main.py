import tkinter as tk
from tkinter import messagebox

class EntranceExamApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Entrance Exam")
        self.master.geometry("600x900")

        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.roll_label = tk.Label(self.master, text="Roll Number:")
        self.roll_label.pack(pady=5)
        self.roll_entry = tk.Entry(self.master)
        self.roll_entry.pack(pady=5)

        self.class_label = tk.Label(self.master, text="Class:")
        self.class_label.pack(pady=5)
        self.class_entry = tk.Entry(self.master)
        self.class_entry.pack(pady=5)

        self.start_button = tk.Button(self.master, text="Start Exam", command=self.start_exam)
        self.start_button.pack(pady=10)

        self.quiz_frame = tk.Frame(self.master)
        self.quiz_frame.pack()

        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "Who wrote 'Romeo and Juliet'?",
            "Which programming language is used for machine learning?",
            "When was python invented?",
            "Who invented python",
            "can we make software using python yes/no?",
            "who is ceo of youtube",
            "Who is the ceo of microsoft",
            "Who was the ceo of minecraft"
        ]

        self.answers = [
            "Paris",
            "Mars",
            "William Shakespeare",
            "python",
            "1991",
            "Guido van Rossum",
            "yes",
            "Neal Mohan",
            "Satya Narayana",
            "Markus Persson"
        ]

        self.user_answers = [tk.StringVar() for _ in range(len(self.questions))]

    def start_exam(self):
        self.name_entry.config(state=tk.DISABLED)
        self.roll_entry.config(state=tk.DISABLED)
        self.class_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)

        for i, question in enumerate(self.questions):
            question_label = tk.Label(self.quiz_frame, text=f"{i + 1}. {question}")
            question_label.grid(row=i, column=0, padx=10, pady=5)

            answer_entry = tk.Entry(self.quiz_frame, textvariable=self.user_answers[i])
            answer_entry.grid(row=i, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.master, text="Submit Exam", command=self.submit_exam)
        submit_button.pack(pady=10)

    def submit_exam(self):
        correct_answers = 0
        for i in range(len(self.questions)):
            if self.user_answers[i].get().lower() == self.answers[i].lower():
                correct_answers += 1

        total_points = correct_answers * 10

        result_message = f"Total Correct Answers: {correct_answers}\nTotal Points: {total_points}"
        if total_points >= 30:
            result_message += "\nCongratulations! You Passed!"
        else:
            result_message += "\nSorry, You Failed. Better luck next time."

        messagebox.showinfo("Exam Results", result_message)

        student_name = self.name_entry.get()
        roll_number = self.roll_entry.get()
        student_class = self.class_entry.get()

        with open("final_exam_results.txt", "a") as file:
            file.write(f"Name: {student_name}, Roll Number: {roll_number}, Class: {student_class}, "
                       f"Correct Answers: {correct_answers}, Total Points: {total_points}, "
                       f"Pass/Fail: {'Pass' if total_points >= 30 else 'Fail'}\n")

        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EntranceExamApp(root)
    root.mainloop()
