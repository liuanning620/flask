# -*- coding:utf-8 -*-
"""
@author: Alan
@file: qa.py
@time: 2023/4/2 0:11
@desc: 
"""
from flask import Blueprint

qa_blueprint = Blueprint("qa", __name__, url_prefix="/")


@qa_blueprint.route("/")
def index():
    pass