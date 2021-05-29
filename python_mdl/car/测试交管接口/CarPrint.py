import json

import requests

if __name__ == '__main__':
    url = "http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/form"
    Header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'Content-Length': '553',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=A550517988D8DC12C5817E3AA6158F30; arraycookie=wangban2',
        'Host': 'cgs.gzjd.gov.cn',
        'Origin': 'http://cgs.gzjd.gov.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    data = {
        "bizType": 1,
        "business": 1,
        "isProxy": 1,
        "isProxyNew": 0,
        "plateTempHead": "粤",
        "plateTempTail": "AQY910",
        "origin": "0",
        "vehiclePurpose": "5",
        "load": "3",
        "vehicleNo": "0793",
        "ownerName": "顺捷荣达（广州）物流有限公司",
        "ownerIdType": "N",
        "ownerId": "91440101MA5D2F9N5B",
        "proxyName": "谢雄波",
        "proxyId": "422432197607242554",
        "imgCode": "bsyx",
        "plateTemp": "粤AQY910",
        "proxyIdType": "A"
    }
    data = json.dumps(data)
    print(data)
    text = requests.post(url, data=data, headers=Header).text
    print(text)
