from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
from linkd import selectdata

mysql = "SELECT title,baidu_index,google_index,qihoo_index,sogou_index FROM chinaz ORDER BY baidu_index" \
        " + google_index + qihoo_index + sogou_index DESC LIMIT 10;"

data = selectdata(mysql)

title = []
lista = []
listfa = []
listgs = []
listhd = []
for i in data:
    titles = i[0]  # 标题
    lists = i[1]  # 百度收录
    listf = i[2]  # 谷歌收录
    listg = i[3]  # 360收录
    listh = i[4]  # 搜狗收录
    title.append(titles)
    lista.append(lists)
    listfa.append(listf)
    listgs.append(listg)
    listhd.append(listh)

# print(lista)

colors = ["#5793f3", "#d14a61", "#FF1493", "#cccccc"]

bar = (
    Bar(init_opts=opts.InitOpts(width="1460px", height="720px"))
    .add_xaxis(xaxis_data=title)
    .add_yaxis(
        series_name="谷歌收录", y_axis=listfa, yaxis_index=0, color=colors[3]
    )
    .add_yaxis(
        series_name="百度收录", y_axis=lista, yaxis_index=1, color=colors[2]
    )
    .add_yaxis(
        series_name="搜狗收录", y_axis=listhd, yaxis_index=3, color=colors[0]
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="谷歌收录",
            type_="value",
            min_=0,
            max_=15000,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color=colors[0])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
        )
    )

    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="百度收录",
            min_=0,
            max_=15000,
            position="left",
            # offset=10,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color=colors[2])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="360收录",
            min_=0,
            max_=15000,
            position="right",
            offset=70,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color=colors[2])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="搜狗收录",
            type_="value",
            min_=0,
            max_=555000,
            position="right",
            offset=130,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color=colors[3])
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
        )
    )
)

line = (
    Line()
    .add_xaxis(xaxis_data=title)
    .add_yaxis(
        series_name="360收录", y_axis=listgs, yaxis_index=2, color=colors[2]
    )
)

bar.overlap(line).render("平台收录.html")
