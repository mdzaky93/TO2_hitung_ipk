from app import app
from app.controller import hitung_ipk_controller
from flask import request

@app.route('/hitung_ipk', methods=['POST','GET'])
def todo():
    if request.method == 'POST':
        return hitung_ipk_controller.store()
    elif request.method == 'GET':
        return hitung_ipk_controller.index()




@app.route('/hitung_ipk/<id>', methods=['PUT', 'GET', 'DELETE'])
def todoDetail(id):
    if request.method == 'GET':
        return hitung_ipk_controller.show(id)
    elif request.method == 'PUT':
        return hitung_ipk_controller.update(id)
    elif request.method == 'DELETE':
        return hitung_ipk_controller.delete(id)


# @app.route('/todo-files/<id>', methods=['POST'])
# def todoFiles(id):
#     if request.method == 'POST':
#         return todoFileController.store(id)

# @app.route('/hitung_ipk/<id>', methods=['POST','GET'])
# def todoFiles(id):
#     if request.method == 'POST':
#         return hitung_ipk_controller.store(id)
#     if request.method == 'GET':
#         return hitung_ipk_controller.index(id)