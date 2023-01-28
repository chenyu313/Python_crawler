import re
import os
import requests
#需求：爬取一个网页的图片并保存
if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #创建一个文件夹，保存所有图片
    if not os.path.exists('./imgLibs'):
        os.mkdir('./imgLibs')
    url='https://www.guancha.cn/TaiWanJunShi/list_%d.shtml'
    pageNum=1
    for pageNum in range(1,16):
        #对应页码的url
        new_url=format(url%pageNum)
        print(new_url)
        #响应对象
        response = requests.get(url=url,headers=headers)
        response.encoding='utf-8'
        #获取响应数据
        page_text=response.text
        #使用聚焦爬虫将页面中的所有图片进行解析/提取
        ex ='<div class="main content-main">.*?<a href="(.*?)" target="_blank">(.*?)</div>'
        img_src_list=re.findall(ex,page_text,re.S)
        print(img_src_list)
