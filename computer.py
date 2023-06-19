# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/4/18 16:32'


from flask import Blueprint,render_template
from models import Computer_Cpu,Computer_Price,Computer_Brand
from pyecharts import Pie, Line, Bar
# 创建一个蓝图的对象，蓝图就是一个小模块的抽象的概念
app_comp = Blueprint("app_computer",__name__)# 小范围 以当前模块为准

@app_comp.route("/brand/")
def computer_brand():
    '''笔记本销量 牌子 '''
    data_list=Computer_Brand.query.all()
    brands=[]
    count=[]
    for item in data_list:
        brands.append(item.brand)
        count.append(item.count)
    pie = Pie('笔记本-销量/牌子Info',title_pos='center',width=1000)
    pie.add('',brands,count,center=[25,50],is_random=True,radius=[30,65],rosetype='area',is_legend_show=False,
            is_label_show=True)
    # Computer_Count.query.all().order_by
    pie.add('',brands,count,center=[80,50],is_random=True,radius=[30,65],rosetype='radius',is_legend_show=False)
    return render_template('Com_brand.html', hm=pie)

@app_comp.route("/cpu/")
def Compu_cpu():
    '''笔记本销量 CPU版本关系'''
    cpus = []
    count = []
    data_list = Computer_Cpu.query.all()
    for item in data_list:
        # print(item.cpu_version)
        cpus.append(item.cpu_version)
        count.append(item.count)
    bar = Bar("笔记本销量-CPU关系柱状图图")
    # bar.use_theme('dark')
    bar.add("cpu型号", cpus, count, mark_point=["min", "average", "max", ])
    return render_template('Com_cpu.html',hm=bar)


@app_comp.route("/price/")
def Compu_Price():
    '''笔记本 价格'''
    prices = []
    count = []
    data_list = Computer_Price.query.all()
    for item in data_list:
        prices.append(item.price)
        count.append(item.count)
    line = Line("笔记本-价格需求分析折线图")
    line.add("哈哈", prices, count, mark_point=["average"])
    return render_template('Com_price.html', hm=line)
