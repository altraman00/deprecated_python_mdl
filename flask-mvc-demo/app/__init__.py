#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:39
# @Author: xk
# @File  : __init__.py.py

# coding:utf8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config.db_config import DB_DATABASE, DB_PASSWORD, DB_URL, DB_USERNAME, DB_PORT

# 实例化flask
app = Flask(__name__)
app.debug = True
# 执行 python modules.py 会自动在mysql中创建表
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://%s:%s@%s/%s" % ('root', '123456', '127.0.0.1:3305', 'python-flask-movie')
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://%s:%s@%s:%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_URL, DB_PORT, DB_DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

# 引入home和admin的蓝图模块
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
# 访问地址需要加上/admin_pre前缀
# 如：http://127.0.0.1:5000/admin_pre/admin
app.register_blueprint(admin_blueprint, url_prefix="/admin_pre")


# 404页面
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template("home/404.html"), 404
