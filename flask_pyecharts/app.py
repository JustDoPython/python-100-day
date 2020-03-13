from flask import Flask, render_template
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates/pyecharts"))

from pyecharts import options as opts
from pyecharts.charts import Bar, WordCloud, Line


app = Flask(__name__)


def bar_base() -> Bar:  # -> 表示要返回的是类型
    c = (
        Bar()
        .add_js_funcs("""
        alert("Hahaha")
        """)
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
        .add_yaxis("商家C", [33, 23, 12, 53, 23, 10])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Bar-基本示例", 
                title_link='https://baidu.com', 
                subtitle="我是副标题",
                pos_left= "center",
                pos_top="top"),
            legend_opts=opts.LegendOpts(
                pos_top="60"
            ))
    )
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        # .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

# 词云
def wordcloud_base() -> WordCloud:
    w = (
        WordCloud()
        .add('',[('python', 23),('word',10),('cloud',5),
        ('java', 23),('C',10),('C++',5),('设计模式',20),('重构',12),('架构','20')], shape='circle')
    )
    return w
# 模板渲染
@app.route("/")
def index():
    c = bar_base()
    return Markup(c.render_embed())

@app.route("/wordcloud")
def wordcloud():
    wordcloud = wordcloud_base()
    return Markup(wordcloud.render_embed())

# 前后分离
@app.route("/bar")
def bar():
    return render_template("index.html")

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

# 定时增量更新
from random import randrange
from flask.json import jsonify

def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

@app.route("/line")
def line():
    return render_template("index2.html")

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

idx = 9

@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})

if __name__ == "__main__":
    print("ok")
    app.run()