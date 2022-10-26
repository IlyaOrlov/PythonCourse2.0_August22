#вызываем библиотеки
import time
import random

#задаем время задержки
begin_time = 3
end_time = 6
vremy_random = random.randint(begin_time, end_time)


#создаем класс Pupil
class Pupil:

#определяем метод класса
    def solve_task(self):
        time.sleep(vremy_random)
        print("I'm not ready yet")


my_object = Pupil()
my_object.solve_task()