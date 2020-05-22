from flask import jsonify
import json

def get_model_score(text, percentage):
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
