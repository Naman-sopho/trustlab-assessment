import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)

initial_html = '<embed type="text/html" src="embed" width="500" height="200">'

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
    if value is not None:
        global percentage
        percentage = int(value)
    return embed()

@app.route('/analyze', methods=['POST'])
def analyze_text():
    input_text = request.form['input-text']

    # call to text analyzer like BERT
    # assuming model returns JSON
    result = '{"report": "86"}'
    result_json = json.loads(result)
    report = int(result_json['report'])
    
    # following is just for testing purposes and proof of concept
    report = percentage

    feedback = str(report) + chr(37) + ' likely to be hate speech. '
    if report > 70:
        feedback += 'Please edit.'
    elif report > 40:
        feedback += 'Please consider editing before posting.'
    else:
        feedback += 'Good to go.'
    
    feedback_json = {"feedback": feedback, "val": report}
    feedback_json = jsonify(feedback_json)
    return feedback_json

app.run()