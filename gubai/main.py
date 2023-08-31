import json

from flask import Flask, request
from flask_cors import CORS

from gubai.user import user1, mysql
import pymysql

conn = pymysql.connect(host='192.168.233.200', port=3306, database='gubai', user='root', password='102030',charset='utf8')
csl = conn.cursor()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '成功'

@app.route('/user')
def user():
    sss = user1()
    return sss

@app.route('/ywcli', methods=["GET", "POST"])
def ywcli():
    set_config = request.args.to_dict()
    num1 = set_config.get('name')
    # print(num1)
    js = json.dumps(num1)
    print(js)
    return js

if __name__ == '__main__':
    app.run(debug=True)