class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

b = Book("king", "kingsman", 300)
print(b)
print(repr(b))
print([b])

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}: {self.marks}"

    def passed(self):
        return self.marks >= 40
s = Student("Asha", 85)
print(s)                               # Asha: 85
print(s.passed())                      # True
print(Student("Ravi", 30).passed())    # False
print(Student("Meena", 40).passed())   # True