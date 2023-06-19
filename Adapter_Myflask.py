# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/4/18 17:48'

from flask import Flask
from flask.templating import Environment

from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig

# ----- Adapter 适配器---------
class FlaskEchartsEnvironment(Environment):# 集成jinja2模板
    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.pyecharts_config = PyEchartsConfig(jshost='/static/js')  # 使用本地 echarts js文件
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)    #  添加模板函数到全局字典中。


# ---User Code ----
class MyFlask(Flask):# 继承Flask
    jinja_environment = FlaskEchartsEnvironment # 指定 Flask EchartsEnvironment 为默认模板引擎
