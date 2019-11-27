from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Forms import FormPacient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bando_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'
db = SQLAlchemy(app)


class Pacient(db.Model):
    usuario = db.Column(db.String(20), primary_key=True)
    idade = db.Column(db.DateTime, unique=True, nullable=False)
    e_mail = db.Column(db.String(100), unique=True, nullable=False)
    genero = db.Column(db.String(20), unique=True, nullable=False)
    senha = db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Pacient %r>' % self.usuario


@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/register", methods=['POST', 'GET'])
def Register():
    return render_template("/_links/_Register.html")

@app.route("/about")
def About():
    return render_template("_links/_About.html")

@app.route("/form_pacient", methods=['POST', 'GET'])
def Pacient():

    form = FormPacient()
    if form.validate_on_submit():
        user = Pacient()
        user.usuario = form.usuario.data
        user.idade = form.idade.data
        user.e_mail = form.e_mail.data
        user.senha = form.senha.data
        db.session.add(user)
        db.session.commit()

    return render_template("_links/_FormP.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)