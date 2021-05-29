import json
import os
import random
import requests


# 下载验证码
def download_img(my_cookie, img_url, dir_path):
    imageHeader = {
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
def applyForm(my_cookie, imgCode):
    url = "http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/form"
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

    form_data = {
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

    data = json.dumps(form_data)
    print(data)
    res = requests.post(url, data=data, headers=form_header)
    errcode = json.loads(res.content)['error']
    print(str(res.content))
    if errcode == 1:
        print('提交表单的验证码识别成功--SUCCESS')
        return True
    else:
        print('提交表单的验证码识别失败--FAILED')
        return False


# 获取验证码并发送短信验证码
def getImgCodeAndSendPhoneCode(my_cookie, phone, imageCode):
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
        "Cookie": my_cookie,
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


# 提交手机收到的短信验证吗，以便进入下一步
def verifycode(my_cookie, applay_base_info, phone, img_code, phone_code):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/verifycode'
    data = {
        "bizType": "1",
        "bookMobile": phone,
        "business": "1",
        "imgCode": img_code,
        "isProxy": "1",
        "isProxyNew": "0",
        "load": "3",
        "origin": "0",
        "ownerId": applay_base_info['ownerId'],
        "ownerIdType": "N",
        "ownerName": applay_base_info['ownerName'],
        "plate": applay_base_info['plate'],
        "plateTemp": applay_base_info['plateTemp'],
        "plateTempHead": "粤",
        "plateTempTail": applay_base_info['plateTempTail'],
        "proxyId": applay_base_info['proxyId'],
        "proxyIdType": "A",
        "proxyName": applay_base_info['proxyName'],
        "sfzmhm": applay_base_info['sfzmhm'],
        "sfzmmc": "N",
        "source": "native",
        "syr": applay_base_info['syr'],
        "vehicleNo": applay_base_info['vehicleNo'],
        "vehiclePurpose": "5",
        "vehicleType": "H12",
        "verifycode": phone_code,
        "lack": {
            "ownerMobile": True
        },
    }

    print('[确认短信验证码]' + str(data))

    verify_code_header = {
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

    data = json.dumps(data)
    text = requests.post(url, data=data, headers=verify_code_header).text
    print('[确认短信验证码]' + text)


# 获取可抢的日期（最后一天）
def getApplyDay(my_cookie):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/days'
    applyDayHeader = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Connection": "keep-alive",
        "Cookie": my_cookie,
        "Host": "cgs.gzjd.gov.cn",
        "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    days = requests.get(url, headers=applyDayHeader)
    days_arr = json.loads(days.content)
    day = days_arr[len(days_arr) - 1]
    return day


# 查询指定分所的信息
def getOfficeInfo(my_cookie, officeName, day):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/offices?day=' + day
    remainCountHeader = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Connection": "keep-alive",
        "Cookie": my_cookie,
        "Host": "cgs.gzjd.gov.cn",
        "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    office_list = requests.get(url, headers=remainCountHeader)
    office_arr = json.loads(office_list.content)
    for office_obj in office_arr:
        if office_obj['name'] == officeName:
            return office_obj
    return


# 检查可约时段, 并选中时段提交申请
def checkAndChoiseTimeInterval(my_cookie, office_info, day):
    office_id = office_info['id']
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/quotas?officeId=' + str(office_id) + '&day=' + str(day)
    time_interval_Header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Connection": "keep-alive",
        "Cookie": my_cookie,
        "Host": "cgs.gzjd.gov.cn",
        "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    office_time_interval_resp = requests.get(url, headers=time_interval_Header)
    office_time_interval = json.loads(office_time_interval_resp.content)

    choisedQuota = None
    for quota_info in office_time_interval:
        amount = quota_info['amount']
        leftCount = quota_info['leftCount']
        # printLeftNum('基本信息', quota_info)

        # 剩余不多
        lackNum_flag = (amount > 3 and (leftCount / amount) < 1 / 3 or amount <= 3) & leftCount > 0
        if lackNum_flag is True:
            printLeftNum('剩余不多', quota_info)
            choisedQuota = quota_info
            continue

        # 紧张
        lack_flag = amount > 3 and (leftCount / amount) >= 1 / 3 and (leftCount / amount) <= 2 / 3
        if lack_flag is True:
            printLeftNum('余号紧张', quota_info)
            choisedQuota = quota_info
            continue

            # 充足
        adequate_flag = amount > 3 and (leftCount / amount) > 2 / 3
        if adequate_flag is True:
            printLeftNum('余号充足', quota_info)
            choisedQuota = quota_info
            break

    if leftCount > 0 and choisedQuota is not None:
        printLeftNum('**选择**', quota_info)
        # 选择并提交预约时段
        choiseRes = False
        # 循环提交选择的时段，直到成功
        while choiseRes is False:
            choiseRes = choiseQuota(my_cookie, office_info, choisedQuota)


# 打印剩余号段数
def printLeftNum(title, quota_info):
    amount = quota_info['amount']
    leftCount = quota_info['leftCount']
    time_id = quota_info['id']
    startTime = quota_info['startTime']
    endTime = quota_info['endTime']
    officeName = quota_info['officeName']
    officeId = quota_info['officeId']
    print(title + '--->（' + str(startTime) + ' ~ ' + str(endTime) + '）--->总数:' + str(amount) + '--->剩余:' + str(
        leftCount) + '--->officeName:' + str(officeName) + '--->time_id:' + str(time_id) + '--->officeId:' + str(
        officeId))


# 选择并提交预约时段
def choiseQuota(my_cookie, office_info, quota_info):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply/quotas'
    data = {
        'office': office_info,
        'quota': quota_info,
    }

    choiseQuotaHeader = {
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

    data = json.dumps(data)
    res = requests.post(url, data=data, headers=choiseQuotaHeader).text
    print('提交选择时段结果（null表示成功）：' + res)
    if res == 'null':
        print('提交选择时段成功')
        return True
    else:
        print('==================提交选择时段失败==================')
        return False


# 倒数第二步，查询提交结果
def checkSubmitResult(my_cookie):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply?bizType=1'
    check_submit_Header = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8",
        "Connection": "keep-alive",
        "Cookie": my_cookie,
        "Host": "cgs.gzjd.gov.cn",
        "Referer": "http://cgs.gzjd.gov.cn/vbook/portal/regist/apply/quota.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    check_res = requests.get(url, headers=check_submit_Header)
    check_res_json = json.loads(check_res.content)
    print('查询提交的结果' + str(check_res_json))
    return check_res_json


# 最终的提交
def finalSubmit(my_cookie, img_code):
    url = 'http://cgs.gzjd.gov.cn/vbook/api/portal/books/apply'
    data = {
        'imgCode': img_code
    }

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

    data = json.dumps(data)
    res = requests.post(url, data=data, headers=final_submit_header)
    print('final提交结果:' + res.text)

    errcode = json.loads(res.content)['code']
    # {"error":"图形验证码错误","code":"portal.verifycode.img.error"}
    if errcode == 'portal.verifycode.img.error':
        print('[final提交]验证码错误')
        return False
    elif errcode == '':
        print('[final提交]系统繁忙请稍后再试')
        return False
    else:
        return True


# 打印桃心
def printPeachHearts():
    print("\n".join([''.join(['*' * ((x - y) % 3) if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
            y * 0.1) ** 3 <= 0 else ' ' for x in range(-30, 30)]) for y in range(15, -15, -1)]))


# ============================================================主流程 start==================================================================

# 发送表单申请流程
def sendFormApply(my_cookie, img_url, dir_path):
    # 1、下载并识别验证码
    formImgCode = downloadAndRrecognizeImgCode(my_cookie, dir_path, img_url)
    # 2、提交基本信息表单
    res = applyForm(my_cookie, formImgCode)
    return res


# 下载并识别验证码
def downloadAndRrecognizeImgCode(my_cookie, dir_path, img_url):
    # 1、下载验证码图片
    img_path = download_img(my_cookie, img_url, dir_path)
    print('验证码路径:' + img_path)
    # 2、识别验证码
    formImgCode = recognizeCode(dir_path, img_path)
    print('验证码:' + formImgCode)
    return formImgCode


# 发送手机短信
def sendPhoneCode(my_cookie, phone, img_url, dir_path):
    # 1、下载验证码图片
    img_path = download_img(my_cookie, img_url, dir_path)
    print('发送手机验证码的验证码路径:' + img_path)

    # 2、识别验证码
    phoneImgCode = recognizeCode(dir_path, img_path)
    print('发送手机验证码的验证码:' + phoneImgCode)

    # 3、获取验证码并发送短信验证码
    res = getImgCodeAndSendPhoneCode(my_cookie, phone, phoneImgCode)
    return res


# 提交申请人和车牌等基本信息表单
def sendFormApplyFunc(my_cookie, img_url, dir_path):
    global res, count
    res = False
    count = 0
    while res is False:
        if count != 0:
            print('提交表单 验证码破解失败，再尝试一次')
        res = sendFormApply(my_cookie, img_url, dir_path)
    print('提交表单 申请完成')
    return res


# 发送短信验证码
def sendPhoneCodeFunc(my_cookie, phone, img_url, dir_path):
    global res, count
    res = False
    count = 0
    while res is False:
        if count != 0:
            print('发送短信 验证码破解失败，再尝试一次')
        res = sendPhoneCode(my_cookie, phone, img_url, dir_path)
    print('发送短信 申请完成')


# 查询指定分所的信息
def getOfficeBaseinfo(my_cookie, office_name):
    office_info = None
    count = 0
    while office_info is None:
        if count != 0:
            print("==================分所名字不对，请检查后重新输入==================")
            office_name = input("请输入分所名字：")
        # 查询指定分所的信息
        office_info = getOfficeInfo(my_cookie, office_name, day)
        count += 1
    return office_info


# ============================================================主流程 end==================================================================

# 最终提交
def finalSubmitRequest(my_cookie, dir_path, img_url):
    finalRes = False
    count = 0
    while finalRes is False:
        if count != 0:
            print("[final提交]验证码错误,再次尝试第" + str(count) + '次')
        # 1、下载并识别验证码
        imgCode = downloadAndRrecognizeImgCode(my_cookie, dir_path, img_url)
        print('[final提交]验证码:' + imgCode)
        finalRes = finalSubmit(my_cookie, imgCode)
        count += 1

    if finalRes is True:
        printPeachHearts()
    return finalRes


# 确认并提交手机短信验证码
def verifyPhoneCode(my_cookie, applay_base_info, phone, dir_path, img_url):
    # 下载并识别验证码
    img_code = downloadAndRrecognizeImgCode(my_cookie, dir_path, img_url)
    phone_code = input("请输入手机短信验证码:")
    print('==>' + phone_code)
    verifycode(my_cookie, applay_base_info, phone, img_code, phone_code)


if __name__ == '__main__':
    phone = '13728448480'
    # phone = '13733333333'
    officeName = '增城分所'

    dir_path = "/Users/knight/Desktop/mobvoi/valid_code/code/test"
    img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode" + '?' + str(random.randrange(50000, 60000))
    site_cookie = "JSESSIONID=4192B6AA9C34ED78C7F60F2DA92EF207; arraycookie=wangban2"



    print('==========================================《第一步》==========================================')
    # 1、发送表单申请
    applay_base_info = sendFormApplyFunc(site_cookie, img_url, dir_path)



    print('==========================================《第二步》==========================================')
    # 2、发送短信的验证码
    sendPhoneCodeFunc(site_cookie, phone, img_url, dir_path)
    # 3、提交短信验证码
    verifyPhoneCode(site_cookie, applay_base_info, phone, dir_path, img_url)


    # ==========================================前两步可省略，直接在网页上操作==========================================


    # print('==========================================《第三步》==========================================')
    # # 4、获取可抢的日期（最后一天）
    # day = getApplyDay(site_cookie)
    # # 5、查询指定分所的信息
    # office_info = getOfficeBaseinfo(site_cookie, officeName)
    # # 6、检查可约时段, 并选中时段提交申请
    # checkAndChoiseTimeInterval(site_cookie, office_info, day)
    #
    #
    #
    # print('==========================================《第四步》==========================================')
    # # 7、最后一步提交，提交成功就预约成功了
    # finalSubmitRequest(site_cookie, dir_path, img_url)
    # print('*********抢号成功*********')
