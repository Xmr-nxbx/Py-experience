import urllib.request
from bs4 import BeautifulSoup

url = r"file:///C:/Users/HP/Desktop/%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/Beautiful%20Soup%204.2.0%20%E6%96%87%E6%A1%A3%20%E2%80%94%20Beautiful%20Soup%204.2.0%20documentation.html"
response = urllib.request.urlopen(url)
html = response.read().decode()
bs1 = BeautifulSoup(html,"html.parser")
findlist = bs1.find_all("",{"class" : "section"})#或者 class_ = ""
for each in findlist:
    print(each.get_text())