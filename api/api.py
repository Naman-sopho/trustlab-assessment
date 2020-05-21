import flask
from flask import jsonify


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return '<h1>Hello World!!!</h1>'

app.run()