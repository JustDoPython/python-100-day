#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""
import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Page, Pie


# 读取数据
pdata = pd.read_excel('populationtwo.xlsx')


# 分析人口结构
def analysis_struct():
    # 处理数据
    x_data = pdata['年份'].map(lambda x: "%d" % x).tolist()
    y_data1 = pdata['0-14岁人口(万人)'].map(lambda x: "%.2f" % x).tolist()
    y_data2 = pdata['15-64岁人口(万人)'].map(lambda x: "%.2f" % x).tolist()
    y_data3 = pdata['65岁及以上人口(万人)'].map(lambda x: "%.2f" % x).tolist()

    # 人口结构折线图
    line = Line()
    line.add_xaxis(x_data)
    line.add_yaxis('0-14岁人口', y_data1, label_opts=opts.LabelOpts(is_show=False))
    line.add_yaxis('15-64岁人口', y_data2, label_opts=opts.LabelOpts(is_show=False))
    line.add_yaxis('65岁及以上人口', y_data3, label_opts=opts.LabelOpts(is_show=False))
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="人口结构", pos_bottom="bottom", pos_left="center"),
        xaxis_opts=opts.AxisOpts(
            name='年份',
            name_location='end',
            type_="category",
            # axislabel_opts=opts.LabelOpts(is_show=True, color="#000", interval=0, rotate=90),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="shadow", label=opts.LabelOpts(is_show=True))
        ),
        # y轴相关选项设置
        yaxis_opts=opts.AxisOpts(
            name='人口数（万人）',
            type_="value",
            position="left",
            axislabel_opts=opts.LabelOpts(is_show=True)
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )

    # 渲染图像，将多个图像显示在一个html中
    # DraggablePageLayout表示可拖拽
    page = Page(layout=Page.DraggablePageLayout)
    page.add(line)
    page.render('population_struct.html')

# 分析抚养比例
def analysis_raise():
    # 处理数据
    x_data = pdata['年份'].map(lambda x: "%d" % x).tolist()
    y_data1 = pdata['总抚养比(%)'].map(lambda x: "%.2f" % x).tolist()
    y_data2 = pdata['少儿抚养比(%)'].map(lambda x: "%.2f" % x).tolist()
    y_data3 = pdata['老年抚养比(%)'].map(lambda x: "%.2f" % x).tolist()

    line = Line()
    line.add_xaxis(x_data)
    line.add_yaxis('总抚养比(%)', y_data1, label_opts=opts.LabelOpts(is_show=False))
    line.add_yaxis('少儿抚养比(%)', y_data2, label_opts=opts.LabelOpts(is_show=False))
    line.add_yaxis('老年抚养比(%)', y_data3, label_opts=opts.LabelOpts(is_show=False))
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="人口抚养比例", pos_bottom="bottom", pos_left="center"),
        xaxis_opts=opts.AxisOpts(
            name='年份',
            name_location='end',
            type_="category",
            # axislabel_opts=opts.LabelOpts(is_show=True, color="#000", interval=0, rotate=90),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="shadow", label=opts.LabelOpts(is_show=True))
        ),
        # y轴相关选项设置
        yaxis_opts=opts.AxisOpts(
            name='抚养比例(%)',
            type_="value",
            position="left",
            axislabel_opts=opts.LabelOpts(is_show=True)
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )

    # 渲染图像，将多个图像显示在一个html中
    # DraggablePageLayout表示可拖拽
    page = Page(layout=Page.DraggablePageLayout)
    page.add(line)
    page.render('population_raise.html')


# 分析城镇化比例
def analysis_urban():
    x_data = pdata['年份'].map(lambda x: "%d" % x).tolist()
    # total = pdata['年末总人口(万人)'].map(lambda x: "%.2f" % (x / 1000)).tolist()
    y_data1 = pdata['城镇人口(万人)'].map(lambda x: "%.2f" % (x / 1000)).tolist()
    y_data2 = pdata['乡村人口(万人)'].map(lambda x: "%.2f" % (x / 1000)).tolist()

    # 城镇化比例
    # y_data_rate = pdata['城镇人口(万人)'] * 100 / pdata['年末总人口(万人)']

    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("城镇人口", y_data1, stack="stack1", category_gap="10%")
    bar.add_yaxis("乡村人口", y_data2, stack="stack1", category_gap="10%")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", rotate=90))
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="中国城镇化进程"),
        xaxis_opts=opts.AxisOpts(
            name='年份',
            name_location='end',
            type_="category",
            # axislabel_opts=opts.LabelOpts(is_show=True, color="#000", interval=0, rotate=90),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="shadow", label=opts.LabelOpts(is_show=True))
        ),
        # y轴相关选项设置
        yaxis_opts=opts.AxisOpts(
            name='人口数(千万人)',
            type_="value",
            position="left",
            axislabel_opts=opts.LabelOpts(is_show=True)
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )


    # 渲染图像，将多个图像显示在一个html中
    page = Page(layout=Page.DraggablePageLayout)
    page.add(bar)
    page.render('population_urban.html')


if __name__ == '__main__':
    # analysis_struct()
    # analysis_raise()
    analysis_urban()