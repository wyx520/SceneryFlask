# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length
from wtforms.fields.html5 import URLField
from wtforms.validators import url


# 注册
class RegistrationForm(Form):
    email = StringField(u'邮箱地址', validators=[DataRequired(),
                                                Length(1, 64),
                                                Email(),
                                                Regexp('^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', 0,
                                                       u'邮箱格式不正确,请检查之后注册')]
                        )
    emailplaceholder = u"邮箱地址"
    name = StringField(u'用户名', validators=[DataRequired(),
                                              Length(1, 64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                     u'用户名必须由字母数、字数、下划线或 . 组成')])
    nameplaceholder = u"用户名"
    area = SelectField(u'地区',
                       choices=[('zh_CN', u'中国大陆'), ('zh_TW', u'中华台湾'), ('US', u'美国'), ('JP', u'日本')],
                       validators=[DataRequired()]
                       )
    areaplaceholder = u"选择地区哦"
    password = PasswordField(u'密码', validators=[DataRequired()])
    # passwordplaceholder = u"密码"
    password2 = PasswordField(u'确认密码', validators=[DataRequired(),
                                                      EqualTo('password', message=u'密码必须一至')])
    password2placeholder = u"确认密码"

    submit = SubmitField(u'马上注册')

    # 登陆


class LoginFrom(Form):
    name = StringField(u'用户名', validators=[DataRequired(),
                                              Length(1, 64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                     u'用户名必须由字母数、字数、下划线或 . 组成')])
    nameplaceholder = u"键入账号"
    password = PasswordField(u'密码', validators=[DataRequired()
                                                  ])
    passwordplaceholder=u"键入密码"

    remeber_me = BooleanField(u'记住密码')
    remeber_meplaceholder=u"记住密码"
    submit = SubmitField(u'登录')
