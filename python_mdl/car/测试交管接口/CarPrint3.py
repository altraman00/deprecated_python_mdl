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

    imageHeader = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=A550517988D8DC12C5817E3AA6158F30; arraycookie=wangban2',
        'Host': 'cgs.gzjd.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode??0.883773825702513"
    img = requests.get(img_url, headers=imageHeader).content
    img_path = "/Users/pan.song/Desktop/sp_test.png"
    with open(img_path, 'wb') as f:
        f.write(img)
    file = {'file': open(img_path, 'rb')}
    user_info = {'name': 'letian'}
    r = requests.post("http://10.27.0.3:8080/ImageUpdate", data=user_info, files=file)
    r = json.loads(r.content)
    code = r['result']

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
        "imgCode": code,
        "plateTemp": "粤AQY910",
        "proxyIdType": "A"
    }
    data = json.dumps(data)
    print(data)
    text = requests.post(url, data=data, headers=Header).text
    print(text)