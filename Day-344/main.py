import pandas as pd

class Analyzing_Movie_Ratings_Data:
    def data_summarry(self):
        movie_rating_data = {
        'Movie ID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Movie Title': [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight',
        'Pulp Fiction', 'Schindler\'s List', 'Inception',
        'Fight Club', 'Forrest Gump'
        ],
        'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Biography', 'Sci-Fi', 'Drama', 'Drama'],
        'Rating': [9.3, 9.2, 9.0, 8.9, 8.9, 8.8, 8.8, 8.8],
        'Number of Ratings': [2300000, 1600000, 2300000, 1700000, 1200000, 2000000, 1700000, 1900000]
    }
        
        data_frame = pd.DataFrame(movie_rating_data)

        avrage_rating = data_frame['Rating'].mean()
        total_numbers_of_ratings = data_frame['Number of Ratings'].sum()

        avrage_rating_for_each_genre = data_frame.groupby('Genre')['Rating'].mean()
        total_rating_for_each_genre = data_frame.groupby('Genre')['Rating'].sum()

        top_3_highest_rated_movie = data_frame.nlargest(3, 'Rating')[['Movie Title', 'Rating']]
        top_3_most_rated_movie = data_frame.nlargest(3, 'Number of Ratings')[['Movie Title', 'Number of Ratings']]

        print(f"Avrage Rating: {avrage_rating}\n Total Numbers Of Rating: {total_numbers_of_ratings}\nAvrage Rating For Each Genre: {avrage_rating_for_each_genre}\nTotal Rating For Each Genre: {total_rating_for_each_genre}\nTop 3 Highest Rated Movie: {top_3_highest_rated_movie}\nTop 3 Most Rated Movie: {top_3_most_rated_movie}")

if __name__ == "__main__":
    amrd = Analyzing_Movie_Ratings_Data()
    amrd.data_summarry()
