from random import random, randint

a = randint (1, 100)

if a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
elif a % 15 == 0:
    print("FizzBuzz")
else:
    print(a)