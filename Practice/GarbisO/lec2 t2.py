start = int(input("Топлива было: "))
end = int(input("Топлива осталось: "))
distance = int(input("Расстояние: "))
diff = int(start) - int(end)
result = diff / distance
print(f"Расход топлива: {result}")