import numpy as np
from matplotlib import pyplot as plt
from pymysql import connect

conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
csl = conn.cursor()

csl.execute("SELECT DISTINCT `name` as 书名,`read` as 阅读 FROM fiction1 ORDER BY `read` desc LIMIT 10;")

data = csl.fetchall()

dd1 = []
dd2 = []
for data1,data2 in data:
    dd1.append(data1)
    dd2.append(data2)
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False
x = np.array(dd1)
y = np.array(dd2)
plt.title('图形')
plt.bar(x,y, color="c", linewidth=2.0)
plt.show()

conn.close()
csl.close()