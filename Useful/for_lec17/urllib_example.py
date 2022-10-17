from urllib import request
import re


req = request.Request('https://yandex.ru/pogoda/nizhny-novgorod?lat=56.326887&lon=44.005986')
response = request.urlopen(req)
web_page = response.read().decode()

s = re.compile(r'Текущая температура</span><span class="temp__value temp__value_with-unit">([+|-]\d+)</span>')
res = re.findall(s, web_page)
print(res)
