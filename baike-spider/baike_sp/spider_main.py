#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:18
# @Author: xk 入口函数
# @File  : spider_main.py

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):

    # 每个模块中已经创建好了需要用的class 以及 在构造函数中初始化好了所需要的对象
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫的调度程序
    def crow(self, root_url):
        count = 1
        # 设置需要爬取的url
        self.urls.add_new_url(root_url)

        # 如果有需要爬取的url，则循环爬取，直到结束
        while self.urls.has_new_url():
            # 获取最新的url
            new_url = self.urls.get_new_url()

            # 下载页面
            html_cont = self.downloader.download(new_url)
            # 解析页面html，获取新的url和数据
            new_urls, new_data = self.parser.parser(new_url, html_cont)

            print("craw:%d, :%s" % (count, new_url))

            self.urls.add_new_urls(new_urls)
            # 收集数据
            self.outputer.collect_date(new_data)

            if count == 3:
                break

            count = count + 1

        # 打印爬取到的数据到html文件中
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    # 创建主函数类
    obj_spider = SpiderMain()
    # 创建启动爬虫的入口函数
    obj_spider.crow(root_url)
