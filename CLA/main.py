from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def main_app():
    return "<h1>Welcome to trendsaf core<h1/>"

if __name__== "__main__":
    serve(app, host="0.0.0.0", port=8080)