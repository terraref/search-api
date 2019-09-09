import yaml
from flask import Flask, Response, abort
from helpers import bety_helper, clowder_helper, search_helper
from api.cultivars import get_sites_by_cultivar

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

bety_products = config["bety_products"]
clowder_products = config["clowder_products"]

"""
General search endpoint for searching using multiple parameters.
"""

def search(season=None, date=None, start_date=None, end_date=None, experimentId=None, germplasmName=None, treatmentId=None, product=None, sitename=None,pageSize=None, page=None):
    if season is None: season = '6'
    if germplasmName and not product:
        product = 'RGB GeoTIFFs'

    if product:
        # ----- SEARCH CLOWDER ------
        if str(product) in clowder_products:
            if date:
                start_date = date
                end_date = date
            elif start_date is None or end_date is None:
                return abort(400, "Need start_date and end_date for product: " + product)

            if germplasmName:
                # Get the plot names for the requested cultivar
                sites = get_sites_by_cultivar(germplasmName, "MAC Season %s" % season)
            elif sitename:
                sites = [sitename]
            else:
                sites = []

            # Get datasets filtered by this plot (and optionally date)
            results = clowder_helper.search_products_cached(product, start_date, end_date, sites)
            return results

        # ----- SEARCH BETYDB ------
        elif str(product) in bety_products:
            #result = bety_helper.get_trait_sitename('Season ' + season, trait=product, bety_key=os.environ['BETY_KEY'])
            result = bety_helper.get_bety_search_result('Season ' + season, trait=product)
            return {"clowder": [], "bety": [result]}
        else:
            return abort(400, "No product matches " + product)

    else:
        if not (experimentId or germplasmName or treatmentId):
            return abort(400, "Correct search parameters not provided")
        return {"clowder": [], "bety": []}

def get(season=None, date=None, start_date=None, end_date=None, experimentId=None, germplasmName=None, treatmendId=None, product=None, pageSize=None, page=None):
    return "Not implemented."
