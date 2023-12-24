#!/usr/bin/python3
"""
starting flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    hello flask
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hello prompt hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def testpost(text):
    """
    remplace text with string
    """
    text = text.replace('_', ' ')
    return "C " + str(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
