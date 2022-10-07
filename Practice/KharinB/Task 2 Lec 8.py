def read_gen(file_path):
    with open(file_path, 'r') as f:
        for j in f:
            yield j
#Я не понимаю почему это работает. Почему он перебирает по строчно? Это как-то связано с режимом буферизации, который при значании "1" происходи построчно?
            

for i in read_gen("text.txt"):
    print(i)
    print("____________")