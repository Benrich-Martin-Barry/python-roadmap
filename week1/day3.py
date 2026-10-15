n = [9, 5, -1, 2]
big = n[0]
for x in n:
  if x > big:
    big = x
print(big)

nums = [3, 1, 3, 2, 1]
res = []
for a in nums:
  if a not in res:
    res.append(a)
print(res)