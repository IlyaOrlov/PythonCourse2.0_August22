from urllib import request
import re


req = request.Request('http://google.com')
response = request.urlopen(req)
web_page = response.read().decode()


s = re.compile(r'"http[\/\:a-zA-Z\.\d\?\=]+[^\":]')

res = re.findall(s, web_page)
print(res)

