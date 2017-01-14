# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from . import home
from .forms import RegistrationForm, LoginFrom
from .. import mongo
from flask.ext.login import login_required, login_user, current_user, logout_user
from flask import json
from ..models.emails import send_email




@home.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html',404)

@home.route('/',  methods=['GET', 'POST'])
def index():
    flash(current_user.name)
    return render_template('index.html',title = u"大周边")

# 注销登陆
@home.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'已经注销')
    return redirect(url_for('home.index'))

# 注销登陆
@home.route('/sendemail')
@login_required
def sendemail():
    emails=request.form.get('emmails')
    send_email("382035562@qq.com", u'表单回收',
               'email/confirm', user=current_user)
    flash("发送成功")
    return redirect(url_for('home.index'))




