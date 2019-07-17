import requests
import os
import datetime
import json

terra_clowder_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'

terra_clowder_dataset_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'

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
    dataset_name = product + ' - ' + date
    dataset_name = dataset_name.replace(' ', '%20')
    url = terra_clowder_url + '?title=' + dataset_name
    url = url+'&key='+os.environ['CLOWDER_KEY']
    print('getting results for url : ', url)

    if os.environ['TEST'] == 'True':
        ds = sample_data
    else:
        dataset_data = requests.get(url)
        ds = dataset_data.json()

    if type(ds) == list:
        for each in ds:
            current_id = each['id']
            current_name = each['name']
            current_dataset_url = terra_clowder_dataset_url+'/'+current_id
            download_link = terra_clowder_url+'/'+current_id
            result = {"name": current_name, "view": current_dataset_url, "download": download_link}
            results.append(result)
        return results

    return results