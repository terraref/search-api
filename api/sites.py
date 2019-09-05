import yaml
import requests

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
Sites are the experimental plot names, using BrAPI's /observationunits endpoint.
"""

def search(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    url = "%s/observationunits" % config["brapi_api"]
    try:
        results = []
        r = requests.get(url).json()['result']['data']

        # Get plot names & filter to distinct
        for ou in r:
            results.append(ou['observationUnitName'])

        results.sort()
        return list(set(results))

    except:
        print("Error fetching sites from BrAPI; using default.")
        if season is None: season = "MAC Season 6"

        results = []
        for r in range(54):
            for c in range(16):
                results.append("%s Range %s Column %s" % (season, r+1, c+1))

        return results

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "Not implemented."