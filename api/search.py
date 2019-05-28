import json
import helper


def search(season=None, experimentId=None, cultivarId=None, treatmendId=None, pageSize=None, page=None):
    # load all the data
    data = {"leadPersonDbId": "person1", "leadPersonName": "Name Nameson"}
    count = 1
    return helper.create_result({"data": data}, count, pageSize, page)

def get(season=None, experimentId=None, cultivarId=None, treatmendId=None, pageSize=None, page=None):
    return "this is the page"