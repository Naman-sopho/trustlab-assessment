import flask
from flask import request
import utils


app = flask.Flask(__name__)

initial_html = '<embed type="text/html" src="embed" width="600" height="500">'

global percentage
percentage = 56

@app.route('/', methods=['GET'])
def root():
    return initial_html

@app.route('/embed', methods=['GET'])
def embed():
    f = open('./embed.html')
    return f.read()

@app.route('/<value>')
def set_percentage(value):
    """
    Endpoint for testing different percentage values
    """
    try:
        value = int(value)
    except ValueError:
        return embed()

    if value is not None:
        global percentage
        percentage = int(value)
    return embed()

@app.route('/analyze', methods=['POST'])
def analyze_text():
    input_text = request.form['input-text']

    return utils.get_model_score(input_text, percentage)

app.run()