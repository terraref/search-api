import json

data = json.load(open('data/plots.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    return "this is the page"