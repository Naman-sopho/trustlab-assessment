import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)


initial_html = ' <form><input type="text" id="input-text" name="input-text"></form>\
<h4 id="result"></h4>\
<script src="https://code.jquery.com/jquery-3.5.1.js"\
    integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous">\
</script>\
<script>\
let typingTimer;\
let doneTypingInterval = 500;\
let myInput = document.getElementById(\'input-text\');\
myInput.addEventListener(\'keyup\', () => {\
    clearTimeout(typingTimer);\
    if (myInput.value) {\
        typingTimer = setTimeout(doneTyping, doneTypingInterval);\
    }\
});\
\
function doneTyping () {\
    console.log(\'done typing\');\
    var text = $("#input-text").val();\
    console.log(text);\
    $.post(\'/analyze\',\
        {"input-text": text},\
        function(data) {\
            $("#result").html(data["feedback"])\
        }\
    );\
}\
</script>'

@app.route('/', methods=['GET'])
def root():
    return initial_html

@app.route('/analyze', methods=['POST'])
def analyze_text():
    input_text = request.form['input-text']

    # call to text analyzer like BERT
    # assuming model returns JSON
    result = '{"report": "56"}'
    result_json = json.loads(result)
    report = int(result_json['report'])
    
    feedback = str(report) + chr(37) + ' likely to be hate speech. '
    if report > 70:
        feedback += 'Please edit.'
    elif report > 40:
        feedback += 'Please consider editing before posting.'
    else:
        feedback += 'Good to go.'
    
    feedback_json = {"feedback": feedback}
    feedback_json = jsonify(feedback_json)
    return feedback_json

app.run()