class Book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author}"

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

class Transaction:
    def __init__(self, user, book, due_date):
        self.user = user
        self.book = book
        self.due_date = due_date

    def __str__(self):
        return f"User: {self.user}\nBook: {self.book}\nDue Date: {self.due_date}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book, due_date):
        if book in self.books and book.copies > 0:
            transaction = Transaction(user, book, due_date)
            self.transactions.append(transaction)
            book.copies -= 1
            return True
        else:
            return False

    def return_book(self, user, book):
        for transaction in self.transactions:
            if transaction.user == user and transaction.book == book:
                self.transactions.remove(transaction)
                book.copies += 1
                return True
        return False

    def list_books(self):
        for book in self.books:
            print(book)

    def list_users(self):
        for user in self.users:
            print(user)

    def list_transactions(self):
        for transaction in self.transactions:
            print(transaction)


if __name__ == "__main__":
    library = Library()

    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "1234567890", 5)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 3)

    user1 = User("shubh", "shubhankar2604@gmail.com")
    user2 = User("rohan", "thepic.booksb@gmail.com")

    library.add_book(book1)
    library.add_book(book2)

    library.add_user(user1)
    library.add_user(user2)

    library.borrow_book(user1, book1, "2023-10-15")
    library.borrow_book(user2, book2, "2023-10-20")

    library.return_book(user1, book1)

    print("\nList of Books:")
    library.list_books()

    print("\nList of Users:")
    library.list_users()

    print("\nList of Transactions:")
    library.list_transactions()
