import tkinter as tk
from tkinter import messagebox
import random

class Book_Recommendation_System:
    def __init__(self, master_root):
        self.master_root = master_root
        self.master_root.title("Book Recommendation System")
        self.master_root.geometry("800x600")

        self.user_profile = {"name": "", "favorite_genre": ""}

        self.label_name = tk.Label(self.master_root, text="Name:")
        self.label_name.pack()

        self.entry_name = tk.Entry(self.master_root)
        self.entry_name.pack()

        self.label_favorite_genre = tk.Label(self.master_root, text="Favorite Genre:")
        self.label_favorite_genre.pack()

        self.entry_favorite_genre = tk.Entry(self.master_root)
        self.entry_favorite_genre.pack()

        self.button_save_profile = tk.Button(self.master_root, text="Save Profile", command=self.save_profile)
        self.button_save_profile.pack(pady=10)

        self.button_get_recommendations = tk.Button(self.master_root, text="Get Recommendations", command=self.get_recommendations)
        self.button_get_recommendations.pack(pady=10)

        self.recommendation_label = tk.Label(self.master_root, text="Recommended Books:")
        self.recommendation_label.pack()

    def save_profile(self):
        self.user_profile["name"] = self.entry_name.get()
        self.user_profile["favorite_genre"] = self.entry_favorite_genre.get()
        messagebox.showinfo("Profile Saved", "Your profile has been saved.")

    def get_recommendations(self):
        recommended_books = self.generate_recommendations()

        recommendation_text = "\n".join(recommended_books)
        self.recommendation_label.config(text=f"Recommended Books:\n{recommendation_text}")

    def generate_recommendations(self):
        book_titles = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5", "Book 6"]
        return random.sample(book_titles, min(3, len(book_titles)))

if __name__ == "__main__":
    root = tk.Tk()
    book_recommendation_system = Book_Recommendation_System(root)
    root.mainloop()
