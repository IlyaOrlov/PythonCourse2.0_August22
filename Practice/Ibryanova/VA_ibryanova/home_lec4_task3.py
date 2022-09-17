a = ""




while not (a := input("Введите число: ")).isdecimal():
   if a == "stop":
       break
else:
   print("Введено не число!")
print("Завершено")


#num =""
#while (num1 := input("Enter a numeric character: ")).lower() != "stop":
#   if num1.isdecimal():
#       num += num1
 #   else:
#      print("You enter not numeric character")
#else:
#   print(f"Generated number: {int(num)}")
