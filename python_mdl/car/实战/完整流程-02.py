import json
import os
import random
import requests


# 下载验证码
def download_img(cookie, img_url, dir_path):
    imageHeader = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'cgs.gzjd.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    r = requests.get(img_url, headers=imageHeader, stream=True)
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        img_name = img_url.split('?').pop() + '.png'
        img_path = dir_path + '/' + img_name
        with open(img_path, 'wb') as f:
            f.write(r.content)
        return img_path


# 识别验证码
def recognizeCode(dir_path, img_path):
    file_rb = open(img_path, 'rb')
    file = {'file': file_rb}
    user_info = {'name': 'letian'}
    r = requests.post("http://10.27.0.3:8080/ImageUpdate", data=user_info, files=file)
    print(r.content)
    try:
        code = json.loads(r.content)['result']
    except:
        print("解析异常")
        pass

    newImgename = "{}.png".format(code)
    newImagePathStr = dir_path + "/" + newImgename
    cmd = f"mv {img_path} {newImagePathStr}"
    os.system(cmd)
    return code


# 提交第一步申请
def applyForm(cookie, imgCode):
    url = "http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/form"
    form_header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'Content-Length': '553',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': cookie,
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
        "imgCode": imgCode,
        "plateTemp": "粤AQY910",
        "proxyIdType": "A"
    }

    data = json.dumps(data)
    print(data)
    res = requests.post(url, data=data, headers=form_header)
    errcode = json.loads(res.content)['errcode']
    print(str(res.content))
    if errcode == 1:
        print('提交表单的验证码识别成功--SUCCESS')
        return True
    else:
        print('提交表单的验证码识别失败--FAILED')
        return False


# 获取验证码并发送短信验证码
def getImgCodeAndSendPhoneCode(cookie, phone, imageCode):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/verifycode/send'
    data = {
        "mobile": phone,
        "imgCode": imageCode
    }

    phoneCodeHeader = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "41",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": cookie,
        "Host": "cgs.gzjd.gov.cn",
        "Origin": "http://cgs.gzjd.gov.cn",
        "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/sms.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    data = json.dumps(data)
    text = requests.post(url, data=data, headers=phoneCodeHeader).text
    print('send phone code result' + text)

    if text == 'null':
        return True
    else:
        return False


# 发送表单申请流程
def sendFormApply(cookie, img_url, dir_path):
    # 1、下载验证码图片
    img_path = download_img(cookie, img_url, dir_path)
    print('提交表单的验证码路径:' + img_path)
    # 2、识别验证码
    formImgCode = recognizeCode(dir_path, img_path)
    print('提交表单的验证码:' + formImgCode)
    # 3、提交基本信息表单
    res = applyForm(cookie, formImgCode)
    return res


def sendPhoneCode(cookie, phone, img_url, dir_path):
    # 1、下载验证码图片
    img_path = download_img(cookie, img_url, dir_path)
    print('发送手机验证码的验证码路径:' + img_path)

    # 2、识别验证码
    phoneImgCode = recognizeCode(dir_path, img_path)
    print('发送手机验证码的验证码:' + phoneImgCode)

    # 3、获取验证码并发送短信验证码
    res = getImgCodeAndSendPhoneCode(cookie, phone, phoneImgCode)
    return res


if __name__ == '__main__':
    phone = '13728448480'
    # phone = '13733333333'
    dir_path = "/Users/knight/Desktop/mobvoi/valid_code/code/test"
    img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode" + '?' + str(random.randrange(50000, 60000))
    cookie = "JSESSIONID=A550517988D8DC12C5817E3AA6158F30; arraycookie=wangban2"

    print('==========================================《第一步》==========================================')
    # 1、发送表单申请
    res_1 = False
    count = 0
    while res_1 is False:
        if count != 0:
            print('提交表单 验证码破解失败，再尝试一次')
        res_1 = sendFormApply(cookie, img_url, dir_path)
    print('提交表单 申请完成')

    print('==========================================《第二步》==========================================')

    # 2、发送短信的验证码
    res_1 = False
    count = 0
    while res_1 is False:
        if count != 0:
            print('发送短信 验证码破解失败，再尝试一次')
        res_1 = sendPhoneCode(cookie, phone, img_url, dir_path)
    print('发送短信 申请完成')

