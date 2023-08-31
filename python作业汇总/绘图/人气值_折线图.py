import numpy as np
from matplotlib import pyplot as plt
from pymysql import connect

conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
csl = conn.cursor()

csl.execute("SELECT DISTINCT `name` as 书名,`score` as 人气值 FROM fiction1 ORDER BY `score` desc LIMIT 7; ")

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
x = dd1
y = dd2
plt.plot(x,y)
plt.title('图形')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

conn.close()
csl.close()