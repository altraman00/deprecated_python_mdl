# -*-coding:utf-8 -*-
from __future__ import unicode_literals

import cookielib
import json
import sys
import time
import urllib2

import cv2
import requests

import predict_code

# 防止中文出错
reload(sys)
sys.setdefaultencoding('utf-8')


''' 获取验证码并识别验证码返回 '''


def get_image_code():
    global timestamp, opener
    # 这是一个get请求，获取图片资源
    image_code_url = "https://网页地址?timestamp=" + str(timestamp)
    res = opener.open(image_code_url).read()
    with open("%s.jpg" % 'image_code', "wb") as f:  # 将图片保存在本地
        f.write(res)
    image = cv2.imread('image_code.jpg')
    pre_code = predict_code.predict(image)  # 调用predict_code进行图片识别
    print '预测验证码为:%s' % (pre_code)
    return pre_code


''' 模拟登陆 '''


def login(username, password):
    pre_code = get_image_code()
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '124',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'zb.cninfo.com.cn:3367',
        'Origin': 'https://zb.cninfo.com.cn:8080',
        'Referer': 'https://zb.cninfo.com.cn:8080/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    }
    datas = {
        'checkCode': pre_code,
        'imageCode': timestamp,
        'password': password,
        'username': username,
    }

    posturl = 'https://zb.cninfo.com.cn:3367/api-a/user/login'
    response = requests.post(url=posturl, data=json.dumps(datas), headers=headers)
    res_content = response.content
    json_dict = json.loads(response.text)

    # 判断登陆失败，则重新登陆
    if json_dict['code'] != 0:
        res_content = login(username, password)

    print res_content
    print '登陆成功！'
    return res_content


if __name__ == "__main__":
    global opener, timestamp
    cookie = cookielib.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
    handler = urllib2.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    opener = urllib2.build_opener(handler)  # 通过handler来构建opener

    timestamp = unicode(long(time.time() * 1000))
    username = 'tuxiaochao'
    password = 'f6b1dba6158981dc2511d2276eed1acec8041cc6'
    login(username, password)
