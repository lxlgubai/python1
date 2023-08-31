import flask, json
from flask import request

server = flask.Flask(__name__)


@server.route('/list/project',methods=['get'])
def projectlist():
    proj = request.values.get('project')
    name = request.values.get('name')
    project={
        "mdg":"查询成功",
        "status":200,
        "data":[{   "project":proj,"name":name}]
    }
    return project

@server.route('/login',methods=['post'])
def login():
    params = flask.request.json
    if params:
        dic = {
            'user_name':params.get('user_name'),
            'pwd':params.get('pwd')
        }
        login_info={
            "data":{
                "id": 500,
                "rid":0,
                "username": dic['user_name'],
                "pwd": '********',
                "mobile": "12345678",
                "email": "adsfad@qq.com",
                "token": "Bearer eyJhbGciOi"
            },
            "meta":{
                "msg":"登陆成功",
                "status":200
            }
        }

        data = json.dumps(login_info)
        print("'/login',methods=['psot']: %s; %s"%(str(dic),str(data)))
        return  login_info
    else:
        data = ({"result_code":3002, "msg":"入参必须为json类型"})
        print("'/login',methods=['psot']:"+str(data))
        return data


if __name__ == '__main__':
    if __name__ == "__main__":
        server.run('0.0.0.0',port=5000,debug=True)