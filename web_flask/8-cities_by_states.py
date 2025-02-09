#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0:5000"""

from flask import Flask, render_template, g
from os import getenv
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Renders a list of all states from the database"""

    states = storage.all(State).values()

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close(exception=None):
    """Removes the current SQLAlchemy Session after each request"""
    #from models import storage
    if hasattr(g, 'db'):
        g.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
