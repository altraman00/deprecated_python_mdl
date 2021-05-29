#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 15:18
# @Author: xk 打印爬取下来的百科内容
# @File  : html_outputer.py
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_date(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出到html中
    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</body>")
        fout.write("</table>")
        fout.write("</html>")

