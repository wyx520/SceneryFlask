# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length
from wtforms.fields.html5 import URLField
from wtforms.validators import url



