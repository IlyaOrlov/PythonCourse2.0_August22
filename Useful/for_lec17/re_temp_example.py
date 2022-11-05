from urllib import request
import re


req = request.Request('https://yandex.ru/pogoda/nizhny-novgorod?utm_source=home&utm_medium=web&utm_campaign=informer&utm_content=main_informer&utm_term=title&lat=56.326887&lon=44.005986')
response = request.urlopen(req)
web_page = response.read().decode()
print(web_page)

s = re.compile(r'"Текущая температура ([+|−]?\d+)')
res = re.findall(s, web_page)
print(res)
