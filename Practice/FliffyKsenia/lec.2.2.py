start = input("Топлива было: ")
distance = input("Расстояние: ")
end = input("Топлива осталось: ")
diff = int(start) - int(end)
print (f"Result: {int (diff) / int (distance)}")

