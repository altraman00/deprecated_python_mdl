#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:41
# @Author: xk
# @File  : forms.py

# coding:utf8

from app import db,app
from app.modules import Admin

class AdminService(object):
    """查询admin用户"""

    def queryAdmin(self, id):
        # 数据库链接方式一，使用db.session
        app.logger.debug('查询admin表')
        admin = db.session.query(Admin).filter_by(id=id).first()

        # 数据库连接方式二，使用model对象Admin直接进行查询操作
        # adminCount = Admin.query.filter_by(id=id).all()
        if admin is None:
            resStr = "暂时没有admin用户"
            # return resStr
            # print(resStr)
            app.logger.debug(resStr)

        # 创建新的admin对象
        # try ... except 是简单的事务捕捉，嵌套事务需要在try里面添加with session.begin_nested()
        # 事务的提交最后由外层的commit执行，with执行完毕，内层session自动托管到外层事务上
        try:
            admin = self.create_admin()

            print(type(admin))
            print("创建新用户", admin.name)
            # # # 先插入数据，然后等所有逻辑操作做完之后，再db.session.commit()，事务才会起效
            # a = 1 / 0

        except BaseException as e:
            print("创建异常，事务回滚", e)
            db.session.rollback()
            return '创建异常，事务已经回滚'

        # 提交事务
        db.session.commit()

        return admin.name

    # 插入数据
    def create_admin(self):
        from werkzeug.security import generate_password_hash
        admin = Admin(
            name="mtianyan16",
            pwd=generate_password_hash("123456"),
            is_super=0,
            role_id=2
        )
        db.session.add(admin)
        return admin
