from flask import Flask, render_template, request, url_for, session, redirect
from classe import *

app = Flask("__name__")

app.config["SECRET_KEY"] = 'admin'
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form_criar_votacao")
def form_criar_votacao():
    return render_template("criar_votacao.html")

@app.route("/criar_votacao", methods=['post'])
def criar_votacao():
    pass

@app.route("/votar")
def votar():
    return render_template("votar.html")

@app.route("/ver_ranking")
def ver_ranking():
    return render_template("ver_ranking.html")

@app.route("/form_cadastrar")
def form_cadastrar():
    return render_template("cadastrar.html")

@app.route("/cadastrar", methods=['post'])
def cadastrar():
    pass

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    email = request.form["email"]
    senha = request.form["senha"]

    if email == "bla@gmail.com" and senha == "admin":
        session['usuario'] = email
        return redirect("/")
    else:
        return "erro no login, tente novamente"

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

app.run(debug=True)