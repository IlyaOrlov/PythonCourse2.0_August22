def avg_speed(distance, time):
    return distance / time


print("Расчет средней скорости \nДля расчета требуется ввести часы и минуты раздельно")
time1 = float(input("Введите время движения (часы): "))
time2 = float(input("Введите время движения (минуты): "))
fulltime = time1 + time2 / 60
distance = float(input("Введите пройденное расстояние (км): "))
speed = avg_speed (distance, fulltime)
a=2
print(f"Средняя скорость {speed:.2f} км/ч")
