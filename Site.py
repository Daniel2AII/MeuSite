from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Banco_Usuarios.db'
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
    usuario = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=True)
    idade = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.Integer, unique=True, nullable=False)


if __name__ == "__main__":
    app.run(debug = True)