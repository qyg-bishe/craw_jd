# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/3/29 15:47'

# from exts import db
from create_app import db


class Computer_Brand(db.Model):
    __tablename__ = 'computer_brand'
    '''可视化model字段'''
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255))
    count = db.Column(db.Integer)


class Computer_Cpu(db.Model):
    __tablename__ = 'computer_cpu'
    '''可视化model字段'''
    id = db.Column(db.Integer, primary_key=True)
    cpu_version = db.Column(db.String(255))
    count = db.Column(db.Integer)


class Computer_Price(db.Model):
    __tablename__ = 'computer_price'
    '''可视化model字段'''
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(255))
    count = db.Column(db.Integer)
