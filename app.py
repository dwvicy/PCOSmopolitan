from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np


app = Flask(__name__, template_folder="template")

reg = pickle.load(open("model.pkl", "rb"))




@app.route("/")
def hello_worl():
     return render_template("index.html")
    
@app.route("/remedies")
def hello_1():
    return render_template("remedies.html")

@app.route("/login")
def hello2():
     return render_template("login.html")
 



@app.route("/test")
def hello1():
     return render_template("test.html") 
 
 
@app.route("/predict", methods=["POST"])
def home():
   
    data2 = float(request.form["b"])
    data3 = float(request.form["c"])
    data4 = float(request.form["d"])
    d5 = float(request.form["e"])
    d6 = float(request.form["f"])
    d7 = float(request.form["g"])
    d8 = float(request.form["h"])
    d9 = float(request.form["i"])
    d10 = float(request.form["j"])
    d11 = float(request.form["k"])
    d12 = float(request.form["l"])
    d13 = float(request.form["m"])
    d14 = float(request.form["n"])
    d15 = float(request.form["o"])
    d16 = float(request.form["p"])
    d17 = float(request.form["q"])
    d18 = float(request.form["r"])
    d19 = float(request.form["s"])
    d20 = float(request.form["t"])
    d21 = float(request.form["u"])
    d22 = float(request.form["v"])
    d23 = float(request.form["w"])
    d24 = float(request.form["x"])
    d25= float(request.form["y"])
    d26 = float(request.form["z"])
    d27 = float(request.form["za"])
    d28 = float(request.form["zb"])
   
   

    arr = np.array(
        [
            [
                data2,
                data3,
                data4,
                d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,
                d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28
                            ]
        ]
    )
    pred = reg.predict(arr)
    print(pred)
    return render_template("predict.html", data=pred)


    

if __name__ == "__main__":
    app.run(debug=True)
