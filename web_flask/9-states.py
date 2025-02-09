#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML Page with all the states from the database"""
    states = storage.all(State).values()

    return render_template("9-states.html", states=states, path="states")


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with the State object with id"""
    state = storage.all(State).get(f"State.{id}")

    return render_template("9-states.html", state=state, path="states_id")


@app.teardown_appcontext
def close(exception=None):
    """Closes the database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
