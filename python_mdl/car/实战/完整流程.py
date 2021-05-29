import json
import os
import sys

import requests

# 下载验证码
from car.实战 import gzjd_setting


# 下载图片验证码
def download_img():
    # 验证码下载后的存放地址
    dir_path = gzjd_setting.img_code_dir_path
    r = requests.get(gzjd_setting.img_code_url, headers=gzjd_setting.img_code_header, stream=True)
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        img_code_url = gzjd_setting.img_code_url
        img_name = img_code_url.split('?').pop() + '.png'
        img_path = dir_path + '/' + img_name
        with open(img_path, 'wb') as f:
            f.write(r.content)
        return img_path


# 识别验证码
def recognizeCode(img_path):
    file_rb = open(img_path, 'rb')
    file = {'file': file_rb}
    user_info = {'name': 'letian'}
    r = requests.post(gzjd_setting.recognize_code_url, data=user_info, files=file)
    print(r.content)
    try:
        code = json.loads(r.content)['result']
    except:
        print("解析异常")
        pass

    new_imge_name = "{}.png".format(code)
    new_image_path_str = gzjd_setting.img_code_dir_path + "/" + new_imge_name
    cmd = f"mv {img_path} {new_image_path_str}"
    os.system(cmd)
    return code


# 提交第一步申请
def applyForm(form_data, img_code):
    form_data['imgCode'] = img_code
    data = json.dumps(form_data)
    print(data)
    form_res = requests.post(gzjd_setting.form_url, data=data, headers=gzjd_setting.form_header)
    print(str(form_res.content))

    # 成功和失败时的返回值不一样
    try:
        res_code = json.loads(form_res.content)['code']
    except:
        res_code = ''
        pass

    if res_code == 'portal.verifycode.img.error':
        print('提交表单的验证码识别失败--FAILED')

    try:
        # 有时候返回errcode，有时候返回error，验证成功时返回errcode
        # error = json.loads(form_res.content)['error']
        err_code = json.loads(form_res.content)['errcode']
    except:
        err_code = -1
        pass

    if err_code == 1:
        print('提交表单的验证码识别成功--SUCCESS')
        return True
    else:
        print('提交表单的验证码识别失败--FAILED')
        return False


# 获取验证码并发送短信验证码
def getImgCodeAndSendPhoneCode(phone, phone_img_code):
    data = {
        "mobile": phone,
        "imgCode": phone_img_code
    }
    data = json.dumps(data)
    text = requests.post(gzjd_setting.send_phone_code_url, data=data, headers=gzjd_setting.send_phone_code_header).text
    print('send phone code result' + text)

    if text == 'null':
        return True
    else:
        return False


# 提交手机收到的短信验证吗，以便进入下一步
def verifycode(apply_base_info, phone, img_code):
    phone_code = input("请输入手机号" + phone + "的短信验证码:")
    print('==>' + str(phone_code))

    ownerId = apply_base_info['ownerId']
    ownerName = apply_base_info['ownerName']
    plate = apply_base_info['plateTemp']
    plateTemp = apply_base_info['plateTemp']
    plateTempTail = apply_base_info['plateTempTail']
    proxyId = apply_base_info['proxyId']
    proxyName = apply_base_info['proxyName']
    sfzmhm = apply_base_info['ownerId']
    syr = apply_base_info['ownerName']
    vehicleNo = apply_base_info['vehicleNo']

    data = {
        "bizType": "1",
        "bookMobile": phone,
        "business": "1",
        "imgCode": img_code,
        "isProxy": "1",
        "isProxyNew": "0",
        "load": "3",
        "origin": "0",
        "ownerId": ownerId,
        "ownerIdType": "N",
        "ownerName": ownerName,
        "plate": plate,
        "plateTemp": plateTemp,
        "plateTempHead": "粤",
        "plateTempTail": plateTempTail,
        "proxyId": proxyId,
        "proxyIdType": "A",
        "proxyName": proxyName,
        "sfzmhm": sfzmhm,
        "sfzmmc": "N",
        "source": "native",
        "syr": syr,
        "vehicleNo": vehicleNo,
        "vehiclePurpose": "5",
        "vehicleType": "H12",
        "verifycode": phone_code,
        "lack": {
            "ownerMobile": True
        },
    }
    print('[确认短信验证码]' + str(data))

    data = json.dumps(data)
    text = requests.post(gzjd_setting.verify_phone_code_url, data=data,
                         headers=gzjd_setting.verify_phone_code_header).text
    print('[确认短信验证码]' + text)


# 获取可抢的日期（最后一天）
def getApplyDay():
    days = requests.get(gzjd_setting.apply_day_url, headers=gzjd_setting.apply_day_header)
    print(str(days.content))
    days_arr = json.loads(days.content)
    res_code = days_arr['code']
    if res_code == 'portal.apply.form.empty':
        print('================请先填写预约基本信息================')
        print('================请先填写预约基本信息================')
        print('================请先填写预约基本信息================')
        print('================请先填写预约基本信息================')

        print('\n》》》》》》》》》》》退出程序》》》》》》》》》》》》》')
        sys.exit(0)
    day = days_arr[len(days_arr) - 1]
    return day


# 查询指定分所的信息
def getOfficeInfo(officeName, day):
    office_url = (gzjd_setting.office_url % (str(day)))
    office_list = requests.get(office_url, headers=gzjd_setting.office_header)
    office_arr = json.loads(office_list.content)
    # {'error': '请先填写预约基本信息', 'code': 'portal.apply.form.empty'}
    for office_obj in office_arr:
        if office_obj['name'] == officeName:
            return office_obj
    return


