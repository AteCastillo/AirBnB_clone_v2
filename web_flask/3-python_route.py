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


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''new route with variable'''
    return 'C {}'.format(str(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def texts(text='is cool'):
    '''new route with variable'''
    return 'Python {}'.format(str(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run()
