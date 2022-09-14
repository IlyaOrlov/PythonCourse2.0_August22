print("Введите слово 'stop' для получения конечного результата")
number = ""

while True:
    n = input("Введите число: ")
    if n.lower() == "stop":
        break
    if not n.isdecimal():
        print("Вы ввели не число. Повторите ввод!")
    else:
        number += str(n)

print(f"Ваше число: {number}")




