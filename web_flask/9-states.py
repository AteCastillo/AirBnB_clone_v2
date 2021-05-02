#!/usr/bin/python3
'''Flask Module'''

from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all("State")
    key = "{}.{}".format('State', id)
    return render_template("9-states.html", states=states, key=key, id=id)    


@app.teardown_appcontext
def close_session(self):
    """to close session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
