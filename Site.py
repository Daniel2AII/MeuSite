from flask import flask

app = Flask(__name__)

@app.route("/")
def Index():
    return "Olá mundo!"

if __name__ == "__main__":
    app.run(debug = True)