input_text_file = open("text_for_5_ex.txt", "r")
data = input_text_file.read()
input_text_file.close()

input_text_file = open("text_for_5_ex.txt", "w")
switch = int(input("Press 1: TAB to 4 space\n"
               "Press 2: 4 space to TAB\n"))
if switch == 1:
    data = data.replace("\t", "    ")
else:
    data = data.replace("    ", "\t")

input_text_file.write(data)
input_text_file.close()
