import numpy as np
from matplotlib import pyplot as plt
from pymysql import connect

conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
csl = conn.cursor()

csl.execute("SELECT DISTINCT classify as 连载状态,COUNT(*) as 次数 FROM fiction1 GROUP BY classify;")

data = csl.fetchall()
# print(data)
dd1 = []
dd2 = []
for data1, data2 in data:
    dd1.append(data1)
    dd2.append(data2)
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False
explode = [0, 0.03]
plt.pie(dd2, labels=dd1, autopct='%.0f%%', explode=explode, shadow=True)
plt.title('图形')
plt.show()

conn.close()
csl.close()
