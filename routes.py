"""
Author: Aishwarya Sharma
"""
import os

from bottle import get, post, route, static_file
from jinja2 import Environment, FileSystemLoader
import Logger

import json


# Specifies that our templates are located in the "templates" folder inside
path_to_templates = os.path.dirname(os.path.abspath(__file__)) + "/templates"
template_env = Environment(
    loader=FileSystemLoader(path_to_templates, followlinks=True))


# Setting the Logger
log = Logger.get_logger()


# Static Routes
@route('/static/<filename:path>')
def serve_static_files(filename):
    return static_file(filename=filename, root="./static")


# Main Site routes
@route("/")
@route("/index")
@route("/home")
def index():
    app_data = []
    try:
        with open("AppData.json") as data:
            app_data = json.load(data)
    except FileNotFoundError:
        log.error("Could not find file AppData.json")
    except:
        log.error("Had an error when trying to read AppData.json")
    return template_env.get_template("index.html").render(apps=app_data)


# To do List Routes
@route("/todo")
def todo_index():
    pass
