from flask import Flask,render_template
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Pie,Line

# from jinja2 import Markup

app = Flask(__name__)

from pymysql import connect


def bar_base():
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()

    csl.execute("SELECT `name` as 书名,`read` as 阅读 FROM fiction1 LIMIT 10;")

    data = csl.fetchall()
    dd1 = []
    dd2 = []
    for data1, data2 in data:
        dd1.append(data1)
        dd2.append(data2)

    line = (
        Line()
            .add_xaxis(xaxis_data=dd1)
            .add_yaxis(
            series_name="阅读量",
            y_axis=dd2,
            is_connect_nones=True
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="阅读量"),xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":-45}))
    )
    conn.close()
    csl.close()
    return line

def bar_base1():
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()

    csl.execute("SELECT DISTINCT `name` as 书名,`score` as 人气值 FROM fiction1 ORDER BY `score` desc LIMIT 15; ")

    data = csl.fetchall()
    dd1 = []
    dd2 = []
    for data1, data2 in data:
        dd1.append(data1)
        dd2.append(data2)

    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(dd1)
            .add_yaxis("人气值", dd2)
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":-45}))
    )
    conn.close()
    csl.close()
    return bar

def bar_base2():
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()

    csl.execute("SELECT serialize as 分类,moods as 评分 FROM	fiction1 GROUP BY serialize;")

    data = csl.fetchall()
    dd1 = []
    dd2 = []
    for data1, data2 in data:
        dd1.append(data1)
        dd2.append(data2)

    pie = (
        Pie(init_opts=opts.InitOpts(width='720px', height='320px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(dd1, dd2)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    conn.close()
    csl.close()
    return pie

def bar_base3():
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()

    csl.execute("SELECT DISTINCT classify as 连载状态,COUNT(*) as 次数 FROM fiction1 GROUP BY classify ;")

    data = csl.fetchall()
    dd1 = []
    dd2 = []
    for data1, data2 in data:
        dd1.append(data1)
        dd2.append(data2)

    pie = (
        Pie(init_opts=opts.InitOpts(width='720px', height='320px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(dd1, dd2)],color='#FF00FF')
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    conn.close()
    csl.close()
    return pie

def bar_base4():
    conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
    csl = conn.cursor()

    csl.execute("SELECT `name`,score,`read` FROM fiction1 LIMIT 10;")

    data = csl.fetchall()
    dd1 = []
    dd2 = []
    dd3 = []
    for data1, data2, data3 in data:
        dd1.append(data1)
        dd2.append(data2)
        dd3.append(data3)

    line = (
        Line()
            .add_xaxis(xaxis_data=dd1)
            .add_yaxis(series_name="人气", y_axis=dd2, symbol="arrow", is_symbol_show=True,color='#000')
            .add_yaxis(series_name="阅读量", y_axis=dd3,color='red')
            .set_global_opts(title_opts=opts.TitleOpts(title="阅读"),xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":-45}))
    )
    conn.close()
    csl.close()
    return line


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/barChart")
def get_bar_chart():
    c1 = bar_base1()
    return c1.dump_options_with_quotes()

@app.route("/barChart1")
def get_bar_chart1():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/barChart2")
def get_bar_chart2():
    c2 = bar_base2()
    return c2.dump_options_with_quotes()

@app.route("/barChart3")
def get_bar_chart3():
    c2 = bar_base3()
    return c2.dump_options_with_quotes()

@app.route("/barChart4")
def get_bar_chart4():
    c3 = bar_base4()
    return c3.dump_options_with_quotes()


if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True)
