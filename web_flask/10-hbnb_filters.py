#/usr/bin/python3
""" """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda state: state.name)
    amenities = list(storage.all(Amenity).values())
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)




@app.teardown_appcontext
def teardowndb(exception):
    """it ends the sqlalchemy session"""
    storage.close()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
