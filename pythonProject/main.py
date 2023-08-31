import json
import sys

import pymysql
from flask import Flask, request
from flask_cors import CORS
# from pythonProject.__nain__ import yhxx1

app = Flask(__name__)
CORS(app)

conn = pymysql.connect(host='localhost', port=3306, database='gubai',
                       user='root', password='102030',charset='utf8')
csl = conn.cursor()

@app.route('/')
def main():
    return '你好'

# 获取用户信息
@app.route('/yhxx', methods=['GET', 'POST'])
def yhxx():
    # print(request.values.get('pager'))
    # 用户信息查询
    # aa = yhxx1()
    # return aa
    pass
# 登录
@app.route('/Landind1', methods=['GET', 'POST', 'PUT'])
def Landind1():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        yx = request.form.get('yx')
        yzxx = {username, password, yx}
    return '登录成功'

# 注册
@app.route('/Registration', methods=['GET', 'POST'])
def Registration():
        if request.method == 'POST':
            print(request.form.get('username'))
            print(request.form.get('password'))
            print(request.form.get('yx'))
            print(request.form.get('ty'))

        return '成功'
if __name__ == '__main__':
    app.run(debug=True)