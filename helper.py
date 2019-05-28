#from bety_brapi import database

import database
import math

DEFAULT_PAGE_SIZE = 1000

def query_count(query, params=None):
    """
    Executes the query and returns the count of the number rows that would be returned
    by this query. This will not actually return the results.
    :param query: the actual sql parameterized query to execute.
    :param params: the parameters to be used with the query
    :return: the total number of elements returned by the query. This is not limited
             by a page and/or pageSize
    """
    count_query = 'SELECT COUNT(*) FROM (' + query + ') AS a;'
    response = database.get_engine().execute(count_query, params)
    count = response.fetchone()
    response.close()
    return count[0]


def query_result(query, params=None, pageSize=None, page=None):
    """
    Actually execute the query. This will use the pageSize and page values to limit the number
    of results that re returned. The query is assumed to be a parameterized query, and params
    contains the actual values. For example the get a specific user we can use:
    SELECT * FROM user WHERE id=%s and add a value to params that will be safely inserted in
    the actual query
    :param query: the actual sql parameterized query to execute.
    :param params: the parameters to be used with the query
    :param pageSize: the maximum number of elements to be returned (adds a LIMIT pageSize)
    :param page: which page to return, 0 based. (adds a OFFSET page * pageSize)
    :return: the results of the query.
    """
    if not params:
        params = []
    if not pageSize:
        pageSize = DEFAULT_PAGE_SIZE
    query += ' LIMIT %s'
    params.append(pageSize)
    if page:
        query += ' OFFSET %s'
        params.append(pageSize * page)
    return database.get_engine().execute(query, params)


def create_result(data, rowCount, pageSize=None, page=None):
    """
    Given the data, rowCount (total number of records), and optionally the pageSize and page
    this function will return a brapi paged result.
    :param data: the actual data to be returned
    :param rowCount: the total number of rows in the database
    :param pageSize: the number of results to return
    :param page: the page in the database with the results
    :return: the dict that can be returned as the brapi result
    """
    if not pageSize:
        pageSize = DEFAULT_PAGE_SIZE
    if not page:
        page = 0
    body = {
        "metadata": {
            "datafiles": [],
            "pagination": {
                "currentPage": page,
                "pageSize": pageSize,
                "totalCount": rowCount,
                "totalPages": math.ceil(rowCount / pageSize)
            },
            "status": []
        },
        "result": data
    }
    return body
