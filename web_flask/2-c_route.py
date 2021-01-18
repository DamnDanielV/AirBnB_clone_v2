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


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
