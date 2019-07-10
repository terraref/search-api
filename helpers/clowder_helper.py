import requests

terra_clowder_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets?'

def get_dataset_link(product, date):
    dataset_name = product + ' - ' + date
    dataset_name = dataset_name.replace(' ', '%20')
    url = terra_clowder_url + dataset_name
    return url