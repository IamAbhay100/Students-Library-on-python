class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks

    def availablebook(self):
        print("The books available in Library are :")
        for books in self.books:
            print(" *"+ books)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"you have been issused the book {bookname} please return in 30 Day!Enjoy the book ")
            self.books.remove(bookname) 
            return True       
        else :
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning the book.Have a nice Day!") 

    def donatebook(self,bookname):
        self.books.append(bookname)

class Student:

    def requestbook(self):
        self.book=input("enter the name of the book you want to borrow:")
        return self.book

    def returnbook(self):
        self.book=input("enter the name of the book you want to return:")
        return self.book
    def donatebook(self):
        self.book=input("enter the name of the book you want donate:")
        return self.book    

if __name__ == "__main__" :
    CentralLibrary=Library(["The Jungle Book","The Great Gatsby","Catch-22","Beloved"]) 
    student=Student()

    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Donate a book
        5. Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("enter the choise:"))

        if a==1:
            CentralLibrary.availablebook() 
        elif a==2:
            CentralLibrary.borrowBook(student.requestbook()) 
        elif a==3:
            CentralLibrary.returnbook(student.returnbook()) 
        elif a==4:
            CentralLibrary.donatebook(student.donatebook())
            print("Thanks for donates us book .that's mean us lots ! Have a nice day")
        elif a==5:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit() 
        else:
            print("invalid choise")            
