from flask import Flask, request, redirect, render_template

app = Flask(__name__)

lista = [1, 2, 3, 4]

studenti = [
    {"id": 1, "nome": "Anna"},
    {"id": 2, "nome": "Marco"}
]

@app.route("/")
def index():
    return render_template("index.html", lista = lista)

if __name__ == "__main__":
    app.run(debug = True)