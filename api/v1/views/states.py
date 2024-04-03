#!/usr/bin/python3
""" view for State objects, handles all default"""
from models import storage
from api.v1.views import 
from flask import abort, make_response, request
from models.state import State

@app_views.route("/get/api/v1/states", methods=['GET'])
def show_states():
    """returns the list of all state objects"""
    #retriev a list of all the state objects from storage
    # cycle through each to apply to_dict() 
    # add each result to list
    state_objects = storage.all()
    state_obj_list = [obj.to_dict() for obj in state_objects]
    return jsonify(state_obj_list)


@app_views.route("/api/v1/states/<state_id>", methods=['GET'])
def single_state(state_id):
    """ retrieves a state based on id"""
    # retrieve dictionary of all state objects with .all()
    # loop though?
    # if id == obj['id']
        # return obj
    # else  call abort(404)
    state_objects = storage.all()
    for state in state_objects:
        if state_id == state['id']:
            return jsonify(state.to_dict())
    abort(404)

@app_views.route("/api/v1/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """ deletes a state object """
    state_objects = storage.all()
    for state in state_objects:
        if state_id == state['id']:
            storage.delete(state)
            return make_response(jsonify({}), 200)
    abort(404)

@app_views.route("/api/v1/states", methods=['POST'])
def create_state():
    """ creates a state object """
    # parse json from incomin request 
    req_body = request.get_json
    # validation
    if req_body == None:
        abort(400, "NOT A JSON")
    elif name not in req_body:
        abort(400, "Missing  name")
    else:
        # create object from dict & call the new() method on the object
        new_state = State(**req_body)
        storage.new(new_state)
        # save to database
        storage.save()
        # return response (new state) with 201 code
        return make_response(jsonify(new_state.to_dict()), 201)

@app_views.route("/api/v1/states/<state_id>", methods=['PUT'])
def update_state(state_id):
    """ updates a state object"""

    old_state = storage.get(State, state_id)
    if state is None:
        abort(404)
    # parse json from incomin request 
    req_body = request.get_json
    if req_body == None:
        abort(400, "NOT A JSON")
    # locate the state object
    state_objects = storage.all()
    
    for key, value in old_state.items():
        if key not in ['id',' created_at', 'updated_at']:
            setattr(old_state, key, value)
    old_state.save()
    return make_response(jsonify(old_state.to_dict), 200)

# INCOMPLETE 


    


