#!/usr/bin/python3
"""
start web flask :START THE INTERMIDIARE betwine the back-end & front-ent
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """welcome in the intermaidiare"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prompt framwork"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

