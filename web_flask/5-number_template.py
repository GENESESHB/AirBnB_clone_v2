#!/usr/bin/python3
"""
starting flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    hello flask app with this prompt hellohbnb
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
    remplace text with string c + text
    """
    text = text.replace('_', ' ')
    return "C " + str(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_post(text="is cool"):
    """
    difine a function can remplace text with is cool
    """
    text = text.replace('_', ' ')
    return "Python" + str(text)


@app.route('/number/<int:n>', strict_slashes=False)
def npost(n):
    """
    return number
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    '''
    display an html page onlY if <n> is an integer
    '''
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
