class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        return f"Hi, Myself {self.name}"
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
    def greet(self):
        base = super().greet()
        return f"{base}, and I scored {self.marks}"
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def greet(self):
        base = super().greet()
        return f"{base}, and I teach {self.subject}"


t = Teacher("Meena", "Maths")
p = Person("asha")
s = Student("Ben", 85)
print(p.greet())
print(s.greet())
print(t.greet())
print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(p, Student))


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


animals = [Dog("Rex"), Cat("Tom"), Animal("Generic")]
for a in animals:
    print(a.name, a.speak())