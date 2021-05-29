import requests

if __name__ == '__main__':
    url = "http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply?bizType=1"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Cache-Control": "max-age=0",
        "Cookie": "JSESSIONID=D91BCDA726EC328B8816C38F1D2BA79B; arraycookie=wangban2",
        "Host": "cgs.gzjd.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    print(response.text)
