from flask import Flask,request,json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():

    return 'f'




if __name__ == '__main__':
    app.run(debug=True)


