#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
""" Flask app for API"""
app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """ closes the current session"""
    storage.close()

if __name__ == "__main__":
    # threaded is so app can take multiple requests at once
    host = getenv(AIRBNB_API_HOST, "0.0.0.0")
    port = getenv(AIRBNB_API_PORT, "5000")
    app.run(host=host, port=port, debug=True, threaded=True)