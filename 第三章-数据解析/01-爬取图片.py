import requests

if __name__ == '__main__':
    url='https://i.guancha.cn/news/2022/08/24/20220824132633266.jpg'
    #content返回的是二进制形式的图片数据
    # text(字符串) content(二进制) json() (对象)
    img_data = requests.get(url=url).content

    with open('imgLibs/1.jpg', 'wb') as fp:
        fp.write(img_data)
    print('over~')