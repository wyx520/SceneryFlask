# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    # 全球化注释中文
    BABEL_DEFAULT_LOCALE = 'zh'
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\x03d\xf4\x95J\x15\xa4B\xfb\xc0\xaf \xd1A[j$}\x18\x16a\xe7\xd0\xec'
    # 缓存
    CACHE_TYPE = 'simple'


@staticmethod
def init_app(app):
    pass

# 开发模式
class DevelopmentConfig(Config):
    # 开启调试报错
    DEBUG = True
    # 设置邮箱地址
    MAIL_SERVER = 'smtp.163.com'
    # 邮箱端口
    MAIL_PORT = 25
    # 邮箱起用安全链接
    MAIL_USE_TLS = True
    # 邮箱帐号
    MAIL_USERNAME = 'bianyouqing'
    # 邮箱密码
    MAIL_PASSWORD = 'yiuyjvvnhyhdrtqu'
    # 邮箱名
    ADMINS = 'bianyouqing@163.com'
    # 邮箱主题功能
    FLASK_MAIL_SUBJECT_PREFIX = u'激活账号'
    # 邮箱发送者
    FLASK_MAIL_SENDER = 'bianyouqing@163.com'
    # SSL_DISABLE =False

# 生产模式
class Production(Config):
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'bianyouqing'
    MAIL_PASSWORD = 'yiuyjvvnhyhdrtqu'
    ADMINS = 'bianyouqing@163.com'
    FLASK_MAIL_SUBJECT_PREFIX = u'激活账号'
    FLASK_MAIL_SENDER = 'bianyouqing@163.com'
    SSL_DISABLE = True

config = {
    'development': DevelopmentConfig,
    'production': Production
}