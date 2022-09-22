d = {"dog": "собака", "four": "четыре"}

for i in d.values():
    if i == "собака":
        print("нашлась")
        break
else:
    print("не нашлась")

#print("dog" in d)
