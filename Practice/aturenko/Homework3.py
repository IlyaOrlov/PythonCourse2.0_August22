# 1.Написать программу для расчёта периметра прямоугольника по введённым длине и ширине.

a = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the width of the rectangle: "))
res = 2 * a + 2 * b
print(f"The perimeter of the rectangle is {res}")

# 2.Написать программу для расчёта средней скорости автомобиля по введённым значениям времени и расстояния,
# пройденного за это время.

t = float(input("Enter the time in hours: "))
s = float(input("Enter the distance in kilometers: "))
v = s/t
print(f"The average speed of the car is {v} kilometers per hour")

# 3.Написать две программы: одна должна шифровать введённый пользователем цифровой пароль при помощи секретного кода,
# другая – расшифровывать получившийся результат при помощи ЭТОГО ЖЕ секретного кода.

password = int(input("Enter 5 integers from 0 to 9: "))
key = 12345
result = password ^ key
print(result)          # Выводит пароль в зашифрованном виде
code = result
decoding = code ^ key
print(decoding)        # Выводит расшифрованный пароль

# 4.Написать программу, заменяющую все буквы “А” в слове, введённом пользователем, на символ “*”.

word = str(input("Enter one word: "))

if "a" in word:
    word2 = word.replace("a","*")
if "A" in word:
    word3 = word2.replace("A", "*")
else:
    print("There is no letter 'A' in this word")

print(word3)

# 5. Написать программу, проверяющую, что слово, введённое пользователем,
# является палиндромом (примеры: “Топот”, “Довод”). Программа должна выводить True или False

pal = str(input("Enter one word: "))

if pal[0:] == pal[::-1]:
    print(True)
else:
    print(False)



