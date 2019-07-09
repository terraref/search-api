import json
from helpers import bety_helper
import os

data = json.load(open('dummy-data/searchResults.json', 'r'))
geotiff_data = json.load(open('dummy-data/geotiffSearchResults.json', 'r'))
canopycover_data = json.load(open('dummy-data/canopyCoverSearchResults.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    if product:
        if product == 'IR GeoTIFF':
            return geotiff_data
        elif product == 'Canopy Cover':
            if season:
                result = bety_helper.get_canopy_cover_sitename(season,bety_key=os.environ['BETY_KEY'])
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "this is the page"