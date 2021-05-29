# coding=utf8
from __future__ import unicode_literals
import requests
import time

if __name__ == "__main__":
    #获取图片总数设置number
    number = 100
    for num in range(number):
        img_url = 'http://爬取的网页地址'
        data={'timestamp':unicode(long(time.time()*1000))}
        # print (img_url)
        res = requests.get(img_url,params=data)  # 这是一个get请求，获取图片资源
        with open("./download_image/%d.jpg" % num, "wb") as f:  # 将图片保存在本地
            f.write(res.content)
            print("%d.jpg" % num + "获取成功")