start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние: ")

diff = int(start) - int(end)
result = diff / int(distance)
sred_result = result * 100

print(f"Автомобиль расходует на 1 км пути {result} литров")
print(f"Автомобиль расходует на 100 км пути {sred_result} литров")