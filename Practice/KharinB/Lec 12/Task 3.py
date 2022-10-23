import urllib.request as ur
import re


def check_link(path):
   with ur.urlopen(path) as resp:
      html = resp.read()
      html = html.decode("UTF-8")
      links = re.findall(r"http+s*://+\w[^\"]+", html)
      not_found_links = []
      for i in links:
         try:
            ur.urlopen(i)
         except:
            not_found_links.append(i)
      if not_found_links == []:
         not_found_links = "Нерабочие ссылки не найдены"
      return not_found_links


print(check_link(input("Введите ссылку") or "http://google.com"))
