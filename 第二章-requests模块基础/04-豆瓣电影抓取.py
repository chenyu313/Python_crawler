import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    #参数
    param={
        'type': '11',
        'interval_id': '100:90',
        'action':'',
        'start':'0', #从库中的第几个电影去取
        'limit':'20', #一次取出的个数
    }
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #获取响应对象
    response=requests.get(url=url,params=param,headers=headers)
    #返回响应数据
    list_data=response.json()
    #将数据写入
    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over~')
