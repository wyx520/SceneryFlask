# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from flask import current_app
from flask import render_template
from app import mail
from threading import Thread
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .. import mongo
from bson import ObjectId

def send_async_email(app, msg):
    with  app.app_context():
        mail.send(msg)

# 发送邮
def send_email(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASK_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr







