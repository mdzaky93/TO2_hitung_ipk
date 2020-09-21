from app.model.mahasiswa import Mahasiswas
from flask import request, jsonify
from app import response, db
from app.controller import userController

def store():
    try:
        nim = request.json['nim']
        nama_mahasiswa = request.json['nama_mahasiswa']
        mutu = request.json['mutu']
        jumlah_sks = request.json['jumlah_sks']
        ipk = request.json['ipk']
        # ipk = mutu / jumlah_sks
        user_id = request.json['user_id']

        mahasiswa = Mahasiswas(user_id=user_id, nim=nim, nama_mahasiswa=nama_mahasiswa, mutu=mutu, jumlah_sks=jumlah_sks, ipk=ipk)
        db.session.add(mahasiswa)
        db.session.commit()
        
        return response.ok('', 'Successfully create IPK')
        # print(mutu, jumlah_sks)

    except Exception as e:
        print(e)


def index():
    try:
        id = request.args.get('user_id')
        mahasiswa = Mahasiswas.query.filter_by(user_id=id).all()
        data = transform(mahasiswa)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    print(values.users.id)
    print(values.users.email)
    data = {
        'id': values.id,
        'user_id': values.user_id,
        'nim': values.nim,
        'nama_mahasiswa': values.nama_mahasiswa,
        'mutu': values.mutu,
        'jumlah_sks': values.jumlah_sks,
        # 'ipk': values.ipk,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        'user': userController.singleTransform(values.users)
    }

    return data



def update(id):
    try:
        nim = request.json['nim']
        nama_mahasiswa = request.json['nama_mahasiswa']
        mutu = request.json['mutu']
        jumlah_sks = request.json['jumlah_sks']
        ipk = request.json['ipk']
        # ipk = float(mutu)/float(jumlah_sks)
        mahasiswa = Mahasiswas.query.filter_by(id=id).first()
        
        mahasiswa.nim = nim
        mahasiswa.nama_mahasiswa = nama_mahasiswa
        mahasiswa.mutu = mutu
        mahasiswa.jumlah_sks = jumlah_sks
        mahasiswa.ipk = ipk
        db.session.commit()
        return response.ok('', 'Successfully update IPK')
    except Exception as e:
        print(e)


def show(id):
    try:
        mahasiswa = Mahasiswas.query.filter_by(id=id).first()
        if not mahasiswa:
            return response.badRequest([], 'Empty....')

        data = singleTransform(mahasiswa)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def delete(id):
    try:
        mahasiswa = Mahasiswas.query.filter_by(id=id).first()
        if not mahasiswa:
            return response.badRequest([], 'Empty....')

        db.session.delete(mahasiswa)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)


