from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np


app = Flask(__name__, template_folder="template")

reg = pickle.load(open("model.pkl", "rb"))




@app.route("/home")
def hello_worl():
     return render_template("index.html")
    
@app.route("/remedies")
def hello_1():
    return render_template("remedies.html")

@app.route("/")
def hello2():
     return render_template("login.html")


@app.route("/test")
def hello():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)
