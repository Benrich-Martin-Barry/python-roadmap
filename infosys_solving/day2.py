def is_pal(s):
  if s[::-1] == s:
    return "yes"
  else:
    return "no"
print(is_pal(input()))

def is_total(nums):
  total = 0
  for n in nums:
    if n%2 == 0:
      total = total + n
  return total
print( is_total(list(map(int, input().split()))))

def reverse_w(words):
  return " ".join(words[::-1])
print(reverse_w(input().split()))


def dup(nums):
  res = []
  for n in nums:
    if n not in res:
      res.append(n)
  return res
nums = dup(list(map(int, input().split())))
print(*nums)
