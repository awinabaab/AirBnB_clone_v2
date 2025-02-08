#!/usr/bin/python3
"""Starts a Flask web application on 0.0.0.0:5000"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of the text variable

    params:
        text (str)
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is_cool"):
    """Displays 'Python' followed by the value of the text variable

    params:
        text (str)
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' if only n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template_route(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
