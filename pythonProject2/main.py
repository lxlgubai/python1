import csv
import json
from flask import Flask
from flask_cors import CORS
from pythonProject2.Epidemic import main

app = Flask(__name__)
CORS(app)

#
# @app.route('/')
# def main():
#     return render_template('index.html')

# @app.route('/app')
# def ind():
#     with open('ind5.json', mode='r', encoding='utf-8') as f:
#         f1 = json.load(f)
#         kd = json.dumps(f1, ensure_ascii=False)
#     return kd
@app.route('/app')
def ind():
    bb = main()
    return bb

def main1():
    date1 = ind()
    return date1



if __name__ == '__main__':
    app.run(debug=True)