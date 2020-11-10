 #Grupo pablo
from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "webchicles"

@app.route("/")
def home():
    return render_template("index.html", page="inicio")

@app.route("/App/")
def aplicación():
    return render_template("index.html", page="home")

@app.route("/Tarifas/")
def tarifas():
    return render_template("index.html", page="Tarifas")

@app.route("/Terminos/")
def terminos():
    return render_template("index.html", page="Terminos")

@app.route("/Contacto/")
def contacto():
    return render_template("contacto.html", page="Contacto")

if __name__ == "__main__":
    app.run(debug=True)