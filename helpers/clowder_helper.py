import requests
import os

terra_clowder_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'

def get_dataset_link(product, date):
    dataset_name = product + ' - ' + date
    dataset_name = dataset_name.replace(' ', '%20')
    url = terra_clowder_url + '?' + dataset_name
    url = url+'&key='+os.environ['CLOWDER_KEY']
    dataset = requests.get(url)
    ds = dataset.json()

    if type(ds) == list:
        results = []
        for each in ds:
            current_id = each['id']
            current_dataset_url = terra_clowder_url+'/'+current_id
            results.append(current_dataset_url)
        return {"datasets": results}


    if dataset.raise_for_status == 200:
        print('got a dataset')
    return url