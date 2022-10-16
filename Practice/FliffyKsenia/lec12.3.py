from urllib.request import urlopen
from urllib.parse import urlparse

# адрес на котором ищем все ссылки
url = "http://www.google.com"
# получаем страницу
page = urlopen(url)
# объявляем пустой массив для списка урл
urls = [[]]
# загружаем страницу в переменную html_bytes
html_bytes = page.read()
# декодируем страницу в кодировку utf-8
html = html_bytes.decode("utf-8")
# Убираем пробелы из страницы для избавления от возможного неправильно работающего парсера.
html = html.replace(" ","")
ind = 0
while ind>-1:
    # ищем ближайший тег а, который отвечает за ссылку
    ind = html.find("<a",ind+1)
    if ind>-1:
        # ищем свойство href в которой прописана ссылка
        indh = html.find("href=",ind)+6
        # ищем закрывающую кавычку и формируем строку для ссылки. от кавычки которая идет за href до следующей кавычки.
        ur = html[indh:html.find('"',indh)]
        "проверяем локальная ли это ссылка, если да, то превращаем в глобальную"
        if ur[0]=="/":
            ur = url+ur
        is_avail = False
        # проверяем на досупность ссылки в инернете
        try:
            p = urlopen(ur)
            is_avail= True
        except:
            pass
        # дописываем ссылку в массив ссылок
        urls.append([ur,is_avail])
    else:
        break

# выводим на экран получившийся массыв ссылок
print("Живость ссылки  | Ссылка")
urls.pop(0)
for u in urls:
    if u[1]:
        print(f"ссылка досупна  | {u[0]}")
    else:
        print(f"ссылка недосупна| {u[0]}")