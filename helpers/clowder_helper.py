import requests
import os

terra_clowder_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'

terra_clowder_dataset_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'


def get_dataset_link(product, date):
    results = []

    dataset_name = product + ' - ' + date
    dataset_name = dataset_name.replace(' ', '%20')
    url = terra_clowder_url + '?' + dataset_name
    url = url+'&key='+os.environ['CLOWDER_KEY']
    dataset = requests.get(url)
    ds = dataset.json()

    if type(ds) == list:
        for each in ds:
            current_id = each['id']
            current_name = each['name']
            current_dataset_url = terra_clowder_dataset_url+'/'+current_id
            download_link = terra_clowder_url+'/'+current_id
            result = {"name": current_name, "view": current_dataset_url, "download": download_link}
            results.append(result)
        return results


    if dataset.raise_for_status == 200:
        print('got a dataset')
    return results