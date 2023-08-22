#Movie Library
class Movie:
  def __init__(self, title, director, year, genre):
    self.title = title
    self.derector = director
    self.year = year
    self.genre = genre

  def display_info(self):
    print(self.title)
    print(self.derector)
    print(self.year)
    print(self.genre)

class MovieLibary:
  def __init__(self):
    self.movies = []

  def add_movie(self, movie):
    self.movies.append(movie)

  def List_movies(self):
    for movie in self.movies:
      print(f"The Movie Title is: {movie.title} \nThe Movie Direct by: {movie.derector} \nThe Movie realesed in: {movie.year} \nThe Movie Genre is: {movie.genre}")

if __name__ == "__main__":
  Movielibary = MovieLibary()

movie1 = Movie("PeakeyBlinder", "Ankon", 2023, "I AM PEAKEY BLINDER")
movie2 = Movie("IDF", "Ankon", 2023, "IDFC")
    
Movielibary.add_movie(movie1)
Movielibary.add_movie(movie2)
    
print("Movies in the library:")
Movielibary.List_movies()