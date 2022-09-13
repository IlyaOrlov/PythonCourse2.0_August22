word = input("Введите слово, содержащее букву/буквы А,а: ")
word = word.replace("А", "*").replace("а", "*")
print(f"Результат: {word}")