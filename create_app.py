# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/4/2 13:50'

import logging
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config_map
from Adapter_Myflask import MyFlask

# 方法二,分步骤
db = SQLAlchemy()


def create_app(object_name):
    '''

    :param object_name:
    :return: app
    '''
    # 配置项目日志
    app = MyFlask(__name__)
    app.config.from_object(config_map[object_name])
    # 数据库的初始化
    db.init_app(app)
    # 开启csrf保护
    CSRFProtect(app)

    from computer import app_comp
    # 注册蓝图  应用对象从蓝图对象的deferer_functions 列表取出每一项，既调用应用对象的add_url_rule()方法。修改路由的映射列表
    app.register_blueprint(app_comp, url_prefix='/computer')
    return app


def setup_log(config_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config_map[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
