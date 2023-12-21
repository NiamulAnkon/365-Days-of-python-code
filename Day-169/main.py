import tkinter as tk
from tkinter import messagebox
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MovieRecommendationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Recommendation System")
        self.master.geometry("800x600")

        self.db_connection = sqlite3.connect("movie_database.db")
        self.create_table()

        self.label_genre = tk.Label(self.master, text="Enter Preferred Genre:")
        self.label_genre.pack()

        self.entry_genre = tk.Entry(self.master)
        self.entry_genre.pack()

        self.button_get_recommendations = tk.Button(self.master, text="Get Recommendations", command=self.get_recommendations)
        self.button_get_recommendations.pack(pady=10)

        self.recommendation_label = tk.Label(self.master, text="Recommended Movies:")
        self.recommendation_label.pack()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           title TEXT, 
                           genre TEXT, 
                           plot TEXT)''')
        self.db_connection.commit()

        # Inserting some example movies into the database
        cursor.execute("INSERT INTO movies (title, genre, plot) VALUES (?, ?, ?)",
                       ("Inception", "Sci-Fi", "A thief enters the dreams of others to steal their secrets."))
        cursor.execute("INSERT INTO movies (title, genre, plot) VALUES (?, ?, ?)",
                       ("The Shawshank Redemption", "Drama", "Two imprisoned men bond over a number of years."))
        cursor.execute("INSERT INTO movies (title, genre, plot) VALUES (?, ?, ?)",
                       ("The Dark Knight", "Action", "Batman faces a new adversary known as The Joker."))
        self.db_connection.commit()

    def get_recommendations(self):
        user_genre = self.entry_genre.get().lower()

        if user_genre:
            movies_data = self.fetch_movies_data()

            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(movies_data['plot'])

            cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

            movie_titles = movies_data['title']
            movie_indices = {title: idx for idx, title in enumerate(movie_titles)}

            recommended_movies = get_genre_recommendations(user_genre, cosine_similarities, movie_indices)

            recommendation_text = "\n".join(recommended_movies)
            self.recommendation_label.config(text=f"Recommended Movies:\n{recommendation_text}")
        else:
            tk.messagebox.showwarning("Empty Genre", "Please enter a preferred genre.")

    def fetch_movies_data(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT title, genre, plot FROM movies")
        movies_data = {'title': [], 'genre': [], 'plot': []}

        for row in cursor.fetchall():
            movies_data['title'].append(row[0])
            movies_data['genre'].append(row[1])
            movies_data['plot'].append(row[2])

        return movies_data


def get_genre_recommendations(user_genre, cosine_similarities, movie_indices):
    user_genre_lower = user_genre.lower()

    print("Movie Indices:", movie_indices)
    print("User Genre:", user_genre_lower)

    if user_genre_lower not in movie_indices:
        tk.messagebox.showwarning("Genre Not Found", f"No movies found for the genre '{user_genre}'.")
        return []

    idx = movie_indices[user_genre_lower]

    print("Selected Index:", idx)


if __name__ == "__main__":
    root = tk.Tk()
    movie_recommendation_app = MovieRecommendationApp(root)
    root.mainloop()
