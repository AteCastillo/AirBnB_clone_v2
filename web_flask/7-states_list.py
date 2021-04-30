#!/usr/bin/python3
'''new thing'''

from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """display a HTML all States"""
    states_list = list(storage.all(State).values())
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def close_session(self):
    """function that call close methofd"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
