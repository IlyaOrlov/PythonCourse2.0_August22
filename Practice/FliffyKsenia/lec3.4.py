#запрашиваем слово с буквой "А"
a = input ("Введите слово содержащее букву А: ")
# заменяем все варианты буквы "А" (англ. русскю.) на *
result = a.replace("A", "*").replace("a", "*").replace("А", "*").replace("а", "*")
#выводим на экран
print(f"Result: {result}")
