#n = int(input("Which table? "))
#for i in range(1, 11):
 #   print(f"{n} * {i} = {n*i}")


for i in range(1, 16):
    if i %3 ==0 and i %5==0:
        print("FizzBuzz")
    elif i %3==0:
        print("Fizz")
    elif i %5==0:
        print("Buzz")
    else:
        print(i)