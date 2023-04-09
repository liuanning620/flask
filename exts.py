# -*- coding:utf-8 -*-
"""
@author: Alan
@file: exts.py
@time: 2023/4/2 0:12
@desc: 为了解决循环引用的问题
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()