# 检查可约时段, 并选中时段提交申请
def checkAndChoiseTimeInterval(office_info, day):
    office_id = office_info['id']
    time_interval_url = (gzjd_setting.time_interval_url % (str(office_id), str(day)))
    office_time_interval_resp = requests.get(time_interval_url, headers=gzjd_setting.time_interval_header)
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
            choiseRes = choiseQuota(office_info, choisedQuota)


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
def choiseQuota(office_info, quota_info):
    data = {
        'office': office_info,
        'quota': quota_info,
    }
    data = json.dumps(data)
    res = requests.post(gzjd_setting.choise_quota_url, data=data, headers=gzjd_setting.choise_quota_header).text
    print('提交选择时段结果（null表示成功）：' + res)
    if res == 'null':
        print('提交选择时段成功')
        return True
    else:
        print('==================提交选择时段失败==================')
        return False


# 倒数第二步，查询提交结果
def checkSubmitResult():
    check_res = requests.get(gzjd_setting.check_submit_url, headers=gzjd_setting.check_submit_header)
    check_res_json = json.loads(check_res.content)
    print('查询提交的结果' + str(check_res_json))
    return check_res_json


# 最终的提交
def finalSubmit(img_code):
    data = {
        'imgCode': img_code
    }
    data = json.dumps(data)
    res = requests.post(gzjd_setting.final_submit_url, data=data, headers=gzjd_setting.final_submit_header)
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
def sendFormApply(form_data):
    # 1、下载并识别验证码
    formImgCode = downloadAndRrecognizeImgCode()
    # 2、提交基本信息表单
    res = applyForm(form_data, formImgCode)
    return res


# 下载并识别验证码
def downloadAndRrecognizeImgCode():
    # 1、下载验证码图片
    img_path = download_img()
    print('验证码路径:' + img_path)
    # 2、识别验证码
    formImgCode = recognizeCode(img_path)
    print('验证码:' + formImgCode)
    return formImgCode


# 发送手机短信
def sendPhoneCode(phone):
    # 1、下载验证码图片
    img_path = download_img()
    print('发送手机验证码的验证码路径:' + img_path)

    # 2、识别验证码
    phone_img_code = recognizeCode(img_path)
    print('发送手机验证码的验证码:' + phone_img_code)

    # 3、获取验证码并发送短信验证码
    res = getImgCodeAndSendPhoneCode(phone, phone_img_code)
    return res


# 提交申请人和车牌等基本信息表单
def sendFormApplyFunc(form_data):
    global res, count
    res = False
    count = 0
    while res is False:
        if count != 0:
            print('提交表单 验证码破解失败，再尝试一次')
        res = sendFormApply(form_data)
    print('提交表单 申请完成')
    return res


# 发送短信验证码
def sendPhoneCodeFunc(phone):
    global res, count
    res = False
    count = 0
    while res is False:
        if count != 0:
            print('发送短信 验证码破解失败，再尝试一次')
        res = sendPhoneCode(phone)
    print('发送短信 申请完成')


# 查询指定分所的信息
def getOfficeBaseinfo(office_name, day):
    office_info = None
    count = 0
    while office_info is None:
        if count != 0:
            print("==================分所名字不对，请检查后重新输入==================")
            office_name = input("请输入分所名字：")
        # 查询指定分所的信息
        office_info = getOfficeInfo(office_name, day)
        count += 1
    return office_info


# ============================================================主流程 end==================================================================

# 最终提交
def finalSubmitRequest():
    finalRes = False
    count = 0
    while finalRes is False:
        if count != 0:
            print("[final提交]验证码错误,再次尝试第" + str(count) + '次')
        # 1、下载并识别验证码
        imgCode = downloadAndRrecognizeImgCode()
        print('[final提交]验证码:' + imgCode)
        finalRes = finalSubmit(imgCode)
        count += 1

    if finalRes is True:
        printPeachHearts()
    return finalRes


# 确认并提交手机短信验证码
def verifyPhoneCode(form_data, phone):
    # 下载并识别验证码
    img_code = downloadAndRrecognizeImgCode()
    verifycode(form_data, phone, img_code)


if __name__ == '__main__':
    phone = '13728448480'
    # phone = '13733333333'
    officeName = '增城分所'
    # officeName = '化龙分所'

    # img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode" + '?' + str(random.randrange(50000, 60000))
    # site_cookie = "JSESSIONID=4192B6AA9C34ED78C7F60F2DA92EF207; arraycookie=wangban2"

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
        "imgCode": '',
        "plateTemp": "粤AQY910",
        "proxyIdType": "A"
    }

    # print('==========================================《第一步》==========================================')
    # # 1、发送表单申请
    # applay_base_info = sendFormApplyFunc(form_data)
    #
    # print('==========================================《第二步》==========================================')
    # # 2、发送短信的验证码
    # sendPhoneCodeFunc(phone)
    # # 3、提交短信验证码
    # verifyPhoneCode(form_data, phone)

    # ==========================================前两步可省略，直接在网页上操作==========================================

    print('==========================================《第三步》==========================================')
    # 4、获取可抢的日期（最后一天）
    day = getApplyDay()
    # 5、查询指定分所的信息
    office_info = getOfficeBaseinfo(officeName, day)
    # 6、检查可约时段, 并选中时段提交申请
    checkAndChoiseTimeInterval(office_info, day)

    print('==========================================《第四步》==========================================')
    # 7、最后一步提交，提交成功就预约成功了
    finalSubmitRequest()
    print('*********抢号成功*********')
