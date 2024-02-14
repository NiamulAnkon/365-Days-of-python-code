class Book_Managment_System:
    def __init__(self):
        self.books = []
        self.amount_books = 0
        self.catageory = []
        self.fav_books = []
        self.want_read = []
        self.done_read = []
    
    def create_account(self):
        self.user_name = input("Enter your username: ")
        self.password = input("Enter your password: ")
    
    def main_menu(self):
        while True:
            usr_choice = int(input(f"Welcome: {self.user_name}\n1.Add Books\n2.Check Books\n3.Add Fav Books\n4.Add Want To Read Books\n5.Add Done Reading Books\n6.Exit\nEnter your choice: "))

            if usr_choice == 1:
                self.add_books()
            elif usr_choice == 2:
                self.check_books()
            elif usr_choice == 3:
                self.add_fav()
            elif usr_choice == 4:
                self.want_read()
            elif usr_choice == 5:
                self.done_read()
            elif usr_choice == 6:
                print("GoodBye :)")
                break
        
    def add_books(self):
        self.book_name = input("Enter the name of the book you want to add: ")
        self.book_catageory = input("Enter your book Catageory: ")
        self.books.append(self.book_name)
        self.catageory.append(self.book_catageory)
    def check_books(self):
        print(f"The Books you added\n{self.book_name}, {self.book_catageory}")
    def add_fav(self):
        self.fav_book_name = input("Enter the name of your fav book: ")
        self.fav_books.append(self.fav_book_name)
    def want_read(self):
        self.want_read_book = input("Enter the name of the book you want to read: ")
        self.want_read.append(self.want_read_book)
    def done_read(self):
        self.done_read_book = input("Enter the name of the book you have done reading: ")
        self.done_read.append(self.done_read_book)


if __name__ == "__main__":
    book_app = Book_Managment_System()
    book_app.create_account()
    book_app.main_menu()