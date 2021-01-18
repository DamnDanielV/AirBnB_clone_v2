#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hello')
def hello_HBNB():
    return('Hello HBNB!')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')