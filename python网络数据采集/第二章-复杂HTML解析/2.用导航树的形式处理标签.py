import urllib.request
from bs4 import BeautifulSoup

def main():
    url = r"file:///C:/Users/HP/Desktop/%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/Beautiful%20Soup%204.2.0%20%E6%96%87%E6%A1%A3%20%E2%80%94%20Beautiful%20Soup%204.2.0%20documentation.html"
    response = urllib.request.urlopen(url)
    html = BeautifulSoup(response.read().decode("utf-8"),"html.parser")
    for i in html.find("span").parent.parent.parent.next_siblings:  #父标签(parent),后面的兄弟(next_siblings)
        print(i)
    for j in html.find("th").descendants():#后代标签(descendants),儿子节点(children)
        print(j)
if __name__ == "__main__":
    main()