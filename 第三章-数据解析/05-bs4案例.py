#需求：爬取三国演义小说的所有章节标题和章节内容
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #对首页的页面数据进行爬取
    url='http://www.gushicimingju.com/novel/sanguoyanyi/'
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).content
    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup=BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    div_text=soup.find_all()
    li_list=soup.select('div[class="main-content"] > ul > li')
    for li in li_list:
        title=li.a.string
        detail_url='http://www.gushicimingju.com'+li.a['href']
        #print(detail_url)
        #对详情页发起请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='shici-content check-more')
        #解析到了章节的内容
        content=div_tag.text
        #持久化存储
        fp=open('./sanguo/'+title+'.txt','w',encoding='utf-8')
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功~')


