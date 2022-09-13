import random


def who_is_winner(first_man, second_man, type_of_hand):

    def winner():
        print("\nВы победили!\n")

    def looser():
        print("\nВы проиграли :(\n")

    def draw():
        print("\nУ вас ничья.\n")

    if first_man == second_man:
        draw()
        return

    loose_map = [2, 0, 1]
    result = loose_map[first_man]
    if result == second_man:
        looser()
    else:
        winner()


rps = ["Камень", "Ножницы", "Бумага"]

while True:
    print("Хотите сыграть? (Y/N)")
    set_game = input().upper()
    if set_game == "Y":
        for index in range(len(rps)):
            print(f"{index} - {rps[index]}")
        my_hand = int(input())
        computer_hand = random.randint(0, len(rps)-1)
        print(f"\n\nВаш выбор - {rps[my_hand]}, \nВыбор компьютера - {rps[computer_hand]}")
        who_is_winner(my_hand, computer_hand, rps)
    else:
        print("До новых встреч!")
        exit()
