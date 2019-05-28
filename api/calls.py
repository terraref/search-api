import helper

VERSIONS_1_2 = ["1.2"]
VERSIONS_1_3 = ["1.3"]
VERSIONS_ALL = VERSIONS_1_2 + VERSIONS_1_3
VERSIONS_LATEST = VERSIONS_1_3


def search(datatype=None, dataType=None, pageSize=None, page=None):
    """
    Return a list of all calls that are implemented
    """

    # create the full list of all calls implemented.
    data = [
        calls_get_helper('calls'),
        calls_get_helper('search')
    ]

    # filter on datatype
    if dataType:
        data = [d for d in data if datatype in d['dataTypes']]
    elif datatype:
        data = [d for d in data if datatype in d['dataTypes']]

    # total number of rows
    count = len(data)

    # add a limit
    if not pageSize:
        pageSize = len(data)
    if not page:
        page = 0
    data = data[page * pageSize:(page + 1) * pageSize]

    # return the resulting data
    return helper.create_result({"data": data}, count, pageSize, page)


def calls_get_helper(api_call, dataTypes=None, methods=None, versions=None):
    """
    Helper function to return a brapi call information.
    """
    if not dataTypes:
        dataTypes = ["application/json"]
    if not methods:
        methods = ['GET']
    if not versions:
        versions = VERSIONS_ALL
    return {
        "call": api_call,
        "dataTypes": dataTypes,
        "methods": methods,
        "versions": versions
    }
