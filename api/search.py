import json
from helpers import bety_helper, clowder_helper
import os
from flask import Flask, Response, abort
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from io import StringIO
from werkzeug.exceptions import BadRequest

data = json.load(open('dummy-data/searchResults.json', 'r'))
geotiff_data = json.load(open('dummy-data/geotiffSearchResults.json', 'r'))
canopycover_data = json.load(open('dummy-data/canopyCoverSearchResults.json', 'r'))

bety_products = ['Canopy Cover', 'Canopy Height', 'Mean Temperature']
clowder_products = ['RGB GeoTIFFs', 'Thermal IR GeoTIFFs', 'Laser Scanner 3D LAS',
                    'Full Field RGB Images', 'Full Field IR Images']


def search(season=None, date=None, start_date=None, end_date=None, experimentId=None, germplasmName=None, treatmendId=None, product=None, pageSize=None, page=None):
    if season:
        pass
    else:
        season = '6'

    if product:
        if str(product) in clowder_products:
            if date:

                result = clowder_helper.get_clowder_result_single_date(product, date)
                return {"clowder": result, "bety": []}
            elif start_date and end_date:
                result = clowder_helper.get_clowder_result_date_range(product, start_date, end_date)
                return {"clowder": result, "bety": []}
            else:
                return abort(400, "Need start_date and end_date for product : " + product)
        elif str(product) in bety_products:
            #result = bety_helper.get_trait_sitename('Season ' + season, trait=product, bety_key=os.environ['BETY_KEY'])
            result = bety_helper.get_bety_search_result('Season ' + season, trait=product)
            return {"clowder": [], "bety": [result]}
        else:
            return abort(400, "No product matches " + product)
    else:
        if not (experimentId or germplasmName or treatmendId):
            return abort(400, "Correct search parameters not provided")
        return {"clowder": [], "bety": []}

def get(season=None, date=None, start_date=None, end_date=None, experimentId=None, germplasmName=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "this is the page"