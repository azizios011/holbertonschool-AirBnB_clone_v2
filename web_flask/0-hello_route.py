#!/usr/bin/python3
""" 
    a Flask web application

"""
from flask import Flask

app = Flask(__name__)
@app.route("/")
"""
a route to display the text

"""
def hello_hbnb():
    return 'Hello HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

