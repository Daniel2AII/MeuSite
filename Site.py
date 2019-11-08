from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)