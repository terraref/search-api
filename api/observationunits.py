import yaml
import requests

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
Sites are the experimental plot names, using BrAPI's /observationunits endpoint.
"""

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    return "Not implemented."