from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
@app.route("/index.html")
def index():
    return "Hello World!"

