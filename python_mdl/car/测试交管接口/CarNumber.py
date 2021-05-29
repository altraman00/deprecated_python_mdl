import requests


class CarNumber(object):
    def __init__(self):
        self.home_index_url = 'http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/index.html'
        self.verifycode_url = 'http://cgs.gzjd.gov.cn/vbook/images/verifycode?0.6757248629952894'
        self.page_one_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/form'

        self.homeHeaders = {
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

    # 首次访问主页,用来获得cookie
    def getCookie(self):
        response = self.session.get(self.home_index_url, headers=self.homeHeaders)

    def login(self):
        validCode = input('输入验证码:')
        post_param = {
            'bizType': 1,
            'business': 1,
            'isProxy': 1,
            'isProxyNew': 0,
            'plateTempHead': '粤',
            'plateTempTail': 'AQY895',
            'origin': '0',
            'vehiclePurpose': 5,
            'load': 3,
            'vehicleNo': '0097',
            'ownerName': '顺捷荣达（广州）物流有限公司',
            'ownerIdType': 'N',
            'ownerId': '91440101MA5D2F9N5B',
            'proxyName': '谢熊波',
            'proxyId': '422432197607242554',
            'imgCode': 'ASAM',
            'plateTemp': '粤AQY895',
            'proxyIdType': 'A',
            'vehicleType': 'H19',
            'plate': None,
            'source': 'native',
            'sfzmhm': '91440101MA5D2F9N5B',
            'syr': '顺捷荣达（广州）物流有限公司',
            'sfzmmc': 'N',
            'lack': {
                'ownerMobile': True
            }
        }

        resp = requests.post(url=self.page_one_url, data=post_param, headers=self.homeHeaders)
        print(resp.text)


carNum = CarNumber()
carNum.login()
