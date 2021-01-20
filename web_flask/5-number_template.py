#!/usr/bin/python3
"""exercise 5 another comment"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return ('hello HBNB!')


@app.route('/hbnb')
def HBNB():
    return ('HBNB')


@app.route('/c/<text>')
def c_text(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_r(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def tem_r(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
