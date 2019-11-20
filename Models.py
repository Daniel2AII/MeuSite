from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'
db = SQLAlchemy(app)

class Pacient(db.Model):
    usuario = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=True)
    dataNascimento = db.Column(db.DateTime, default=datetime.utcnow), unique=True, nullable=False
    e_mail = db.Column(db.String(100), unique=True nullable=False)
    genero = db.Column(db.String(20), unique=True nullable=False)
    senha = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Pacient %r>' % self.usuario