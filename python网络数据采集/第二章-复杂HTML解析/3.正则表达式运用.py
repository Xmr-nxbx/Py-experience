import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://sc.chinaz.com/tupian/beijingtupian.html"
response = urlopen(url)
html = BeautifulSoup(response.read().decode("utf-8"),"html.parser")
#print(html)
print("搜图结果:")
for i in html.find_all("img",src2 = re.compile(".+\.jpg$")):
    print(i["src2"])
for i in html.find_all("img",src = re.compile(".+\.jpg$")):
    print(i["src"])