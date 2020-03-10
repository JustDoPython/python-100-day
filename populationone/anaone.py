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
pdata = pd.read_excel('populationone.xlsx')


# 分析总人口
def analysis_total():
    # 处理数据
    x_data = pdata['年份'].tolist()
    # 将人口单位转换为亿
    y_data1 = pdata['年末总人口(万人)'].map(lambda x: "%.2f" % (x / 10000)).tolist()
    y_data2 = pdata['人口自然增长率(‰)'].tolist()
    y_data3 = pdata['人口出生率(‰)'].tolist()
    y_data4 = pdata['人口死亡率(‰)'].tolist()

    # 总人口柱状图
    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="500px"))
    bar.add_xaxis(x_data)
    bar.add_yaxis("年末总人口（亿）", y_data1, category_gap="10%", label_opts=opts.LabelOpts(rotate=90, position="inside"))
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="年末总人口变化情况", pos_bottom="bottom", pos_left="center"),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            name='年份',
            # 坐标轴名称显示位置
            name_location='end',
            # x轴数值与坐标点的偏移量
            # boundary_gap=False,
            axislabel_opts=opts.LabelOpts(is_show=True, margin=10, color="#000", interval=1, rotate=90),
            # axisline_opts=opts.AxisLineOpts(is_show=True, symbol="arrow"),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="line", label=opts.LabelOpts(is_show=True))
        ),
        # y轴相关选项设置
        yaxis_opts=opts.AxisOpts(
            type_="value",
            position="left",
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )

    # bar.render('bartest.html')

    # 自然增长率、出生率、死亡率折线图
    line = Line(init_opts=opts.InitOpts(width="1400px", height="500px"))
    line.add_xaxis(x_data)
    line.add_yaxis(
        series_name="自然增长率(‰)",
        y_axis=y_data2,
        label_opts=opts.LabelOpts(
            is_show=False
        )
    )
    line.add_yaxis('出生率(‰)', y_data3, label_opts=opts.LabelOpts(is_show=False))
    line.add_yaxis('死亡率(‰)', y_data4, label_opts=opts.LabelOpts(is_show=False))
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="人口自然增长率、出生率、死亡率", pos_bottom="bottom", pos_left="center"),
        xaxis_opts=opts.AxisOpts(
            name='年份',
            name_location='end',
            type_="value",
            min_="1949",
            max_interval=1,
            # 设置x轴不必与y轴的0对齐
            axisline_opts=opts.AxisLineOpts(is_on_zero=False),
            axislabel_opts=opts.LabelOpts(is_show=True, color="#000", interval=0, rotate=90),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="shadow", label=opts.LabelOpts(is_show=True))
        ),
        # y轴相关选项设置
        yaxis_opts=opts.AxisOpts(
            name='比例',
            type_="value",
            position="left",
            min_=-10,
            axislabel_opts=opts.LabelOpts(is_show=True)
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )

    # 渲染图像，将多个图像显示在一个html中
    # DraggablePageLayout表示可拖拽
    page = Page(layout=Page.DraggablePageLayout)
    page.add(bar)
    page.add(line)
    page.render('population_total.html')

# 分析男女比
def analysis_sex():
    x_data = pdata['年份'].tolist()
    # 历年男性人口数
    y_data_man = pdata['男性人口(万人)']
    # 历年女性人口数
    y_data_woman = pdata['女性人口(万人)']
    # 2019年男女比饼图
    sex_2019 = pdata[pdata['年份'] == 2019][['男性人口(万人)', '女性人口(万人)']]

    # 两列相减，获得新列
    y_data_man_woman = pdata['男性人口(万人)'] - pdata['女性人口(万人)']

    pie = Pie()
    pie.add("", [list(z) for z in zip(['男', '女'], np.ravel(sex_2019.values))])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="2019中国男女比", pos_bottom="bottom", pos_left="center"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    pie.render('nvpie.html')

    line = Line(init_opts=opts.InitOpts(width="1400px", height="500px"))
    line.add_xaxis(x_data)
    line.add_yaxis(
        series_name="男女差值",
        y_axis=y_data_man_woman.values,
        # 标出关键点的数据
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="min"),
                opts.MarkPointItem(type_="max"),
                opts.MarkPointItem(type_="average")
            ]
        ),
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
    )
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="中国70年(1949-2019)男女差值（万人）", pos_left="center", pos_top="bottom"),
        legend_opts=opts.LegendOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(
            name='年份',
            name_location='end',
            type_="value",
            min_="1949",
            max_interval=1,
            # 设置x轴不必与y轴的0对齐
            axisline_opts=opts.AxisLineOpts(is_on_zero=False),
            axislabel_opts=opts.LabelOpts(is_show=True, color="#000", interval=0, rotate=90),
            axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
            axispointer_opts=opts.AxisPointerOpts(type_="shadow", label=opts.LabelOpts(is_show=True))
        ),
        yaxis_opts=opts.AxisOpts(
            name='差值（万人）',
            type_="value",
            position="left",
            axislabel_opts=opts.LabelOpts(is_show=True)
        ),
    )

    # 5、渲染图像，将多个图像显示在一个html中
    page = Page(layout=Page.DraggablePageLayout)
    page.add(pie)
    page.add(line)
    page.render('population_sex.html')


if __name__ == '__main__':
    analysis_total()
    analysis_sex()