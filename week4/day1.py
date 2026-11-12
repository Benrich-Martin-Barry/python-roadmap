def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet


hello = make_greeter("Hello")
hi = make_greeter("Hi")

print(hello("Asha"))
print(hi("Ravi"))

def make_counter():
    count = 0

    def add_one():
        nonlocal count
        count = count + 1
        return count

    return add_one


c1 = make_counter()
c2 = make_counter()

print(c1())
print(c1())
print(c1())
print(c2())

def make_multiplier(n1):
    def multiply(n2):
        return n1 * n2
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))

def shout(text):
    return text.upper()


def apply_twice(func, value):
    return func(func(value))


print(apply_twice(shout, "hi"))
print(apply_twice(str.upper, "hi"))

def exclaim(text):
    return text + "!"

print(apply_twice(exclaim, "hi"))

def announce(func):
    def wrapper(*args):
        print("Calling", func.__name__)
        result = func(*args)
        print("Done")
        return result
    return wrapper


@announce
def add(a, b):
    return a + b


print(add(2, 3))