import re
import os
import requests
#需求：爬取一个网页的图片并保存
if __name__ == '__main__':
    #创建一个文件夹，保存所有图片
    if not os.path.exists('./imgLibs'):
        os.mkdir('./imgLibs')
    url='https://www.guancha.cn/military-affairs/2022_08_24_654995.shtml'
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #响应对象
    response = requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    #获取响应数据
    page_text=response.text
    #使用聚焦爬虫将页面中的所有图片进行解析/提取
    ex ='<p align="center">.*?<img src="(.*?)" title.*?'
    img_src_list=re.findall(ex,page_text,re.S)
    #print(img_src_list)
    for src in img_src_list:
        #请求到图片的二进制数据
        img_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[-1]
        #图片存储的路径
        imgPath='./imgLibs/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,"下载成功~")