#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:41
# @Author: xk
# @File  : forms.py

# coding:utf8
from app import app

a = [1, 2, 3]
try:
    print(a[1])
    app.logger.info('12345678')
except Exception as e:
    app.logger.error(e)
