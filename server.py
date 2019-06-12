#!/usr/bin/env python

import logging

import connexion
from searchresolver import SearchResolver
from flask_cors import CORS, cross_origin


def token_auth(token, required_scopes):
    print("token_auth")
    return {'user': 'admin'}


def bearer_auth(token):
    print("bearer_auth")
    return {'user': 'admin'}


def basic_auth(username, password, required_scopes=None):
    print("basic_auth")
    return {'user': 'admin'}


if __name__ == '__main__':
    debug = False

    if debug:
        logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.INFO)

    app = connexion.FlaskApp(__name__, debug=debug)

    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    app.add_api('search.yaml',
                arguments={'title': 'TERRA advanced search api'},
                resolver=SearchResolver('api'),
                resolver_error=501)

    # app.run(port=5000, host=None, server='flask', debug=debug, use_reloader=False)
    app.run(port=5000, host=None, server='flask', debug=debug)
