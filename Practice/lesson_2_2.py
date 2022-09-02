start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние в км: ")

diff = int(start) - int(end)
result = (diff / int(distance))*100
print(f'Расход топлива на: {distance} км = {result} литров')