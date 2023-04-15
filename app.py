from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    string_to_reverse = data['string']
    reversed_string = string_to_reverse[::-1]
    response_data = {'reversed_string': reversed_string}
    return jsonify(response_data)

