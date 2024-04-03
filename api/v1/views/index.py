#!/usr/bin/python3
""" index file , returns a JSON response """

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", strict_slashes="False")
def return_status():
    """ returns a JSON status"""
    response = {
        "status": "OK"
    }
    return response

@app_views.route("/api/v1/stats", strict_slashes="False")
def stats():
    """ returns the number of each object by type """
    # create dict of objects, 'display name : object'
    object_list = {"amenities": Amenity, "cities": City, "places": Place,
                   "reviews": Review, "states": State, "users": User}
    
    #create dict of stats
    current_stats = {}
    # loop through each:
    for name, obj in obj.items():
        #for each, call storage.count(pass_object_here)
        object_stat = storage.count(obj)
        # return value is set as value to in key value pair and assigned to dict
        current_stats[name] = object_stat
        # return jsonified version ( like that should work but just to be sure)
        return jsonify(current_stats)

