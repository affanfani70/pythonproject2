class library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayBooks(self):
        print("The availble books are: ")
        for book in self.books:
            print(book)
    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} and keep it safe and retrun it on time.")
            self.books.remove(bookName)
            return True
        else:
            print("The books you ordered is already taken. Please wait and check after few days.")
            return False
    def retrunBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for retruning book back. Hope you enjoyed.")

class Student:
    def requestBook(self):
        self.book = input("Enter the you want to withdrwal: ")
        return self.book
    def retrunBook(self):
        self.book = input("Enter the book you want to retrun: ")
        return self.book


if __name__=="__main__":
    royalLibrary = library(["algorthms, python notes, Django, Flask"])
    student = Student()
    
    while True:
        welcomeMsg = '''===Welcome to Royal library===
        1. List of all the Books.
        2. Request a Book
        3. Retrun a Book
        4. Exit the library'''
        print(welcomeMsg)
        a = int(input("Enter the choice number: "))
        if a==1:
            royalLibrary.displayBooks()
        elif a==2:
            royalLibrary.borrowBooks(student.requestBook())
        elif a==3:
            royalLibrary.retrunBook(student.retrunBook())
        elif a==4:
           print("Thanks for visiting the royal library.")
           exit()
        else:
            print("Enter the wrong input.")