import numpy as np
from matplotlib import pyplot as plt
from pymysql import connect

conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
csl = conn.cursor()

csl.execute("SELECT serialize as 分类,moods as 评分 FROM	fiction1 GROUP BY serialize;")

data = csl.fetchall()
# print(data)
dd1 = []
dd2 = []
for data1,data2 in data:
    dd1.append(data1)
    dd2.append(data2)
# print(dd1)
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False
y = dd1
plt.plot(y,dd2,color='r')
plt.title('图形')
plt.show()

conn.close()
csl.close()