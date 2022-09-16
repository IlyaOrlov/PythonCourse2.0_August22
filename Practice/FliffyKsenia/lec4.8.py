#импортируем(подключаем) функцию random для возможности её использования
import random
# задаем компьютеру список слов для выбора
game_slovs = ['камень', 'ножницы', 'бумага']
# запрашиваем у пользователя камень, ножницы, бумага
while True:
    igrok = input("Введите камень, ножницы, бумага: ").lower()
    if igrok in game_slovs:
        break
# вызываем функцию рандом
vybor_kompyter = random.randint(0,2)
vybor_igroka = game_slovs.index(igrok.lower())
result_of_game = vybor_kompyter - vybor_igroka
# выводим на печать выбор компьютера
print("Выбор компьютера -", game_slovs[vybor_kompyter] )
#print(game_slovs.index(igrok.lower()))
#print("result of game",result_of_game)
#пишем условия выигрыша:
if result_of_game == 0:
    print("Ничья: ")
elif result_of_game == -1 or result_of_game == 2:
    print("Сожалеем, вы проиграли: ")
elif result_of_game == -2 or result_of_game == 1:
    print("Поздравляем, вы выиграли!: ")
#ничья = 0  пк = -1, 2 игрок = -2,1









