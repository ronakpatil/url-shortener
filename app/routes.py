import logging
import flask
from flask import request
from shortener import Shorteners
LOGGER = logging.getLogger('url_shortener')
APP = flask.Flask(__name__)

@APP.route('/shorturl', methods=['GET'])
def home():
    if 'actualurl' in request.args:
        LOGGER.info('actual url found %s', str(request.args['actualurl']))
        short = Shorteners(str(request.args['actualurl']))
        return short.bitly_shortener()
    return "Error: No url field provided. Please specify an url"

def server():
    APP.run()
