from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/criar_votacao")
def criar_votacao():
    return render_template("criar_votacao.html")

@app.route("/votar")
def votar():
    return render_template("votar.html")

@app.route("/ver_ranking")
def ver_ranking():
    return render_template("ver_ranking.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")

app.run()