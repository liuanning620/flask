# -*- coding:utf-8 -*-
"""
@author: Alan
@file: config.py
@time: 2023/4/2 0:11
@desc: 
"""

# 配置数据库信息
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "landb"
USERNAME = "root"
PASSWORD = "123456"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME,PASSWORD, HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True