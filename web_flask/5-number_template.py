#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, abort, render_template

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
    '''new route with text variable'''
    return 'Python {}'.format(str(text.replace('_', ' ')))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    '''new route with int variable'''
    try:
        return '{} is a number'.format(int(n))
    except:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''new route with int variable and render'''
    try:
        return render_template('5-number.html', n=(int(n)))
    except:
        abort(404)

if __name__ == '__main__':
    app.run()
