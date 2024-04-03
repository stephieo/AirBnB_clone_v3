#!/usr/bin/python3
""" Flask app for API of Airbnb"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

# FIXME  Import statement not working for sbling packages

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """ closes the current session"""
    models.storage.close()

@app.errorhandler(404)
def page_not_found():
    """ returns a JSON response for 404 errors"""
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    import sys
    print(sys.path)
    # threaded is so app can take multiple requests at once
    host = getenv(AIRBNB_API_HOST, "0.0.0.0")
    port = getenv(AIRBNB_API_PORT, "5000")
    app.run(host=host, port=port, debug=True, threaded=True)
