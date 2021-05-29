import random
from io import BytesIO, BufferedReader

import requests


def testValidCode():
    img_url = "http://cgs.gzjd.gov.cn/vbook/images/verifycode" + '?' + str(random.randrange(50000, 60000))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    r = requests.get(img_url, headers=headers, stream=True)

    # 将bytes结果转化为字节流
    bytes_stream = BytesIO(r.content)

    # <class '_io.BytesIO'>
    print(type(bytes_stream))

    # <class 'bytes'>
    print(type(bytes_stream.read()))

    file_like = BufferedReader(bytes_stream)

    # <class '_io.BufferedReader'>
    print(type(file_like))

    # <class 'bytes'>
    print(type(file_like.read()))


if __name__ == '__main__':
    testValidCode()
