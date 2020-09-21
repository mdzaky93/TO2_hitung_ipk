from app import app
from app.controller import userController
from flask import request


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()


@app.route('/users/', methods=['PUT', 'GET', 'DELETE'])
@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id=0):
    if request.method == 'GET':
        return userController.show(id)
    elif request.method == 'PUT':
        return userController.update(id)
    elif request.method == 'DELETE':
        return userController.delete(id)

@app.route('/login', methods=['POST'])
def login():
    return userController.login()

@app.route('/refresh', methods=['POST'])
def refresh():
    return userController.refresh()