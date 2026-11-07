class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, text):
        name, marks = text.split(",")
        return cls(name, int(marks))
    @staticmethod
    def is_valid_marks(value):
        return 0 <= value <= 100

s = Student.from_string("Ben,85")
print(s.name, s.marks)
print(Student.is_valid_marks(85))      # expect True
print(Student.is_valid_marks(150))     # expect False
s = Student.from_string("Meena,72")
print(Student.is_valid_marks(s.marks))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    @classmethod
    def square(cls,side):
        return cls(side , side)
    @staticmethod
    def is_valid(value):
        return 0 < value
r = Rectangle(3, 4)
print(r.area())                       # 12
sq = Rectangle.square(5)
print(sq.area())                      # 25
print(Rectangle.is_valid(-2))         # False



