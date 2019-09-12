class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    
    def printBook(self):
        print(self.title + ", " + self.isbn)

def main():
    b1 = Book("hsdf", "q3eqw")
    b1.printBook()

if __name__ == '__main__':
    main()


