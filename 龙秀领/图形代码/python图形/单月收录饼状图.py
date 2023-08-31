from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from linkd import selectdata

mysql = "SELECT title,month_index FROM chinaz LIMIT 1,30;"

data = selectdata(mysql)
ff = Faker
ss = []
for z in data:
    ss.append(list(z))
c = (
    Pie()
    .add(
        "",
        ss,
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="排名前30单月收录饼状图"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("单月收录饼状图.html")
)