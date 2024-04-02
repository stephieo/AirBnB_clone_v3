#!/usr/bin/python3
""" index file , returns a JSON response """

from api.v1.views import app_views


@app_views.route("/status")
def status():
    """ returns a JSON status"""
    response = {
        "status": "OK"
    }
    return response
