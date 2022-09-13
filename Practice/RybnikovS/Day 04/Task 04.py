x = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]
current_index = 0
while True:
    question = input("Введите ваш вопрос: ")
    if question == "хватит":
        break
    print(x[current_index])
    current_index += 1
    current_index = current_index % len(x)
