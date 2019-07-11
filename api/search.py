import json
from helpers import bety_helper, clowder_helper
import os
from flask import Flask, Response
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from io import StringIO

data = json.load(open('dummy-data/searchResults.json', 'r'))
geotiff_data = json.load(open('dummy-data/geotiffSearchResults.json', 'r'))
canopycover_data = json.load(open('dummy-data/canopyCoverSearchResults.json', 'r'))

bety_products = ['Canopy Cover', 'Canopy Height', 'Mean Temperature']
clowder_products = ['RGB GeoTIFFs', 'Thermal IR GeoTIFFs', 'Laser Scanner 3D LAS',
                    'Full Field RGB Images', 'Full Field IR Images']


def search(season=None, date=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    if season:
        pass
    else:
        season = '6'


    if product:
        if str(product) in clowder_products:
            if date:
                result = clowder_helper.get_dataset_link(product, date)
                return result
        elif str(product) in bety_products:
            result = bety_helper.get_trait_sitename('Season ' + season, trait=product, bety_key=os.environ['BETY_KEY'])
            return result
            # return send_file(result,
            #                  mimetype='text/csv',
            #                  attachment_filename=result,
            #                  as_attachment=True)

    return data

def get(season=None, date=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "this is the page"