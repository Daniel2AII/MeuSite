from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Forms import FormPacient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bando_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'
db = SQLAlchemy(app)


class Pacient(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    age = db.Column(db.String(15), unique=False, nullable=False)
    genre = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    confirm_password = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '<Pacient %r>' % self.usuario


@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/login", methods=['POST', 'GET'])
def Login():
    return render_template("/_links/_Login.html")

@app.route("/about")
def About():
    return render_template("_links/_About.html")

@app.route("/register", methods=['POST', 'GET'])
def Register():

    form = FormPacient()
    if form.validate_on_submit():
        user = Pacient()
        user.username = form.username.data
        user.age = form.age.data
        user.genre = form.genre.data
        user.email = form.email.data
        user.password = form.password.data
        user.confirm_password = form.confirm_password.data
        db.session.add(user)
        db.session.commit()

    return render_template("_links/_Register.html", form=form)

@app.route("/quiz")
def Quiz():
    return render_template("_links/_Quiz.html")

@app.route("/solution0")
def Solution0():
    return render_template("_links/_Solution0.html")

@app.route("/solution1")
def Solution1():
    return render_template("_links/_Solution1.html")

@app.route("/solution2")
def Solution2():
    return render_template("_links/_Solution2.html")

@app.route("/solution3")
def Solution3():
    return render_template("_links/_Solution3.html")

if __name__ == "__main__":
    app.run(debug=True, port=8888)