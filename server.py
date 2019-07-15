#!/usr/bin/env python

import logging, logging.config

logging.basicConfig()
import os
import connexion
from searchresolver import SearchResolver
from flask import Flask
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from flask import jsonify
from flask_cors import CORS, cross_origin
from helpers import bety_helper
import max_bety_sample


def token_auth(token, required_scopes):
    print("token_auth")
    return {'user': 'admin'}


def bearer_auth(token):
    print("bearer_auth")
    return {'user': 'admin'}


def basic_auth(username, password, required_scopes=None):
    print("basic_auth")
    return {'user': 'admin'}


def create_app():
    app = connexion.FlaskApp(__name__, debug=debug)

    # app.add_api('search.yaml',
    #             arguments={'title': 'TERRA advanced search api'},
    #             resolver=SearchResolver('api'),
    #             resolver_error=501)
    CORS(app.app)

    @app.app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def default():
        return "this is the defaultpage"

    @app.route('/download_bety_file/<filename>')
    def download_bety_file(filename):
        file_exists = os.path.isfile(filename)
        if file_exists:
            return send_file(filename,
                             mimetype='text/csv',
                             attachment_filename=filename,
                             as_attachment=True)
        else:
            result = bety_helper.generate_bety_csv_from_filename(filename)
            return send_file(result,
                             mimetype='text/csv',
                             attachment_filename=filename,
                             as_attachment=True)
    return app


def main():
    #os.environ['BETY_KEY'] = max_bety_sample.bety_key
    apiIP = os.getenv('COUNTER_API_IP', "0.0.0.0")
    apiPort = os.getenv('COUNTER_API_PORT', "5454")
    logger.info("*** API now listening on %s:%s ***" % (apiIP, apiPort))
    search_app = create_app()
    search_app.add_api('search.yaml',
                       arguments={'title': 'TERRA advanced search api'},
                       resolver=SearchResolver('api'),
                       resolver_error=501)
    search_app.run(port=5454, host=None, server='flask', debug=debug)


if __name__ == '__main__':
    debug = False
    logger = logging.getLogger('search-api')
    logger.setLevel('INFO')
    if debug:
        logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.INFO)

    main()
