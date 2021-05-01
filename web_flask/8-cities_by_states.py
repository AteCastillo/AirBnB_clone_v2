#!/usr/bin/python3
''' starts a Flask web application'''

from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display all cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_session(self):
    """to close session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
