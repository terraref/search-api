import requests
import os
import datetime
import csv
import yaml

config = yaml.load(open("config.yaml", 'r'), Loader=yaml.FullLoader)
clowder_url = config["clowder_url"]
max_results = config["max_results"]

"""
Helper functions for searching Clowder or cached files.
"""

def search_products(product, start_date, end_date, sites=[]):
    return search_products_cached(product, start_date, end_date, sites)

    # TODO: Provide 'live' alternative off Clowder API once Elasticsearch is faster & more stable
    results = []
    current_search_url = terra_clowder_search_url+'name:'+dataset_name+' name:'+date+'&key='+os.environ['CLOWDER_KEY']
    print('getting results for url : ', current_search_url)

    r = requests.get(current_search_url)
    seach_results = r.json()

    datasets_found = seach_results['datasets']
    collections_found = seach_results['collections']

    if len(datasets_found) == 0 and len(collections_found) == 0:
        print('nothing found, using dummy placeholder data')
        datasets_found = sample_data

    for each in datasets_found:
        current_id = each['id']
        current_name = each['name']
        current_dataset_url = clapi_dataset + '/' + current_id
        download_link = clapi_datasets + '/' + current_id
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

def search_products_cached(product, start_date, end_date, sites=[]):
    results = []

    start_month = start_date[:7]
    end_month = end_date[:7]

    # Iterate over cache files, e.g. "RGB GeoTIFFs - 2018-06.csv"
    cache_dir = os.path.join(os.getcwd(), 'data')
    for cache_file in os.listdir(cache_dir):
        lookup_product = "Full Field" if product == "Full Field Images" else product
        if cache_file.startswith(lookup_product):
            cache_month = cache_file.split(" - ")[1].replace(".csv", "")
            if start_month <= cache_month <= end_month:
                cf = open(os.path.join(cache_dir, cache_file), 'r')
                rows = csv.reader(cf)
                for row in rows:
                    ds_id = row[0]
                    ds_name = row[1]
                    ds_prod = ds_name.split(" - ")[0]
                    ds_date = ds_name.split(" - ")[1].split('__')[0]
                    ds_plot = row[2]

                    if (len(sites) == 0 or ds_plot in sites) and ds_prod == lookup_product and start_date <= ds_date <= end_date:
                        results.append({
                            "name": ds_name,
                            "view": "%s/datasets/%s" % (clowder_url, ds_id),
                            "download": "%s/api/datasets/%s/download" % (clowder_url, ds_id)
                        })

                        if len(results) >= max_results:
                            return results

    return results

def get_date_range(start_date, end_date):
    start_date_object =  datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date_object = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    num_of_days = (end_date_object - start_date_object).days
    daterange = [start_date_object + datetime.timedelta(days=x) for x in range(0, num_of_days+1)]

    result = []
    for each in daterange:
        dt = str(each)
        result.append(dt[:dt.index(' ')])

    return result
