# -*- coding:utf-8 -*-
"""
@author: Alan
@file: auth.py
@time: 2023/4/2 0:11
@desc: 
"""
from flask import Blueprint, request

from models import UserModel

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/login")
def login():
    pass
