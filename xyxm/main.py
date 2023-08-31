from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/homa")
def hello():
    date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html",x1=date_string)

if __name__ == "__main__":
    app.run()