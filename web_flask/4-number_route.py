#!/usr/bin/python3
from flask import Flask
from markupsafe import escape
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
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_r(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
