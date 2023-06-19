# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/4/19 10:39'

from flask import Blueprint

# 创建一个蓝图的对象，蓝图就是一个小模块的抽象的概念
app_comp = Blueprint("app_computer", __name__)  # 小范围 以当前模块为准

# 导入蓝图
from . import computer
