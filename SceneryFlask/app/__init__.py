# -*- coding: utf-8 -*-
from flask_bootstrap import Bootstrap
from flask import Flask
from os import path
from config import config
from flask_login import LoginManager
from flask.ext.pymongo import PyMongo
from flask_wtf.csrf import CsrfProtect
from werkzeug.contrib.cache import SimpleCache


#实例化引用的类
# 页面样式
bootstrap = Bootstrap()
# 芒果数据库

# 缓存
# cache = Cache()
# 文本页面展示
# pagedown = PageDown()
# 邮箱
# mail = Mail()
# 全球化
# babel = Babel()
csrf = CsrfProtect()
mongo = PyMongo()
#session
# 缓存
cache = SimpleCache()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u"您未登录哦！"

basedir = path.abspath(path.dirname(__file__))

# 工厂模式
def create_app(config_name='default'):
    #设置flask初始化配置
    app = Flask(__name__)
    #读取配置文件
    app.config.from_object(config[config_name])
    #初始化
    bootstrap.init_app(app)
    # cache.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)
    # babel.init_app(app)
    # csrf.init_app(app)

    # 开启https
    # if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
    #     from flask.ext.sslify import SSLify
    #     sslify = SSLify(app, permanent=True)

    #导入蓝图
    from auth import auth as auth_blueprint
    # from .main import main as main_blueprint
    from home import home as home_blueprint
    #注册蓝图
    app.register_blueprint(home_blueprint, static_folder='static')
    app.register_blueprint(auth_blueprint,static_folder='static')
    # app.register_blueprint(main_blueprint, static_folder='static')


    return app