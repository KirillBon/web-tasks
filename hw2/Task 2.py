import json
from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{'id': 0, 'name': 'Kirill', 'surname': 'Bondarev'}]

@app.route('/users', methods=['GET'])
def user_get():
    return jsonify(data)

@app.route('/users', methods=['PUT'])
def user_upd():
    data[request.get_json()['id']] = request.get_json()
    return jsonify(data)

@app.route('/users', methods=['POST'])
def user_add():
    request_data = {
        'id': int(data[-1]['id']) + 1,
        'name': request.json['name'],
        'surname': request.json['surname']
    }
    data.append(request.get_json())
    return jsonify(data)

@app.route('/users', methods=['DELETE'])
def user_del():
    data.remove(request.get_json()['id'])
    return jsonify(data)
    pass

if __name__ == '__main__':
    app.run(debug=True)
