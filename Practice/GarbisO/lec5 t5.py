with open('exercise.txt') as file_original:
    text = file_original.read()
text = text.replace("\t", "    ")

with open("exercise1", "w") as file_out:
    file_out.write(text)

with open('exercise.txt') as file_original:
    text = file_original.read()
text = text.replace("    ", "\t")

with open("exercise1", "w") as file_out:
    file_out.write(text)