def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam"))               
print(is_palindrome("never odd or even"))   
print(is_palindrome("A man, a plan, a canal: Panama"))

def remove_duplicates(nums):
    res = []
    for x in nums:
        if x not in res:
            res.append(x)
    return res
print(remove_duplicates([1,1,2]))

def fizz_buzz(n):
    if n%3 == 0 and n%5 == 0:
      return "fizzbuzz"
    elif n%3 == 0:
      return "fizz"
    elif n%5 == 0:
      return "buzz"
    else:
      return n
for i in range(1,16):
  print(fizz_buzz(i))