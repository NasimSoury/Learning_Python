class book():
    def __init__(self, title_input, pages_input):
        self.title= title_input
        self.pages=pages_input
        print("book created!")
    def show_book(self):
        print(f"{self.title} has {self.pages} pages!")

my_book=book("Harry Potter", 300)
my_book.show_book()
