from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "webpatines"

@app.route("/")
def home():
    return render_template("index.html", page="home")

if __name__ == "__main__":
    app.run(debug=True)
