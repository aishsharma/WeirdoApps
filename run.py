"""
Author: Aishwarya Sharma
"""

from bottle import run
import cherrypy
import Logger
from routes import *


if __name__ == '__main__':
    # starting the server
    log = Logger.get_logger()
    log.info("Starting Server...")
    run(server='cherrypy', host="localhost", port=8080, reloader=True, debug=True)
