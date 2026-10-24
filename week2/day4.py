def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
assert safe_divide(6, 3) == 2.0
assert safe_divide(1, 0) is None
assert safe_divide(0, 5) == 0.0
assert safe_divide(6, -3) == -2.0
print("safe_divide passed")

def to_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default
assert to_int("42") == 42
assert to_int("abc") == 0
assert to_int("abc", -1) == -1
assert to_int("") == 0
print("to_int passed")

def safe_get(items, index, default=None):
  try:
    return items[index]
  except IndexError:
    return default
assert safe_get([10, 20], 1) == 20
assert safe_get([10, 20], 5, "none") == "none"
assert safe_get([], 0) is None
assert safe_get([10, 20], -1) == 20
print("safe_get passed")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
assert validate_age(25) == 25
assert validate_age(0) == 0

try:
    validate_age(-1)
    assert False, "should have raised ValueError"
except ValueError:
    pass

try:
    validate_age("20")
    assert False, "should have raised TypeError"
except TypeError:
    pass

print("validate_age passed")