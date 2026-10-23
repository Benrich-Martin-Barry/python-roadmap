def double_all(nums):
    return list(map(lambda n: n * 2, nums))

assert double_all([1, 2, 3]) == [2, 4, 6]
assert double_all([]) == []
assert double_all([-1]) == [-2]
print("double_all passed")

from functools import reduce
def product(nums):
  return reduce(lambda a,b: a*b, nums)

assert product([1, 2, 3, 4]) == 24
assert product([5]) == 5
assert product([2, -3]) == -6
print("product passed")

from functools import reduce
def sum_of_even_squares(nums):
    return reduce(lambda a,b:a+b,(map(lambda n: n**2,(filter(lambda n: n%2 == 0,nums)))),0)

assert sum_of_even_squares([1, 2, 3, 4]) == 20
assert sum_of_even_squares([]) == 0
assert sum_of_even_squares([1, 3]) == 0
print("sum_of_even_squares passed")