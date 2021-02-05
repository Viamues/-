#-*- coding=utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

def getdata(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    r = requests.get(url,headers=headers)
    r1 = r.content
    writefile("1.html",r1)    #储存视频网页文件源码

def writefile(filename,text):      #储存文件
    with open(filename,"wb") as f:
      f.write(text)
      f.close
      print("储存成功！")

def searchdata():            #匹配图片url
    file = open("1.html","r",encoding="utf-8")
    html = file.read()
    bs = BeautifulSoup(html,"html.parser")
    fm1 = bs.find('meta',property="og:image")
    fm2 = str(fm1)
    link = re.findall(linkfind,fm2)[0]
    r = requests.get(link)
    r2 = r.content
    path = linkfinall+".jpg"
    writefile(path,r2)

linkfind = re.compile(r'content="(.*?)"')  #正则匹配规则
linkfinall = input("请输入视频的av号或bv号（如av1919810）：")

def main():
    linkstart = "https://www.bilibili.com/video/"+linkfinall
    getdata(linkstart)
    searchdata()




if __name__ == "__main__":
    main()
