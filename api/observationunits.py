import yaml
import requests
from api.seasons import _getStudyIds

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
ObservationUnits are the experimental plot data, using BrAPI's /studies/layout endpoint.
"""

def search(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    studyIds = _getStudyIds(season)

    results = []
    for studyname in studyIds:
        studyDbId = studyIds[studyname]["studyDbId"]

        try:
            url = "%s/studies/%s/layouts" % (config["brapi_api"], studyDbId)
            r = requests.get(url).json()['result']['data']

            for plot in r:
                results.append({
                    "experiment": studyname,
                    "season": studyIds[studyname]["seasonname"],
                    "observationunitname": plot["observationUnitName"],
                    # TODO: Do we add XY location from sites table to observationunits BrAPI endpoint?
                    "coordinates": []
                })
        except:
            print("Error getting plots from BrAPI for %s." % studyDbId)

    return results
    """
        return [
            {
                "experiment": "Drought Tolerance",
                "season": "Season 0",
                "observationunitname": "MAC Field Scanner Season 1 Range 1 Column 1",
                "coordinates": [33.0, -111.0]

            },
            {
                "experiment": "Cover Crop",
                "season": "Season 0",
                "observationunitname": "MAC Field Scanner Season 1 Range 2 Column 1",
                "coordinates": [33.1, -111.1]
            }
        ]
    """

def get(season=None, experimentId=None, germplasmId=None, treatmendId=None, pageSize=None, page=None):
    return "Not implemented."
