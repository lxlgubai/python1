import pyecharts.options as opts
from pyecharts.charts import Line

from linkd import selectdata

mysql = "SELECT title,baidu_backlink,google_backlink,qihoo_backlink,backlink FROM chinaz LIMIT 10;"

data = selectdata(mysql)
# print(data)
x_data = []
b_data = []  # 百度反链数
g_data = []
q_data = []
s_data = []
for i in data:
    x_data.append(i[0])
    b_data.append(i[1])
    g_data.append(i[2])
    q_data.append(i[3])
    s_data.append(i[4])


(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="百度反链数",
        stack="总量",
        y_axis=b_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="谷歌反链数",
        stack="总量",
        y_axis=g_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="360反链数",
        stack="总量",
        y_axis=q_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="搜狗反链数",
        stack="总量",
        y_axis=s_data,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="反链数折线图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("反链数折线图.html")
)
