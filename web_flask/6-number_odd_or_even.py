#!/usr/bin/python3
'''Flask Module'''
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''First Flask Function'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    '''Second Flask Function'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    '''Third Flask Function'''
    return "C {}".format(str(text)).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    '''Forth Flask Function'''
    return "Python {}".format(str(text)).replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def hello_num(n):
    '''Fifth Flask Function'''
    try:
        return "{} is number".format(int(n))
    except:
        return abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def num_temp_func(n):
    """Number Page"""
    try:
        number = int(n)
        return render_template("5-number.html", number=n)
    except:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def num_odd_even(n):
    '''when odd or even'''
    try:
        number = int(n)
        return render_template('6-number_odd_or_even.html', number=number)
    except:
        abort(404)


if __name__ == "__main__":
    app.run()
