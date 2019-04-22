import os, thread, json, collections
import logging, logging.config, logstash
import time
import pandas as pd
import numpy as np
import datetime
import psycopg2
import re
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, DateField, SelectMultipleField, widgets
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import terrautils

config = {}


# FLASK COMPONENTS ----------------------------
def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/test')
    def test():
        return 'this is only a test, route does nothing'

    @app.route('/seasons')
    def seasons():
        season_numbers = [4,6]
        seasons = []
        for each in season_numbers:
            season = 'Season ' + str(each)
            seasons.append(season)
        return str(seasons)

    @app.route('/products/<int:season>')
    def products(season):
        return 'not implemented'

    return app


if __name__ == '__main__':
    logger = logging.getLogger('search-api')

    apiIP = os.getenv('COUNTER_API_IP', "0.0.0.0")
    apiPort = os.getenv('COUNTER_API_PORT', "5454")
    app = create_app()
    logger.info("*** API now listening on %s:%s ***" % (apiIP, apiPort))
    app.run(host=apiIP, port=apiPort)
