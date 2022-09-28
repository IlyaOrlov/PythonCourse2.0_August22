def tab_space(p, tab_space="t"):
    try:
        f = open(p, "r+")
    except:
        print("Файл не найден")
    else:
        text = f.read()
        if tab_space == "s":
            text = text.replace("\t", " ")
        elif tab_space == "t":
            text = text.replace(" ", "\t")
        else:
            print("Неверно указан тип изменения")
            return None
        f.seek(0)
        f.write(text)
        f.close()


tab_space("text.txt")
