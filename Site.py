from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import FormDoctor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'

db = SQLAlchemy(app)


@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/register", methods=['POST', 'GET'])
def Register():
    return render_template("/_links/_Register.html")

@app.route("/about")
def About():
    return render_template("_links/_About.html")

@app.route("/form_doctor")
def FormDoctor():
    return render_template("_links/_FormD.html")

@app.route("/form_pacient")
def FormPacient():
    return render_template("_links/_FormP.html")


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


if __name__ == "__main__":
    app.run(debug = True)