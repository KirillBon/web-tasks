import json
from flask import Flask, jsonify, request, render_template
import psycopg2
app = Flask(__name__)
data = [{'id': 0, 'name': 'Dave', 'surname': 'McWeber'},
        {'id': 1, 'name': 'Jerry', 'surname': 'Stark'}]


conn = psycopg2.connect(
    host="localhost",
    database="MyDataBase",
    user="postgres",
    password="1111",
)
TABLE_NAME = "users"
COLUMNS = ['user_id', 'user_name', 'user_surname']
cursor = conn.cursor()
success_message = {'success': True}


@app.errorhandler(404)
def user_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/users', methods=['GET'])
def get_users():
    # select all sorted by user_id
    sql = 'SELECT * FROM users ORDER BY user_id ASC;'
    cursor.execute(sql)
    data = cursor.fetchall()
    # convert to list of lists
    data = list(map(list, data))
    # convert to list of dicts
    for cor, val in enumerate(data):
        data[cor] = dict(zip(COLUMNS, data[cor]))
    print(data)
    return jsonify(data)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    sql = 'SELECT * FROM users WHERE user_id=%s;'
    cursor.execute(sql, (str(user_id),))
    data = cursor.fetchall()
    # convert to list of lists
    data = list(map(list, data))
    # convert to list of dicts
    for cor, val in enumerate(data):
        data[cor] = dict(zip(COLUMNS, data[cor]))
    print(data)
    if not data:
        return user_not_found(404)
    else:
        return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    sql = 'INSERT INTO users (user_name, user_surname) VALUES (%s, %s)'
    name = request.json['user_name']
    surname = request.json['user_surname']
    cursor.execute(sql, (name, surname))
    conn.commit()
    print(success_message)
    return jsonify(data)


@app.route('/users', methods=['PUT'])
def update_user():
    sql = 'UPDATE users SET user_name=%s, user_surname=%s WHERE user_id=%s'
    user_id = request.json['user_id']
    name = request.json['user_name']
    surname = request.json['user_surname']
    cursor.execute(sql, (name, surname, user_id,))
    conn.commit()
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    sql = 'DELETE FROM users WHERE user_id=%s'
    user_id = request.json['user_id']
    cursor.execute(sql % user_id)
    conn.commit()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)