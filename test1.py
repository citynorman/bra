# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 09:02:17 2014

@author: stn821
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()