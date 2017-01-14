# -*- coding: utf-8 -*-
import time
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app, request
from .. import login_manager, mongo
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


class user(UserMixin):
    # id
    id = ObjectId()
    # 用户名
    name = ""
    # 密码
    password = ""
    # 我的问卷
    questionnaire = []
    # 实体json
    dirModel = {}

    def addmodel(self):
        dir = {
            "name" : self.name,
            "password":self.getHashCode(self.password),
            "questionnaire":[]
        }
        mongo.db.users.save(dir)

    # 获得哈希code
    @staticmethod
    def getHashCode(password):
        return generate_password_hash(password)

        # 登陆验证

    def loginOn(self, dir):
        tmp = mongo.db.users.find_one({"name": dir["name"]})
        if tmp is not None and check_password_hash(tmp["password"], dir["password"]):
            return tmp
        else:
            return None

@login_manager.user_loader
def load_user(user_id):
    mgdb = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    myuser = user()
    myuser.dirModel = mgdb
    return myuser

