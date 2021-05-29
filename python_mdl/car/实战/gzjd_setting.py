# 相关配置
import random

# 验证码下载后的存放地址
img_code_dir_path = "/Users/knight/Desktop/mobvoi/valid_code/code/test"

recognize_code_url = "http://10.27.0.3:8080/ImageUpdate"

my_cookie = "JSESSIONID=4192B6AA9C34ED78C7F60F2DA92EF207; arraycookie=wangban2"

# 图片验证码相关
img_code_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode" + '?' + str(random.randrange(50000, 60000))
img_code_header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': my_cookie,
    'Host': 'cgs.gzjd.gov.cn',
    'Upgrade-Insecure-Requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

# 表单提交相关
form_url = "http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/form"
form_header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
    'Content-Length': '553',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': my_cookie,
    'Host': 'cgs.gzjd.gov.cn',
    'Origin': 'http://cgs.gzjd.gov.cn',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/index.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

# 发送手机短信相关
send_phone_code_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/verifycode/send'
send_phone_code_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "41",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Origin": "http://cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/sms.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 验证手机短信相关
verify_phone_code_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/verifycode'
verify_phone_code_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "41",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Origin": "http://cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/sms.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 获取可选日期相关
apply_day_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/days'
apply_day_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 选择分所相关
office_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/offices?day=%s'
office_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 选择时段相关
time_interval_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/quotas?officeId=%s&day=%s'
time_interval_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 提交时段相关
choise_quota_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/quotas'
choise_quota_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "41",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Origin": "http://cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/confirm.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 倒数第二步，查询提交结果
check_submit_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply?bizType=1'
check_submit_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

# 最终识别验证码的提交
final_submit_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply'
final_submit_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "41",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": my_cookie,
    "Host": "cgs.gzjd.gov.cn",
    "Origin": "http://cgs.gzjd.gov.cn",
    "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/confirm.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}




# if __name__ == '__main__':
#     time_interval_url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/quotas?officeId=%s&day=%s'
#     time_interval_url = (time_interval_url % ('11111', '90'))
#     print(time_interval_url)
#
#     office_url = (office_url % (str(11)))
#     print(office_url)
