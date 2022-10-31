s ="Белеет парус одинокой \nв тумане моря голубом!.."
d = {"Белеет": "one", "парус": "two", "моря": "three"}

print(f"До:\n{s}")
for i, value in d.items():
    s = s.replace(i, value)
print(f"После:\n{s}")