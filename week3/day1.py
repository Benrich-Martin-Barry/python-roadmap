class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
      return self.pages > 300
    def read_pages(self,n):
       return self.pages - n
print(Book("a", "b", 500).is_long())     # True
print(Book("a", "b", 100).is_long())     # False
print(Book("a", "b", 300).is_long())     # False
print(Book("a", "b", 300).read_pages(100))