def sum_to(n):
    if n == 0:                     
        return 0
    return n + sum_to(n - 1)      

assert sum_to(4) == 10
assert sum_to(0) == 0
assert sum_to(1) == 1
print("sum_to passed")            

def power(base,exponent):
    if exponent == 0:
        return 1
    print("called with", base, exponent)
    return base * power(base,exponent -1)
assert power(2, 3) == 8
assert power(5, 0) == 1 
assert power(3, 1) == 3
assert power(2, 10) == 1024
print("power passed")