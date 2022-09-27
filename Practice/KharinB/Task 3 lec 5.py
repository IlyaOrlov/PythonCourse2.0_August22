text = "three little nigger boys walking in the zoo;\n" \
       "a big bear hugged one, and then there were two.\n" \
       "two little nigger boys sitting in the sun;\n" \
       "one got frizzled up, and then there was one.\n" \
       "one little nigger boy left all alone;\n" \
       "he went out and hanged himself and then there were none."
d = dict(one="1", two="2", three="3")
for _ in range(len(d)):
    el = d.popitem()
    text = text.replace(el[0], el[1])
print(text)
# Программа заменяет все подстроки, даже если это часть слова. Например "none", стало "n1".
# Можно было закончить на этом, но на меня напало вдохновение и я написал код ниже... Если у Вас нет вдохновения это проверять - не проверяйте

# d = dict(one = "1", two = "2", three = "3")
# screen = ""
# while True:# написал "генератор экрана", мне нужно экранировать подстроки, которые соответствуют ключу, но являются частью слова (none, alone - one)
#     screen += random.choice("!@#$%^&*()_+?.,")
#     if screen not in text: #экран генерируется пока последовательность из символов не будет отсутствовать в строке
#         break
# print(screen)
# for _ in range(len(d)):
#     el = d.popitem()
#     len_el = len(el[0])
#     for __ in range(text.count(el[0])):
#         idr = text.find(el[0])
#         if idr-1 > -1 and (text[idr-1] not in " .;.:,?!\n" or text[idr+len_el] not in " .;.:,?!\n"):
#             text = text.replace(el[0], screen, 1)
#         else:
#             text = text.replace(el[0], el[1], 1)
#     else:
#         text = text.replace(screen, el[0]) #возвращаю экранированные подстроки в исходный вид.
#
#
# print(text)
