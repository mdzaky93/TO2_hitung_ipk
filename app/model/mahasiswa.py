from app import db
from datetime import datetime
from app.model.user import Users


class Mahasiswas(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(10), unique=True, nullable=False)
    nama_mahasiswa = db.Column(db.String(100), nullable=False)
    mutu = db.Column(db.Integer(), nullable=False)
    jumlah_sks = db.Column(db.Integer(), nullable=False)
    ipk = db.Column(db.Float(2,2), nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users = db.relationship("Users", backref="user_id")

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.nama_mahasiswa)