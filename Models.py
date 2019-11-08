from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'
db = SQLAlchemy(app)

class Pacient(db.Model):
    usuarioP = db.Column(db.String(20), primary_key=True)
    nomeP = db.Column(db.String(100), unique=True, nullable=True)
    idade = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Pacient %r>' % self.usuarioP

class Doctor(db.Model):
    usuarioD = db.Column(db.String(20), primary_key=True)
    nomeD = db.Column(db.String(100), unique=True, nullable=True)

    def __repr__(self):
    return '<Doctor %r>' % self.usuarioD