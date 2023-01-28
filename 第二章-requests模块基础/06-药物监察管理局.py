import requests

if __name__ == '__main__':
    #批量获取不同企业的id值
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #参数的封装
    data={
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':'',
    }
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    #获取响应对象
    id_list=[] #存储企业的id
    json_ids=requests.post(url=url,headers=headers,data=data).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(id_list)

    #获得企业详细信息
    post_url=' http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=0f6eee9c663d4610882b9ff4ec4a4151'
    for id in id_list:
        data={
            'id':id
        }
        detail_json=requests.post(url=post_url,headers=headers,data=data).json()

