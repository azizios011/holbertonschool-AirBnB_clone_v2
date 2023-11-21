#!/usr/bin/python3
""" a Flask web application """
from flask import Flask


app = Flask(__name__)


"""a route to display the text"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
