import requests
import os
import datetime
import json
import csv

terra_clowder_datasets_api_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'
terra_clowder_dataset_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'

terra_clowder_dataset_metadata_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets/current_id/metadata.jsonld'

terra_clowder_dataset_title_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets?title='

terra_clowder_collections_api_url = 'https://terraref.ncsa.illinois.edu/clowder/api/datasets'
terra_clowder_collection_url = 'https://terraref.ncsa.illinois.edu/clowder/datasets'

terra_clowder_search_url = 'https://terraref.ncsa.illinois.edu/clowder/api/search?query='

sample_data = json.load(open('clowder_dataset_search_results.json', 'r'))

cultivars_season_4_csv = 'cultivars_s4_2017.csv'
cultivars_season_6_csv = 'cultivars_s6_2018.csv'

clowder_products_dataset_name_map = {
    'RGB GeoTIFFs' : 'rgb_geotiff',
    'Thermal IR GeoTIFFs':'ir_geotiff',
    'Laser Scanner 3D LAS':'laser3d_las',
    'Full Field RGB Images':'rgb_fullfield',
    'Full Field IR Images':'ir_fullfield'
}


def get_sitename_from_ds_metadata(ds_metadata):
    sitename = ''
    content = ds_metadata['content']
    site_metadata = content['site_metadata']
    for entry in site_metadata:
        if type(entry) == dict:
            if 'sitename' in entry:
                sitename = entry['sitename']
    return sitename


def get_cultivar_sitename_map(season):

    if season == 'Season 6':
        cultivar_site_map = {}
        with open(cultivars_season_6_csv, 'r') as f:
            reader = csv.reader(f)
            line_count = 0
            for row in reader:
                if row[0] == 'sitename':
                    pass
                else:
                    current_sitename = row[0]
                    current_cultivar = row[1]
                    if current_cultivar in cultivar_site_map:
                        old_value = cultivar_site_map[current_cultivar]
                        if old_value is None:
                            old_value = []
                            new_value = old_value.append(current_sitename)
                            cultivar_site_map[current_cultivar] = new_value
                        else:
                            new_value = old_value
                            new_value.append(current_sitename)
                            cultivar_site_map[current_cultivar] = new_value
                    else:
                        cultivar_site_map[current_cultivar] = [current_sitename]
                line_count += 1
    elif season == 'Season 4':
        cultivar_site_map = {}
        with open(cultivars_season_4_csv, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'sitename':
                    pass
                else:
                    current_sitename = row[0]
                    current_cultivar = row[1]
                    if current_cultivar in cultivar_site_map:
                        old_value = cultivar_site_map[current_cultivar]
                        if old_value is None:
                            old_value = []
                            new_value = old_value.append(current_sitename)
                            cultivar_site_map[current_cultivar] = new_value
                        else:
                            new_value = old_value
                            new_value.append(current_sitename)
                            cultivar_site_map[current_cultivar] = new_value
                    else:
                        cultivar_site_map[current_cultivar] = [current_sitename]
    return cultivar_site_map

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


def get_clowder_result_date_range(product, start_date, end_date, sites = []):
    results = []
    date_range = get_date_range(start_date, end_date)

    for each_date in date_range:
        #new method
        #results_for_date = get_clowder_result_single_date(product, each_date)

        #old method
        results_for_date = get_clowder_result_single_date_old_method(product,each_date, sites)
        results.extend(results_for_date)
    return results


def get_clowder_result_single_date(product, date, sites = []):

    dataset_name = product

    results = []
    current_search_url = terra_clowder_search_url+'name:'+dataset_name+' name:'+date+'&key='+os.environ['CLOWDER_KEY']
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
        print('nothing found, using dummy placeholder data')
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


def get_clowder_result_single_date_old_method(product, date, sites =[]):
    results = []
    dataset_name = product + ' - ' + date

    url = terra_clowder_dataset_title_url + dataset_name + '&key='+os.environ['CLOWDER_KEY']

    if os.environ['TEST'] == 'True':
        ds = sample_data
    else:
        print('getting results for ', url)
        dataset_data = requests.get(url)
        ds = dataset_data.json()

    if type(ds) == list:
        for each in ds:
            current_id = each['id']
            metadata_url = terra_clowder_dataset_metadata_url.replace('current_id',current_id)+'?key='+os.environ['CLOWDER_KEY']

            try:
                md = requests.get(metadata_url)
            except Exception as e:
                print(e)
            if md.status_code == 200:
                md_json = md.json()
                current_sitename = get_sitename_from_ds_metadata(md_json[0])
            current_name = each['name']
            current_dataset_url = terra_clowder_dataset_url+'/'+current_id
            download_link = terra_clowder_datasets_api_url+'/'+current_id
            result = {"name": current_name, "view": current_dataset_url, "download": download_link}
            if len(sites) > 0:
                if current_sitename in sites:
                    results.append(result)
            else:
                results.append(result)
        return results

    return results
