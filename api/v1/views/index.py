#!/usr/bin/python3
from api.v1.views import app_views
""" index file in API """

app = Flask(__name__)

@app_views.route("/status")
def status():
    """ returns a JSON status"""
    response = {
        "status": "OK"
    }
    return response
