import json

data = json.load(open('data/cultivars_season6.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "this is the page"