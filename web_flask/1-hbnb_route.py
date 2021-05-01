#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''web application must be listening on 0.0.0.0, port 5000'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''new route'''
    return 'HBNB'

if __name__ == '__main__':
    app.run()
