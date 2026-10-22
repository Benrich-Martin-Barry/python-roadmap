def squares(nums):
    return [n * n for n in nums]

assert squares([1, 2, 3]) == [1, 4, 9]
assert squares([]) == []
assert squares([-2, 5]) == [4, 25]
print("squares passed")

def evens(nums):
    return [n for n in nums if n % 2 == 0]

assert evens([1, 2, 3, 4]) == [2, 4]
assert evens([]) == []
assert evens([1, 3]) == []
print("evens passed")

def word_lengths(words):
  return{w:len(w) for w in words}
assert word_lengths(["a", "bb"]) == {"a": 1, "bb": 2}
assert word_lengths([]) == {}
assert word_lengths(["hi", "hi"]) == {"hi": 2}
print("word_lengths passed")