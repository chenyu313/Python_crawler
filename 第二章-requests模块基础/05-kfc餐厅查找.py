import requests

if __name__ == '__main__':
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data={
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10',
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #获取响应对象
    response=requests.post(url=url,data=data,headers=headers)
    #获取响应数据
    dic_obj=response.text
    print(dic_obj)
    #持久化存储
    fp=open('./kfc.text','w',encoding='utf-8')
    fp.write(dic_obj)
    fp.close()
    print('over~')