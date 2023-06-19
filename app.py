# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

__author__ = 'qyg'
__date__ = '2019/4/18 16:45'

from flask import render_template, current_app
from create_app import create_app

app = create_app('develop')


@app.route('/')
def index():
    current_app.logger.warn('warn msg')
    return render_template('index.html')
    # 返回app,在manage当中可以调用


if __name__ == '__main__':
    app.run()
