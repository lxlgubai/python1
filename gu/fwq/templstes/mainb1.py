 # 导入模块，固定写法
from pymysql import connect
from pydantic import BaseModel

class Item(BaseModel):
    def ii(self):
        conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030', charset='utf8')
        csl = conn.cursor()
        # 执行SQL语句
        csl.execute("select * from userinfo;")

        data = csl.fetchall()

        # 关闭数据库
        conn.close()
        csl.close()

        print(data)
 # conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030',charset='utf8')
# csl = conn.cursor()
# # 执行SQL语句
# csl.execute("select * from userinfo;")
#
# data = csl.fetchall()
# print(data)
# # 关闭数据库
# conn.close()
# csl.close()
