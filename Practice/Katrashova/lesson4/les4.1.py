
a = 1
while a<=100:
    if a % 15 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")
    else:
        print(a)
    a = a + 1
