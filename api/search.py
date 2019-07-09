import json
from helpers import bety_helper
import os
from flask import Flask, Response
from flask import Flask, render_template, send_file, request, url_for, redirect, make_response
from io import StringIO

data = json.load(open('dummy-data/searchResults.json', 'r'))
geotiff_data = json.load(open('dummy-data/geotiffSearchResults.json', 'r'))
canopycover_data = json.load(open('dummy-data/canopyCoverSearchResults.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    if product:
        if product == 'IR GeoTIFF':
            return geotiff_data
        elif product == 'Canopy Cover':
            if season:
                if os.environ['BETY_KEY'] == '':
                    return send_file('Season 6 canopy_cover.csv',
                                     mimetype='text/csv',
                                     attachment_filename='Season 6 canopy_cover.csv',
                                     as_attachment=True)
                else:
                    result = bety_helper.get_canopy_cover_sitename('Season ' + season, bety_key=os.environ['BETY_KEY'])
                    return send_file(result,
                                     mimetype='text/csv',
                                     attachment_filename=result,
                                     as_attachment=True)

    return data

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "this is the page"