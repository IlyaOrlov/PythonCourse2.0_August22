number = 55
guess = int(input(" Введите целое число: "))

if guess == number:
    print("Ура, Вы угадали!")
elif guess < number:
    print("Введите число побольше")
else:
    print("Введите число поменьше")
print("Завершено")