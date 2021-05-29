#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:18
# @Author: xk url管理
# @File  : url_manager.py


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加批量的url
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    # 判断管理器中是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取管理器中最新的url
    def get_new_url(self):
        # pop() 获取最上层的url，并将该url移除
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
