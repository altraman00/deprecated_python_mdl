from baidu_ocr.aip import AipOcr


def baiduOCR(picfile):  # picfile:图片文件名
    # 百度提供
    """ 你的 APPID AK SK """
    APP_ID = '24169716'  # 这是你产品服务的appid
    API_KEY = 'WLHsk7NvwFAP8Dj9WMoCwSFU'  # 这是你产品服务的appkey
    SECRET_KEY = 'Mi4VZGipmYjU6X4LYMgKSBtYViIOFzAE'  # 这是你产品服务的secretkey
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片
    img = get_file_content(picfile)
    """ 调用通用文字识别（高精度版） """
    message = client.basicAccurate(img)

    print('通用文字识别中 》》》')
    printMsg(message)

    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别（高精度版） """
    message = client.basicAccurate(img, options)

    print('高精度文字识别中 》》》')

    printMsg(message)


"""打印读取结果"""


def printMsg(message):
    # 输出文本内容
    result = message.get('words_result')
    if len(result) is 0:
        print('******识别结果为空******')
    else:
        for text in message.get('words_result'):  # 识别的内容
            print('识别结果：' + text.get('words'))


""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    # url = 'http://cgs.gzjd.gov.cn/vbook/images/verifycode?0.49847842484352545'
    imgPath = '/Users/knight/Desktop/mobvoi/valid_code/verifycode01.png'

    baiduOCR(imgPath)
