import random

t = ("лимон", "клубничка", "вишенка", "банан", "7")
while True:
    s = input("Нажмите кнопку (stop - для остановки): ")
    if s == "stop":
        break

    print(f"{random.choice(t)}|{random.choice(t)}|{random.choice(t)}")
