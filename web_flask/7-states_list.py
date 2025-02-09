#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0:5000"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Renders a list of all states from the database"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states.values())


@app.teardown_appcontext
def close(exception=None):
    """Removes the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
