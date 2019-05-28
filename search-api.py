import os, thread, json, collections
import logging, logging.config, logstash
logging.basicConfig()
import time
import pandas as pd
import numpy as np
import datetime
import psycopg2
import re
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from flask import jsonify

config = {}


def get_season_start_date(season):
    return '2018-04-01'


def get_site_boundaries_date(selected_date):
    with open('sites_boundaries.json', 'r') as f:
        sites_boundaries = json.load(f)
    return sites_boundaries


# FLASK COMPONENTS ----------------------------
def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/')
    def default():
        logger.info("Index page being displayed")
        return render_template('index.html')

    @app.route('/index')
    def index():
        logger.info("Index page being displayed")
        return render_template('index.html')

    @app.route('/seasons')
    def seasons():
        season_numbers = [4,6]
        seasons = []
        for each in season_numbers:
            season = 'Season ' + str(each)
            seasons.append(season)
        return jsonify(seasons)

    @app.route('/plotmap/<int:season>')
    def plotmap(season):
        logger.info("plot map for seasons %s " % season)
        start_date = get_season_start_date(season)
        sites_boundaries = get_site_boundaries_date(start_date)
        return jsonify(sites_boundaries)

    @app.route('/products/<int:season>')
    def products(season):
        logger.info("season queried is %s " % season)
        products = []
        if season == 4 or season == 6:
            products = ['RGB GeoTIFFs',
                    'Thermal IR GeoTIFFs',
                    'Laser Scanner 3D LAS',
                    'Canopy Cover',
                    'Mean Temperature',
                    'Canopy Height'
                    ]
        return jsonify(products)

    return app

def main():
    apiIP = os.getenv('COUNTER_API_IP', "0.0.0.0")
    apiPort = os.getenv('COUNTER_API_PORT', "5454")
    search_app = create_app()
    logger.info("*** API now listening on %s:%s ***" % (apiIP, apiPort))
    search_app.run(host=apiIP, port=apiPort)

if __name__ == '__main__':
    logger = logging.getLogger('search-api')
    logger.setLevel('INFO')

    main()

