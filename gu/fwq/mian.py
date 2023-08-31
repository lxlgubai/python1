import json
from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web
from pymysql import connect


class MainHandler(tornado.web.RequestHandler):
    # 查询数据
    def get(self):
        # 链接数据库
        conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030',
                       charset='utf8')
        csl = conn.cursor()
        # 执行SQL语句
        csl.execute("select * from userinfo;")

        data = csl.fetchall()
        # 关闭数据库
        csl.close()
        conn.close()

        print(data)

        self.render("index.html",show_list=data)

    # 添加数据
    def post(self):

        params_list = list()

        params_list.append(self.get_argument('usename'))
        params_list.append(self.get_argument('age'))
        params_list.append(self.get_argument('sex'))
        params_list.append(self.get_argument('passwrod1'))
        params_list.append(self.get_argument('phone1'))
        params_list.append(self.get_argument('sites'))
        params_list.append(self.get_argument('mailbox'))
        params_list.append(self.get_argument('Date'))

        # 链接数据库
        conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030',
                       charset='utf8')
        csl = conn.cursor()
        # 执行SQL语句
        csl.execute("insert into userinfo(usename,age,sex,passwrod1,phone1,sites,mailbox,Date) VALUFS (%s,%s,%s,%s,%s,%s,%s,%s)",params_list)

        # 提交数据
        conn.commit()
        # 关闭数据库
        csl.close()
        conn.close()

        self.write({"data": "添加成功"})

    def put(self):
        decode_body = self.request.body.decode("utf-8")

        params_dict = json.loads(decode_body)

        print(params_dict)

        # 链接数据库
        conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030',
                       charset='utf8')
        csl = conn.cursor()
        # 执行SQL语句
        # usename,age,sex,passwrod1,phone1,sites,mailbox,Date
        csl.execute("update books set usename=%(usename)s, age=%(age)s, sex=%(sex)s, passwrod1=%(passwrod1)s, phone1=%(phone1)s, sites=%(sites)s, mailbox=%(mailbox)s, Date=%(Date)s",params_dict)

        # 提交数据
        conn.commit()

        # 提交数据
        conn.commit()
        # 关闭数据库
        csl.close()
        conn.close()

        self.write("put")

    def delete(self):
        self.write("修改的数据")

    # 路由函数


def make_app():
    return tornado.web.Application([
        (r"/books/", MainHandler),  # 路由
    ],
        static_path='../static',  # 静态文件夹
        template_path='templstes'  # 模板路径

    )

    # 程序入口


if __name__ == "__main__":
    # 加载配置
    app = make_app()
    # 设置监听
    app.listen(8787)
    tornado.ioloop.IOLoop.current().start()
