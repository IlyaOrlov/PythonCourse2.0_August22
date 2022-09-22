st = 'В корзине бананов - 6, апельсинов - 5, лимонов - 9.'
dct = {5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

for key in dct:
    st = st.replace(str(key), str(dct[key]))
print(st)


