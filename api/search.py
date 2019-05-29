import json

data = json.load(open('data/searchResults.json', 'r'))

def search(season=None, experimentId=None, cultivarId=None, treatmendId=None, pageSize=None, page=None):
    return data

def get(season=None, experimentId=None, cultivarId=None, treatmendId=None, pageSize=None, page=None):
    return "this is the page"