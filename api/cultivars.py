import json

data = json.load(open('dummy-data/cultivars.json', 'r'))

def search(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return data

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "this is the page"