#Bookstore Inventory
class Book:
  def __init__(self, title, author, genre, price):
    self.title = title
    self.author = author
    self.genre = genre
    self.price = price

  def display_info(self):
    print(f"Title:{self.title} \nAuthor:{self.author} \nGenre:{self.genre} \nPrice:{self.price}")


class Bookstore:
  def __init__(self, name, price):
    self.name = name
    self.books = []
    
  def add_books(self, book):
    self.books.append(book)

  def list_books(self):
    for book in self.books:
      print(book.title)
      print(book.price)

if __name__ == "__main__":
    bookstore = Bookstore("Wonderful Books")

book1 = Book("The Subtitle art", "Ankon", "Morden", 60)
book2 = Book("The Motive of Life", "Anonto", "Motivetaed", 100)

bookstore.add_books(book1)
bookstore.add_books(book2)

print("Books in the store:")
bookstore.list_books()