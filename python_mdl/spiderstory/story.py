import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

path = '/Users/knight/workspace/python/day01/spiderstory/xxx.txt'

if not os.path.exists(path):
    os.mkdir(path)

url = 'https://www.xbiquge.cc/book/14719/'

response = requests.get(url=url, headers=headers)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

novel_lists = soup.select("#list dd a")

novel_list = novel_lists[12:]

print(novel_list)

for i in range(len(novel_list)):
    novel_name = novel_list[i].text
    novel_url = url + novel_list[i].get("href")

    novel_response = requests.get(url=novel_url, headers=headers)
    novel_html = novel_response.text
    novel_soup = BeautifulSoup(novel_html, "html.parser")
    novel_content = novel_soup.find('div', id="content").text

    file = open(path, 'a', encoding='utf-8')
    file.write(novel_name)
    file.write(novel_content)
    print(novel_name + '下载完成')
    file.close()

print('全部下载完成')
