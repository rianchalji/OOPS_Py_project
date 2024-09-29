class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = 'Available' if not self.is_issued else 'Issued'
        return f"'{self.title}' by {self.author} - {status}"
class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, book_title, user_name):
        for book in self.books:
            if book.title == book_title:
                if not book.is_issued:
                    book.is_issued = True
                    self.issued_books[book_title] = user_name
                    print(f"Book '{book_title}' issued to {user_name}.")
                    return
                else:
                    print(f"Sorry, '{book_title}' is already issued.")
                    return
        print(f"Book '{book_title}' not found in the library.")

    def return_book(self, book_title):
        if book_title in self.issued_books:
            for book in self.books:
                if book.title == book_title:
                    book.is_issued = False
                    user = self.issued_books.pop(book_title)
                    print(f"Book '{book_title}' returned by {user}.")
                    return
        print(f"Book '{book_title}' not found in issued books.")

    def show_available_books(self):
        print("\nAvailable books:")
        for book in self.books:
            if not book.is_issued:
                print(book)
my_library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)


my_library.issue_book("1984", "John Doe")


my_library.show_available_books()


my_library.return_book("1984")


my_library.show_available_books()
              
