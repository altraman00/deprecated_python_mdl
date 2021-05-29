#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:18
# @Author: xk
# @File  : html_downloader.py
import urllib.request
from _curses import error


class HtmlDownloader(object):

    # 下载html
    def download(self, url):
        if url is None:
            return

        try:
            print('download_url:s%', url)
            response = urllib.request.urlopen(url, timeout=10)
            code = response.getcode()

            if code != 200:
                print('success')
                return None
        except error.URLError as e:
            print(e.reason)

        return response.read()

# if __name__ == '__main__':
#     print("入口")
#     url = "https://baike.baidu.com/item/Python/407313"
#     dw = HtmlDownloader()
#     content = dw.download(url)
#     print('打印：', content, '\n')  # 打印
