import pickle
import random
# задаем имя файла данных, через который будет проходить обмен
config_file_name = "human.data"
# создаем класс Человек.
class Human():
    def __init__(self,name = "", sex = "", age = 0, growth = 0, weight = 0, race = ""):
        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth
        self.weight = weight
        self.race = race

    # создаем процедуру вывода данных о человеке
    def __str__(self):
        return f"Имя: {self.name}, пол: {self.sex}, возраст: {self.age}, вес: {self.growth}, рост: {self.weight}, национальность: {self.race}"
# создаем функцию для сохранения данных на диск.
def backup(number):
    # создаем массив с именами людей
    names = ["Саша","Женя","Валя","Вася","Степа","Рося"]
    # создаем массив возможных полов у человека
    sexs = ["мужской","женский"]
    # создаем список рас у людей
    races = [["Японец", "Кореец", "Китаец", "Европеец", "Американец", "Русский"],["Японка", "Корейка", "Китайка", "Европека", "Американка", "Русская"]]
    # объявляем пустой массив людей данные которых надо будет сохранить
    backup_humans = []
    # создаем людей по количеству которое нам необходимо из переменной number, которая пришла из места выхова процедуры.
    for i in range(number):
        # выбираем пол будущего человека
        sex = random.randint(0, 1)
        # добавляем в массыв людей нового человека.
        backup_humans += [Human(names[random.randint(0,5)],sexs[sex],random.randint(0,100),random.randint(10,200),random.randint(50,220),races[sex][random.randint(0,5)])]
        # сохраняем массив людей на диск.
    with open('config_file_name', 'wb') as f:
        pickle.dump(backup_humans, f)
# функция востановления данных о людях.
def restore():
    # загружаем из файла данные о людях
    with open('config_file_name', 'rb') as f:
        # десериализовываем данные о людях
        restore_humans = pickle.load(f)
    # возвращаем востановленные данные о людях
    return restore_humans

# вызываем функцию создания данных о 9 людях, с сериализацией в файл на диске
backup(9)
# вызываем функцию десериализаци данных о людях из файла на диске
humans = restore()
# выводим десериализованные данные на экран.
for human in humans:
    print(human)