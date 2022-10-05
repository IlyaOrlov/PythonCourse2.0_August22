start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = int(input("Расстояние: "))
diff = int(start) - int(end)
result = diff / distance
print(f"Расход бензина: {result}")
