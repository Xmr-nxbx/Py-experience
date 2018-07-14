import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def main():
    url = "http://www.baidu.com"
    try:
        response = urllib.request.urlopen(url)
    except (urllib.error.HTTPError,urllib.error.URLError) as exce:
        print("打开网页出错:"+str(exce))
    else:
        html = response.read().decode()
        soup = BeautifulSoup(html)
        try:
            title = soup.title
        except AttributeError as reason:
            print("未找到标题")
        else:
            if title == None:
                print("未找到标题")
            else:
                print(title)

if __name__ == "__main__":
    main()