# -*- coding:utf-8 -*-
"""
@author: Alan
@file: models.py
@time: 2023/4/2 0:12
@desc: 
"""
from datetime import datetime

from exts import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False, unique=True)
    phone = db.Column(db.String(11), unique=True)
    age = db.Column(db.String(4))
    sex = db.Column(db.String(2))
    token = db.Column(db.String(30))
