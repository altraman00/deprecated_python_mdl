#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:19
# @Author: xk 解析html文件
# @File  : html_parser.py
import re

from urllib.parse import urljoin

from bs4 import BeautifulSoup

from html_downloader import HtmlDownloader


class HtmlParser(object):

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/*"))
        for link in links:
            new_url = link['href']
            # print('page_url: %s,new_url:s%', page_url, new_url)
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取百科词条的 名字 和 简介
    def get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # 标题
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text

        # 简介
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text

        return res_data

    # 解析文件
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)

        return new_urls, new_data

# if __name__ == '__main__':
#     url = "https://baike.baidu.com/item/Python/407313"
#
#     htmlDownloader = HtmlDownloader()
#     html = htmlDownloader.download(url)
#     htmlParser = HtmlParser()
#     result = htmlParser.parser(html, 123)
#     print(result[0], '\n')
#     print(result[1], '\n')
