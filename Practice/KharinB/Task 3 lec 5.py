text = "three little nigger boys walking in the zoo;\n" \
       "a big bear hugged one, and then there were two.\n" \
       "two little nigger boys sitting in the sun;\n" \
       "one got frizzled up, and then there was one.\n" \
       "one little nigger boy left all alone;\n" \
       "he went out and hanged himself and then there were none."
d = dict(one="1", two="2", three="3")
for el in d.items():
       text = text.replace(el[0], el[1])
print(text)
