#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 21:20
# @Author: xk
# @File  : html_parse.py
import urllib.request as ur
from _curses import error

from bs4 import BeautifulSoup


class HtmlParse(object):

    # 解析html
    def parse_baike(self, url):
        try:
            response = ur.urlopen(url, timeout=10)
            code = response.getcode()

            if code != 200:
                print('success')
                return None
        except error.URLError as e:
            print('下载异常url:s%', url)
            print(e.reason)

        htmlStr = response.read()
        soup = BeautifulSoup(htmlStr, 'html.parser', from_encoding='utf-8')
        return soup

    # 获取百科词条的 名字 和 简介
    def get_html_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # 标题
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text().strip()

        # 简介
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text().strip()

        return res_data


# if __name__ == '__main__':
#     htmlParse = HtmlParse()
#
#     url = "https://baike.baidu.com/item/Python/407313"
#
#     # 解析html成document
#     soup = htmlParse.parse_baike(url)
#
#     # 获取html中的数据
#     res_data = htmlParse.get_html_data(url, soup)
#
#     res_data_url = res_data['url']
#     res_data_title = res_data['title']
#     res_data_summary = res_data['summary']
#     print('url:%s\ntitle:%s\nsummary:%s' % (res_data_url, res_data_title, res_data_summary))
