import urllib.request


def download_img(img_url):
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'Content-Length': '553',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=1FE5584BD6A9C478A6948679ECC345C3; arraycookie=wangban2',
        'Host': 'cgs.gzjd.gov.cn',
        'Origin': 'http://cgs.gzjd.gov.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        img_name = "img.png"
        filename = "/Users/knight/Desktop/mobvoi/valid_code/code" + img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"


if __name__ == '__main__':
    # 下载要的图片
    img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode?0.44907287897441384"
    download_img(img_url)
