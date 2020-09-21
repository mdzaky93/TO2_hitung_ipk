import os
import urllib.request
from app.model.berkasTodo import TodoFiles
from app import response, app
from flask import request, jsonify
from app import db

import datetime
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


def store(id):
    # try:
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_convert = filename
            file_convert = "todo__"+id+"__"+ file_convert.lower()
            berkas = TodoFiles(file_name=file_convert, todo_id=id)
            db.session.add(berkas)
            db.session.commit()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_convert))
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201

            return resp
        else:
            resp = jsonify({
                'message':
                'Allowed file types are txt, pdf, png, jpg, jpeg, gif'
            })
            resp.status_code = 400
            return resp

def index(id):
    try:
        todo = TodoFiles.query.filter_by(todo_id=id).all()
        data = transform(todo)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    data = {
        'id': values.id,
        'todo_id': values.todo_id,
        'file_name': values.file_name,
    }

    return data