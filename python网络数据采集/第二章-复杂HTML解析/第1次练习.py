from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import urllib.request

def main():
    url = "http://sc.chinaz.com/tupian/beijingtupian.html"#站长素材网
    response = urlopen(url)
    bs1 = BeautifulSoup(response.read().decode("utf-8"),"html.parser")
    print("结果:")
    list1 = []
    for each in bs1.find_all("img",src2 = re.compile(".+\.jpg$")):
        list1.append(each)
        print(list1[-1])
    if len(list1) == 0:
        print("错误")
        return None
    else:#写文件:
        try:
            os.mkdir("网络爬虫图片")
        except:
            try:
                os.rmdir("网络爬虫图片")
                os.mkdir("网络爬虫图片")
            except:
                print("出错")
                return None
        os.chdir(r".\网络爬虫图片")
        for each in list1:
            name = str(each["alt"])
            urllib.request.urlretrieve(each["src2"],name+".jpg")    #新东西:urlretrieve(url, filename=None, reporthook=None, data=None)
    print("完成!")

if __name__ == "__main__":
    main()  ##注意,不能改变urlopen的循环读取!