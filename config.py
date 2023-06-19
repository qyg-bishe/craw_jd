# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/4/18 17:30'

import logging


class MyConfig(object):
    # 默认日志等级
    DEBUG = False
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@127.0.0.1:3306/shang_hai?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #    SQLALCHEMY_COMMIT_TEARDOWN = True

class ProductionConfig(MyConfig):
    DEBUG = False
    LOG_LEVEL = logging.ERROR
    pass

class DevelopmentConfig(MyConfig):
    DEBUG = True
    pass


config_map = {
    'product':ProductionConfig,
    'develop':DevelopmentConfig
}