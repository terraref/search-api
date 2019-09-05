import yaml
import requests

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)

"""
Seasons are derived from BETYdb's experiments table, using BrAPI's /studies endpoint.
"""

def search(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    # Use /studies endpoint because /seasons doesn't include start & end date
    url = "%s/studies" % config["brapi_api"]
    try:
        distinct = {}
        r = requests.get(url).json()['result']['data']

        # Get distinct season names
        for study in r:
            start = str(study['startDate'])
            end = str(study['endDate'])
            for seas in study['seasons']:
                seas_name = str(seas['season'])
                if start not in distinct:
                    distinct[start] = {
                        "seasonname": seas_name,
                        "startdate": start,
                        "enddate": end
                    }

        # Filter results if necessary
        results = []
        for start in distinct:
            if config["filter_seasons"]:
                seas_name = distinct[start]['seasonname']
                if seas_name.endswith("Season 4") or seas_name.endswith("Season 6"):
                    results.append(distinct[start])
            else:
                results.append(distinct[start])

        return results

    except:
        print("Error fetching seasons from BrAPI; using default.")
        return [
            {"seasonname": "Season 4", "startdate": "2017-04-13", "enddate": "2017-09-21"},
            {"seasonname": "Season 6", "startdate": "2018-04-20", "enddate": "2018-08-02"}
        ]

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "Not implemented."
