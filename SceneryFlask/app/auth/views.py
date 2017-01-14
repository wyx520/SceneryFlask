# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from . import auth
from ..home.forms import RegistrationForm, LoginFrom
from .. import mongo
from ..models.user import user
from flask.ext.login import login_required, login_user, current_user, logout_user


# 用户注册
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if mongo.db.users.find_one({"name": form.name.data}) is None:
            myuser = user()
            myuser.name=form.name.data
            myuser.password =user.getHashCode(form.password.data)
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
        myuser = user()
        tmp = mongo.db.users.find_one({"name": dir["name"]})
        isSuccess = myuser.loginOn(dir)
        if isSuccess is not None:
            myuser.dirModel = isSuccess
            myuser.id = isSuccess["_id"]
            login_user(myuser, form.remeber_me.data)
            flash(u"欢迎 ")
            flash(u"登陆成功")
            # 保存登陆地址和id
            return redirect(url_for('home.index'))
        else:
            flash(u"账号密码错误�亲。你在核对一下吧!")
    return render_template('login.html', title=u"大周�,
                           form=form, )

# 请求前验�
@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and request.endpoint[:5] != 'home.'\
            and request.endpoint != 'static':
        return redirect(url_for('auth.login'))



