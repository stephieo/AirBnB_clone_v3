#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import *
""" holds the blueprints"""

app_views = Blueprint("views", __name__, url_prefix='/api/v1')




