import requests
from bs4 import BeautifulSoup
import re
import time
#这里列举的b站up主lex的例子（因为近期粉丝波动数量大，便于可视化观察，并无其他恶意）

def getdata(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    r = requests.get(url,headers=headers)
    r1 = r.content
    writefile("2.html",r1)    #储存视频网页文件源码

def writefile(filename,text):      #储存文件
    with open(filename,"wb") as f:
      f.write(text)
      f.close
      print("储存成功！")

def searchdata():            #匹配粉丝数
    file = open("2.html","r",encoding="utf-8")
    html = file.read()
    bs = BeautifulSoup(html,"html.parser")
    fm1 = bs.find('div',class_="up-info clearfix")
    fm2 = str(fm1)
    link = re.findall(linkfind,fm2)[0]
    return link

linkfind = re.compile(r'粉丝：(.*?)万')  #正则匹配规则

def main():
    linkstart = "https://search.bilibili.com/all?keyword=lex&from_source=nav_search_new"
    b = 15  #从下午15点开始爬取数据，设置为15
    while a==1:

       b1 = str(b)
       getdata(linkstart)
       link = b1+ "点lex的粉丝数："+searchdata()+'   \n'
       with open("2.txt","a") as f:  #存储数据到1.txt便于keshihua.py获取利用数据
         f.write(link)
         f.close
         print("储存成功！")
       time.sleep( 3600 )  #每小时爬取一次，单位秒
       b+=1


if __name__ == "__main__":
    main()
