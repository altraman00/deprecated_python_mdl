#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:40
# @Author: xk
# @File  : __init__.py.py

# coding:utf8

from flask import Blueprint

home = Blueprint("home", __name__, template_folder='templetes')

import app.home.views
