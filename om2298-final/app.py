# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template, url_for

#Flask app variable
app = Flask(__name__, template_folder="templates")

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def homepage_1006():
    return render_template("homepage_1006.html")

@app.route("/1006/assignments")
def assignments_1006():
    return render_template("assignments.html")

@app.route("/1006/classes")
def classes_1006():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()