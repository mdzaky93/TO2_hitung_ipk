from app import db
from datetime import datetime
from app.model.todo import Todos


class TodoFiles(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_name = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    todo_id = db.Column(db.BigInteger, db.ForeignKey(Todos.id))
    todos = db.relationship("Todos", backref="todo_id")



    def __repr__(self):
        return '<Todo {}>'.format(self.todo)