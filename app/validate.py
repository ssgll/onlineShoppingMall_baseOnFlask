# -*- coding: utf-8 -*-
from app.models import db, user
from werkzeug.security import check_password_hash


# 注册校验
class registerValidate(object):
    def __init__(self, username, password, password2):
        self.username = username
        self.password = password
        self.password2 = password2

    # 用户名查找
    def exists_username(self):
        exists_user = None
        try:
            exists_user = db.session.query(user).filter_by(username=self.username).one()
        except BaseException as e:
            pass
        if exists_user:
            return "用户名已存在"
        else:
            return None

    # 密码合法性校验
    def passwordValidate(self):
        if self.password2 != self.password:
            return "密码不一致"
        if len(self.password) < 6:
            return "密码长度不符合规范"
        else:
            return None

    # 返回数据
    def results(self):
        error = None
        for errors in [self.exists_username(), self.passwordValidate()]:
            if errors is not None:
                error = errors
                break
        if not error:
            db.session.query(user)
        return error


# 登录校验
class loginValidator(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 用户名查找
    def usernameSearch(self):
        try:
            rel_username = db.session.query(user).filter(user.username == self.username).one().username
        except:
            return '未找到用户名'

        if rel_username is not None:
            return None
        else:
            return '未找到用户名'

    # 密码验证
    def passwordValidator(self):
        try:
            rel_password_hash = db.session.query(user).filter(user.username == self.username).one().password_hash
        except:
            return '密码错误'

        if check_password_hash(rel_password_hash, self.password):
            return None
        else:
            return '密码错误'

    # 校验结果传出
    def checkoutReturn(self):
        error = None
        for errors in [self.usernameSearch(), self.passwordValidator()]:
            if errors is not None:
                error = errors
                break
        return error
