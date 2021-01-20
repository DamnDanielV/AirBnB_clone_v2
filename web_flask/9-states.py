#!/usr/bin/python3
"""fgfhjdmds gdszx dfdx"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear(self):
    storage.close()


@app.route('/states')
def state_l():
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_id():
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
