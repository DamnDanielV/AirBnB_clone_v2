#!/usr/bin/python3
"""dfghjk ghjk ghjkaa"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear(self):
    storage.close()


@app.route('/cities_by_states')
def state_l():
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
