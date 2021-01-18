#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear(self):
    storage.close()


@app.route('/states_list')
def state_l():
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
