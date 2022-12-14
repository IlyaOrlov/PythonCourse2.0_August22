import random



 # 1.Напишите программу, которая выводит на экран числа от 1 до 100.
 # При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz.
 # Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz

for a in range(1, 101):
    if a % 15 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")
    else:
        print(a)

#  2.Составить программу, которая будет считывать введённое пятизначное число.
#  После чего, каждую цифру этого числа необходимо вывести в новой строке:
# Число: 10819
# 1 цифра равна 1
# 2 цифра равна 0
# 3 цифра равна 8
# 4 цифра равна 1
# 5 цифра равна 9

num = input("Enter a five-digit number: ")
if num.isnumeric():
    print(f"Number: {num} ")
    for n in range(0, len(num)):
        print(f"The {n + 1} digit is equal to {num[n]}")
else:
    print("You can only enter numbers")

# 3.Реализовать цикл, формирующий число из вводимых пользователем символов,
# пока не будет введено слово “stop” (или “Stop”, или “STOP”). Если пользователь ввел не числовой символ,
# вывести предупреждение и запросить новый символ.

num =""
while (num1 := input("Enter a numeric character: ")).lower() != "stop":
    if num1.isdecimal():
        num += num1
    else:
        print("You enter not numeric character")
else:
    print(f"Generated number: {int(num)}")



# 4.Написать приложение-спорщик (генератор ответов), отвечающее на все запросы пользователя последовательно фразами:
# "Ты сам-то понял, что написал?", "Аргументируй", "И?", пока пользователь не введёт слово “хватит”.

request = ""
answers = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
flag = True

while flag:
    for answer in answers:
        if request == "хватит":
            flag = False
            break
        else:
            request = input("Enter a request: ")
            print(answer)

# 5.Реализовать приложение, загадывающее целое число из заданного пользователем диапазона
#  и предлагающее пользователю это число угадать. Отгадывание числа должно быть реализовано в цикле:
#  пока пользователь не угадает, или не введет нечисловой символ, продолжать опрос.
#  Если пользователь вводит неправильное число, вывести подсказку: больше оно или меньше загаданного.


a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print(f"Диапазон от {a} до {b}")
c = random.randint(a, b)


while True:
    d = input("Введите целое число из заданного диапазона: ")
    if d.isdecimal():
        d = int(d)
        if d == c:
            print(f"Поздравляем! Вы угадали, загаданное число {c}")
            break
        elif d < c:
            print("Введённое число меньше загаданного, попробуйте ещё раз")
        elif d > c:
            print("Введённое число больше загаданного, попробуйте ещё раз")
    else:
        print("Вы ввели нечисловой символ")

# # 8.Написать приложение – игру "камень, ножницы, бумага".


instr = ["камень", "ножницы", "бумага"]


while True:
    user_instr = input("Введите один из вариантов - камень, ножницы или бумага: ")
    random_instr = random.randint(0, len(instr) - 1)
    comp_instr = instr[random_instr]

    if user_instr == comp_instr:
        print(f"Ничья: вы - {user_instr}, компьютер - {comp_instr}")
    elif user_instr == "камень":
        if comp_instr == "ножницы":
            print(f"Вы победили: вы - {user_instr}, компьютер - {comp_instr}")
        elif comp_instr == "бумага":
            print(f"Вы проиграли: вы - {user_instr}, компьютер - {comp_instr}")
    elif user_instr == "ножницы":
        if comp_instr == "бумага":
            print(f"Вы победили: вы - {user_instr}, компьютер - {comp_instr}")
        elif comp_instr == "камень":
            print(f"Вы проиграли: вы - {user_instr}, компьютер - {comp_instr}")
    elif user_instr == "бумага":
        if comp_instr == "камень":
            print(f"Вы победили: вы - {user_instr}, компьютер - {comp_instr}")
        elif comp_instr == "ножницы":
            print(f"Вы проиграли: вы - {user_instr}, компьютер - {comp_instr}")
    else:
        print("Вы ввели не верное значение")


