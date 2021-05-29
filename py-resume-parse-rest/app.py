import urllib
from _curses import error

from bs4 import BeautifulSoup
from flask import Flask, request, json

import html_parse

app = Flask(__name__)


# hello world接口
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'hello world!'


# 解析简历的接口
@app.route('/resume/parse', methods=['GET'])
def resume_parse():
    url = "https://baike.baidu.com/item/Python/407313"
    htmlParse = html_parse.HtmlParse()

    # 解析html成document
    soup = htmlParse.parse_baike(url)

    # 获取html中的数据
    res_data = htmlParse.get_html_data(url, soup)
    res_data_url = res_data['url']
    res_data_title = res_data['title']
    res_data_summary = res_data['summary']
    print('url:%s\ntitle:%s\nsummary:%s' % (res_data_url, res_data_title, res_data_summary))

    return res_data_summary


# 只接受get方法访问 入参在url后添加
# 请求方式 http://127.0.0.1:5000/test_1.0?name=张三&age=18
@app.route("/test_1.0", methods=["GET"])
def check1():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')
    # 对参数进行操作
    return_dict['result'] = tt(name, age)

    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def tt(name, age):
    result_str = "%s今年%s岁" % (name, age)
    return result_str


# 只接受POST方法访问
# 入参在postman中采用 Body -> raw -> JSON(application/json)
@app.route("/test_1.1", methods=["POST"])
def check2():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断传入的json数据是否为空
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_data = json.loads(get_data)
    name = get_data.get('name')
    age = get_data.get('age')
    # 对参数进行操作
    return_dict['result'] = tt(name, age)

    return json.dumps(return_dict, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
