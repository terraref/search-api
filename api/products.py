import yaml
import requests

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
Products are the available data products to search. Currently hard-coded.
"""

bety_products = config["bety_products"]
clowder_products = config["clowder_products"]

def search():
    full_products = bety_products + clowder_products
    return full_products

def get():
    full_products = bety_products + clowder_products
    return full_products



