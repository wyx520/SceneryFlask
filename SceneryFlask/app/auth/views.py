# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from . import auth
from ..home.forms import RegistrationForm, LoginFrom
from .. import mongo
from flask.ext.login import login_required, login_user, current_user, logout_user


# 用户注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    loginforms = LoginFrom()
    if form.validate_on_submit():
        if mongo.db.users.find_one({"name": form.name.data}) is None and mongo.db.users.find_one(
                {"email": form.email.data}) is None:
            dir = {
                "name": form.name.data,
                "email": form.email.data,
                "password": form.password.data,
                "local": form.area.data
            }
            mongo.db.users.save(dir)
            flash(u"注册成功")
            return redirect(url_for('home.index'))
    return render_template('register.html', title=u"SceneryText",
                           form=form)


# 登陆
@auth.route('/login', methods=['GET', 'POST'])
def login():
    regforms = RegistrationForm()
    form = LoginFrom()
    if form.validate_on_submit():
        dir = {
            "name": form.name.data,
            "password": form.password.data
        }
        tmp = mongo.db.users.find_one({"name": dir["name"]})
        if tmp is not None and tmp["password"]==dir["password"]:
            flash(u"欢迎 ")
            flash(u"登陆成功")
            # 保存登陆地址和id
            return redirect(url_for('home.index'))
        else:
            flash(u"账号密码错误呢,亲。你在核对一下吧!")
            tipsuccess = 0
    return render_template('login.html', title=u"大周边",
                           form=form, )



