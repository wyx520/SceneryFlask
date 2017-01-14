# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from . import home
from .forms import RegistrationForm, LoginFrom
from .. import mongo
from flask.ext.login import login_required, login_user, current_user, logout_user
from flask import json


@home.route('/',  methods=['GET', 'POST'])
def index():
    loginforms = LoginFrom()
    regforms = RegistrationForm()
    return render_template('index.html',title = u"大周边")

@home.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html',404)




# 账号激活


# 重新发邮件


