import csv
import os

search_csv = 'search_list_s6.csv'

rgb_geotiffs_csv = 'rgb_geotiffs_search_list_s6.csv'
thermal_ir_geotiffs_csv = 'thermal_ir_geotiffs_search_list_s6.csv'
laser_3d_scanner_3d_las_csv = 'laser_3d_scanner_3d_las_search_list_s6.csv'
full_field_images_csv = 'fullfields_search_list_s6.csv'




current_location = os.getcwd()

path_to_map = os.path.join(current_location, 'helpers', search_csv)

path_to_rgb_geotiff_map = os.path.join(current_location, 'helpers', rgb_geotiffs_csv)
path_to_thermal_ir_geotiffs_map =  os.path.join(current_location, 'helpers', thermal_ir_geotiffs_csv)
path_to_laser_3d_scanner_las_map = os.path.join(current_location, 'helpers', laser_3d_scanner_3d_las_csv)
path_to_fullfield_product_map = os.path.join(current_location, 'helpers', full_field_images_csv)


def get_datasets_by_product_dataset_name(dataset_name, sites=[]):
    print('using individual product csvs')
    results = []
    map_to_use = path_to_map
    if dataset_name.startswith("RGB"):
        map_to_use = path_to_rgb_geotiff_map
    elif dataset_name.startswith('Thermal'):
        map_to_use = path_to_thermal_ir_geotiffs_map
    elif dataset_name.startswith('Laser'):
        map_to_use = path_to_laser_3d_scanner_las_map
    elif dataset_name.startswith('Full Field'):
        map_to_use = path_to_fullfield_product_map
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

    if os.path.isfile(path_to_rgb_geotiff_map) and os.path.isfile(path_to_thermal_ir_geotiffs_map) and os.path.isfile(path_to_laser_3d_scanner_las_map) and os.path.isfile(path_to_fullfield_product_map):
        return get_datasets_by_product_dataset_name(dataset_name, sites)

    results = []

    f = open(path_to_map, 'r')
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
