class Book():
    def __init__(self, author,title):
        self.author=author
        self.title=title
    def display(self):
        print(self.title+", written by "+self.author)
a=Book("John Steinbeck","Of Mice and Men")
b=Book("Harper Lee","To Kill a Mockingbird")
a.display()
b.display()
