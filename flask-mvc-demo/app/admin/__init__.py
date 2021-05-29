#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/11 18:40
#@Author: xk
#@File  : __init__.py.py

#coding:utf8

from flask import Blueprint

admin = Blueprint("admin",__name__)

import app.admin.views