import requests
import json
if __name__ == '__main__':
    post_url='https://fanyi.baidu.com/sug'
    # 进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #post请求参数处理(同get请求一致)
    word=input("enter a word:")
    data={
        'kw':word
    }
    #发送请求
    response=requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据：json()方法返回的是obj（如果确认响应数据是json类型的，才可以使用json()）
    dic_obj=response.json()
    print(dic_obj)
    #持久化存储
    fp=open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    fp.close()
    print("over~")
