#Используя модуль urllib, соберите все ссылки на заданной веб-странице (http://google.com)
# и проверьте их работоспособность.
from urllib import request
import re


def urls(url):
    req = request.Request(url)
    res = request.urlopen(req)
    page = res.read()
    search = re.findall(r'href="(http(s?)://.*?)"', str(page))
    for i in search:
        print('Ссылка {} : {}'.format(i, url_success))

def url_success(url):
    req_suc = request.urlopen(url).decode()
    return req_suc.status_code == 200


urls('http://google.com')