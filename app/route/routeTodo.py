from app import app
from app.controller import todoController, todoFileController
from flask import request

@app.route('/todo', methods=['POST','GET'])
def todo():
    if request.method == 'POST':
        return todoController.store()
    elif request.method == 'GET':
        return todoController.index()




@app.route('/todo/<id>', methods=['PUT', 'GET', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return todoController.show(id)
    elif request.method == 'PUT':
        return todoController.update(id)
    elif request.method == 'DELETE':
        return todoController.delete(id)


# @app.route('/todo-files/<id>', methods=['POST'])
# def todoFiles(id):
#     if request.method == 'POST':
#         return todoFileController.store(id)

@app.route('/todo-files/<id>', methods=['POST','GET'])
def todoFiles(id):
    if request.method == 'POST':
        return todoFileController.store(id)
    if request.method == 'GET':
        return todoFileController.index(id)