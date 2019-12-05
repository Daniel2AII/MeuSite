from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Forms import FormPacient, FormLoginPacient
from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bando_Usuarios.db'
app.config['SECRET_KEY'] = '2f15588715f5012b4d63e76a1a47e357'
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)


class Pacient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    age = db.Column(db.String(15), unique=False, nullable=False)
    genre = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    confirm_password = db.Column(db.String(100), unique=False, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Usuário %r>' % self.username

@lm.user_loader
def load_user(id):
    return Pacient.query.filter_by(id=id).first()

@app.route("/", methods=['POST', 'GET'])
def Index():
    return render_template("Index.html")

@app.route("/login", methods=['POST', 'GET'])
def Login():

    form = FormLoginPacient()
    print('entrei aqui - tentando login..')
    print(form.validate_on_submit())
    print(form.username)
    print(form.password)
    if form.validate_on_submit():
        print('entrei aqui primeiro..')
        user = Pacient.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            print('entrei aqui..')
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("Quiz"))
        else:
            print('entrei aqui - erro..')
            flash("Invalid login.")

    return render_template("/_links/_Login.html", form=form)

@app.route("/logout")
def Logout():
    logout_user()
    return redirect(url_for("Index"))

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

        return redirect(url_for("Index"))        

    return render_template("_links/_Register.html", form=form)

@app.route("/quiz", methods=['POST', 'GET'])
def Quiz():
    return render_template("_links/_Quiz.html")

@app.route("/solution0", methods=['POST', 'GET'])
def Solution0():
    return render_template("_links/_Solution0.html")

@app.route("/solution1", methods=['POST', 'GET'])
def Solution1():
    return render_template("_links/_Solution1.html")

@app.route("/solution2", methods=['POST', 'GET'])
def Solution2():
    return render_template("_links/_Solution2.html")

@app.route("/solution3", methods=['POST', 'GET'])
def Solution3():
    return render_template("_links/_Solution3.html")

if __name__ == "__main__":
    app.run(debug=True, port=8888)