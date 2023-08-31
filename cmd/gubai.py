from flask import Flask
import flask ,json

# 创建 Flask 实例，在 OOP 中这叫类的实例化
app = Flask(__name__)

# 编写路由
@app.route("/uerc")
def index(): # 编写 视图函数，用户访问的根路径都会给 index 这个视图函数
	return "Hello World"



# 运行实例，并设置端口为 3000
app.run(port=3100)

