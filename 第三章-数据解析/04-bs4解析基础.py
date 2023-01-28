import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp=open('./test.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    #soup.tagName 返回的是html中第一次出现的tagName标签
    #print(soup.h4.a)

    #print(soup.find('h4'))

    #根据属性定位
    #print(soup.find('div',class_='main content-main'))

    #返回符合要求的所有标签
    #print(soup.find_all('h4'))

    #选择器
    print(soup.select('div > ul > li > h4 > a')[0].text)
    print("https://www.guancha.cn"+soup.select('div > ul > li > h4 > a')[0]['href'])
    print(soup.select('div > ul > li > div > span')[0].text)