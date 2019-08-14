import csv
import os
from helpers import split_csv
from helpers import clowder_helper

if 'SEARCH_CACHE_DIR' in os.environ:
    search_cache_dir = os.environ['SEARCH_CACHE_DIR']


search_csv = 'search_list_s6.csv'

search_csv_names = split_csv.generate_csv_names(search_csv, location=search_cache_dir)

full_search_csv = os.path.join(search_cache_dir, search_csv)




current_location = os.getcwd()

# path_to_map = os.path.join(current_location, 'helpers', search_csv)
#
# path_to_rgb_geotiff_map = os.path.join(current_location, 'helpers', rgb_geotiffs_csv)
# path_to_thermal_ir_geotiffs_map =  os.path.join(current_location, 'helpers', thermal_ir_geotiffs_csv)
# path_to_laser_3d_scanner_las_map = os.path.join(current_location, 'helpers', laser_3d_scanner_3d_las_csv)
# path_to_fullfield_product_map = os.path.join(current_location, 'helpers', full_field_images_csv)
# path_to_other_map = os.path.join(current_location, 'helpers', other_csv)


def get_datasets_by_product_dataset_name(dataset_name, sites=[]):
    print('using individual product csvs')
    results = []
    map_to_use = full_search_csv
    if dataset_name.startswith(split_csv.clowder_products[0]):
        map_to_use = search_csv_names[0]
    elif dataset_name.startswith(split_csv.clowder_products[1]):
        map_to_use = search_csv_names[1]
    elif dataset_name.startswith(split_csv.clowder_products[2]):
        map_to_use = search_csv_names[2]
    elif dataset_name.startswith(split_csv.clowder_products[3]):
        map_to_use = search_csv_names[3]
    elif dataset_name.startswith(split_csv.clowder_products[4]):
        map_to_use = search_csv_names[4]
    f = open(map_to_use, 'r')
    reader = csv.reader(f)
    for row in reader:
        current_name = row[1]
        current_plot = row[2]
        current_id = row[0]
        if len(sites) > 0:
            if current_name.startswith(dataset_name):
                if current_plot in sites:
                    current_entry = dict()
                    current_entry["name"] = current_name
                    current_entry["id"] = current_id
                    results.append(current_entry)
        else:
            if current_name.startswith(dataset_name):
                current_entry = dict()
                current_entry["name"] = current_name
                current_entry["id"] = current_id
                results.append(current_entry)
    if len(results) == 0:
        map_to_use = search_csv_names[0]
        f = open(map_to_use, 'r')
        reader = csv.reader(f)
        for row in reader:
            current_name = row[1]
            current_plot = row[2]
            current_id = row[0]
            if len(sites) > 0:
                if current_name.startswith(dataset_name):
                    if current_plot in sites:
                        current_entry = dict()
                        current_entry["name"] = current_name
                        current_entry["id"] = current_id
                        results.append(current_entry)
            else:
                if current_name.startswith(dataset_name):
                    current_entry = dict()
                    current_entry["name"] = current_name
                    current_entry["id"] = current_id
                    results.append(current_entry)
    return results



def findDatasetsFromCSV(dataset_name, sites= []):

    all_files = True
    for each in search_csv_names:
        if not os.path.isfile(each):
            all_files = False

    if all_files:
        get_datasets_by_product_dataset_name(dataset_name, sites)

    results = []

    f = open(full_search_csv, 'r')
    reader = csv.reader(f)
    for row in reader:
        current_name = row[1]
        current_plot = row[2]
        current_id = row[0]
        if len(sites) > 0:
            if current_name.startswith(dataset_name):
                if current_plot in sites:
                    current_entry = dict()
                    current_entry["name"] = current_name
                    current_entry["id"] = current_id
                    results.append(current_entry)
        else:
            if current_name.startswith(dataset_name):
                current_entry = dict()
                current_entry["name"] = current_name
                current_entry["id"] = current_id
                results.append(current_entry)
    return results
