#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that displays "Hello HBNB!" """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbtnb():
    """function that display HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbtnb1(text):
    """function that display C followed by text's"""
    return("C {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
