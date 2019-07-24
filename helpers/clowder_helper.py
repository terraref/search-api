import requests
import os
import datetime
import json

terra_clowder_datasets_api_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'
terra_clowder_dataset_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'

terra_clowder_collections_api_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'
terra_clowder_collection_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'

terra_clowder_search_url = 'https://terraref.ncsa.illinois.edu/clowder/api/search?query='

sample_data = json.load(open('clowder_dataset_search_results.json', 'r'))


def datetime_to_str_date(dt):
    dt = str(dt)
    return dt[:dt.index(' ')]


def get_date_range(start_date, end_date):
    start_date_object =  datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date_object = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    num_of_days = (end_date_object - start_date_object).days
    daterange = [start_date_object + datetime.timedelta(days=x) for x in range(0, num_of_days+1)]

    result = []
    for each in daterange:
        current = datetime_to_str_date(each)
        result.append(current)

    return result


def get_clowder_result_date_range(product, start_date, end_date):
    results = []
    date_range = get_date_range(start_date, end_date)

    for each_date in date_range:
        results_for_date = get_clowder_result_single_date(product, each_date)
        results.extend(results_for_date)
    return results


def get_clowder_result_single_date(product, date):
    results = []
    current_search_url = terra_clowder_search_url+'name:'+product+' name:'+date+'&key='+os.environ['CLOWDER_KEY']
    print('getting results for url : ', current_search_url)

    if os.environ['TEST'] == 'True':
        for each in sample_data:
            current_id = each['id']
            current_name = each['name']
            current_dataset_url = terra_clowder_dataset_url + '/' + current_id
            download_link = terra_clowder_datasets_api_url + '/' + current_id
            result = {"name": current_name, "view": current_dataset_url, "download": download_link}
            results.append(result)
        return results
    else:
        r = requests.get(current_search_url)
        seach_results = r.json()

    datasets_found = seach_results['datasets']
    collections_found = seach_results['collections']

    if len(datasets_found) == 0 and len(collections_found) == 0:
        datasets_found = sample_data

    for each in datasets_found:
        current_id = each['id']
        current_name = each['name']
        current_dataset_url = terra_clowder_dataset_url + '/' + current_id
        download_link = terra_clowder_datasets_api_url + '/' + current_id
        result = {"name": current_name, "view": current_dataset_url, "download": download_link}
        results.append(result)

    for each in collections_found:
        current_id = each['id']
        current_name = each['name']
        current_dataset_url = terra_clowder_collection_url + '/' + current_id
        download_link = terra_clowder_collections_api_url + '/' + current_id
        result = {"name": current_name, "view": current_dataset_url, "download": download_link}
        results.append(result)
        return results
    return results
