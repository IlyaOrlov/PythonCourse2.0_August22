word = input("Введите слово: ")
if word.find("А") != -1 or word.find("а") != -1:
    wordNew = word.replace("А", '*')
    wordLast = wordNew.replace("а","*")
    print(f"В слове {word} буквы 'А' и 'а' заменены\nНовое слово: {wordLast}")
else:
    print(f"В слове {word} нет букв 'А' и 'а'")