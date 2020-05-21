import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)


initial_html = ' <form><input type="text" id="input-text" name="input-text"></form>\
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
    $.post(\'/analyze\', {\
        "input-text": text\
    });\
}\
</script>'

@app.route('/', methods=['GET'])
def root():
    return initial_html

@app.route('/analyze', methods=['POST'])
def analyze_text():
    input_text = request.form['input-text']
    return input_text

app.run()