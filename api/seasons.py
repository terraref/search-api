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
                        "seasonDbId": str(seas['seasonDbId']),
                        "studies": [{
                            "studyname": str(study["studyName"]),
                            "studyDbId": str(study["studyDbId"])
                        }],
                        "startdate": start,
                        "enddate": end
                    }
                else:
                    distinct[start]["studies"].append({
                        "studyname": str(study["studyName"]),
                        "studyDbId": str(study["studyDbId"])
                    })

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

        s4 = {"seasonname": "Season 4",
            "seasonDbId": "a8317fa6b59bfa8cfe29004423f5613b",
            "studies": [{
                "studyname": "Border Plots",
                "studyDbId": "6000000017"
            },{
                "studyname": "All BAP Accessions",
                "studyDbId": "6000000010"
            }],
            "startdate": "2017-04-13",
            "enddate": "2017-09-21"}

        s6 = {"seasonname": "Season 6",
            "seasonDbId": "bb29dbf643e6b94010793f814701d0dd",
            "studies": [{
                "studyname": "Sorghum BAP",
                "studyDbId": "6000000034"
            }],
            "startdate": "2018-04-20",
            "enddate": "2018-08-02"}

        if season == "MAC Season 4":
            return [s4]
        elif season == "MAC Season 6":
            return [s6]
        else:
            return [s4, s6]

def get(season=None, experimentId=None, germplasmId=None, treatmentId=None, pageSize=None, page=None):
    return "Not implemented."

# Get seasonDbId given a season name
def _getSeasonId(season):
    url = "%s/seasons?season=%s" % (config["brapi_api"], season)
    try:
        r = requests.get(url).json()['result']['data']
        if len(r) > 0:
            return r[0]['seasonDbId']
        else:
            return None
    except:
        print("Error fetching seasonDbId from BrAPI for %s." % season)
        return None

# Get a dict of studyName:studyDbId
def _getStudyIds(season=None):
    results = {}

    seasons = search(season)
    for i in range(len(seasons)):
        for stud in seasons[i]["studies"]:
            results[stud["studyname"]] = {
                "studyDbId": stud["studyDbId"],
                "seasonname": seasons[i]["seasonname"]
            }

    return results
