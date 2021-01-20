#!/usr/bin/python3
""" flask flask flaaasaskkk"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear(self):
    storage.close()


@app.route('/hbnb_filters')
def state_l():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('6-index.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
