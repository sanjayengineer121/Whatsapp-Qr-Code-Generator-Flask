from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import webbrowser
from PIL import Image
import os
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/add", methods=["POST"])
def add():
    Mobile = request.form.get("Mobile")
    Message = request.form.get("Message")
    print(Mobile)
    print(Message)
    import qrcode
    #https://wa.me/919818428221?text=Hi
    qrdata="https://wa.me/91"+Mobile+"?text="+Message
    qr = qrcode.make(qrdata)
    qr.save('wrcode.png')
    webbrowser.open('wrcode.png')
    

    return redirect(url_for("home"))
    
    

if __name__ == "__main__":
    app.run(debug=True)