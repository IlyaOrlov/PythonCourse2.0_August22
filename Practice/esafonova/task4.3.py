print("Введите слово 'stop' для получения конечного результата")
number = ""

while True:
    n = input("Введите число: ")
    if n == "stop" or n == "Stop" or n == "STOP":
        break
    if not n.isdecimal():
        print("Вы ввели не число. Повторите ввод!")
        continue
    else:
        number += str(n)

print(f"Ваше число: {number}")




