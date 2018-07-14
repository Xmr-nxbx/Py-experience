from bs4 import BeautifulSoup
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
html = BeautifulSoup(response.read().decode("utf-8"))
print(html)
print(html.title)