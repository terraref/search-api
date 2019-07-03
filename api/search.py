import json

data = json.load(open('dummy-data/searchResults.json', 'r'))
geotiff_data = json.load(open('dummy-data/geotiffSearchResults.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    if product:
        if product == 'IR GeoTIFF':
            return geotiff_data
        elif product == 'Canopy Cover':
            return product
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "this is the page"