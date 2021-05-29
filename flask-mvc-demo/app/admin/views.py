#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:40
# @Author: xk
# @File  : views.py
from app.admin.forms import AdminService
from . import admin


@admin.route("/admin/<int:id>")
def index(id):
    adminService = AdminService()
    res = adminService.queryAdmin(id)
    print("res------>", res)
    return res
