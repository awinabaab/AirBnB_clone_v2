#!/usr/bin/python3
"""Starts a Flask web application on 0.0.0.0:5000"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays filters and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close(exception=None):
    """Closes the database session after each request"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
