import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, software):
        self.software = software
        self.software.title("Language Learning Flashcards")
        self.software.geometry("700x400")

        # Create GUI elements
        self.word_label = tk.Label(self.software, text="Word/Phrase:")
        self.word_label.pack(pady=10)

        self.word_entry = tk.Entry(self.software)
        self.word_entry.pack()

        self.translation_label = tk.Label(self.software, text="Translation:")
        self.translation_label.pack(pady=10)

        self.translation_entry = tk.Entry(self.software)
        self.translation_entry.pack()

        self.add_flashcard_button = tk.Button(self.software, text="Add Flashcard", command=self.add_flashcard)
        self.add_flashcard_button.pack(pady=10)

        self.view_flashcard_button = tk.Button(self.software, text="View Flashcards", command=self.view_flashcards)
        self.view_flashcard_button.pack(pady=10)

        self.quiz_button = tk.Button(self.software, text="Take Quiz", command=self.start_quiz)
        self.quiz_button.pack(pady=10)

        # Flashcards data
        self.flashcards = []

    def add_flashcard(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()

        if word and translation:
            flashcard = {"word": word, "translation": translation}
            self.flashcards.append(flashcard)
            messagebox.showinfo("Flashcard Added", f"Flashcard added:\nWord: {word}\nTranslation: {translation}")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please enter both word and translation.")

    def view_flashcards(self):
        if self.flashcards:
            flashcard_window = tk.Toplevel(self.software)
            flashcard_window.title("Flashcards")

            for idx, flashcard in enumerate(self.flashcards, start=1):
                flashcard_text = f"{idx}. Word: {flashcard['word']}\n   Translation: {flashcard['translation']}"
                flashcard_label = tk.Label(flashcard_window, text=flashcard_text)
                flashcard_label.pack()

        else:
            messagebox.showwarning("Warning", "No flashcards available. Add flashcards to view.")

    def start_quiz(self):
        if self.flashcards:
            # Implement quiz logic here
            messagebox.showinfo("Quiz", "Quiz mode is under construction. Stay tuned!")
        else:
            messagebox.showwarning("Warning", "No flashcards available. Add flashcards to take a quiz.")

    def clear_entries(self):
        self.word_entry.delete(0, tk.END)
        self.translation_entry.delete(0, tk.END)

if __name__ == "__main__":
    start = tk.Tk()
    software = FlashcardApp(start)
    start.mainloop()