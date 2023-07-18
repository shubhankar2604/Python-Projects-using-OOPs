class Library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("The Books present in the library are: ")
        for book in self.books:
            print(f" * {book}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please use it carefully and return it on time. Thank You")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry!! The book {bookName} is either not available to be borrowed or has been already issued to someone else. Please try after a few days. Thank You")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for adding/returning the book {bookName}. Hope you enjoyed it!!")



class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book.title()

    def returnBook(self):
            self.book = input("Enter the name of the book you want to add/return: ")
            return self.book.title()


if __name__ == "__main__":
    centralLibrary = Library(["Python", "Web Dev", "Java", "C++"])
    student = Student()
    while(True):
        welcomemsg = ''' ***** WELCOME TO THE LIBRARY *****
        Please choose one of the following options:
        Press 1 to List all the books
        Press 2 to request a book
        Press 3 to add or return a book
        Press 4 to Exit the Library
        '''
        print(welcomemsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thank You very much for choosing our Library!!")
            exit()
        else:
            print("Invalid Choice")
