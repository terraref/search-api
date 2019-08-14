import os
import csv

split_csv_dir = ''
path_to_csv = 'search_list_s6.csv'

clowder_products = ['RGB GeoTIFFs', 'Thermal IR GeoTIFFs', 'Laser Scanner 3D LAS',
                    'Full Field RGB Images', 'Full Field IR Images']


def generate_csv_names(path_to_search_list_csv):
    csv_name = os.path.split(path_to_search_list_csv)[-1]
    csv_name = csv_name.rstrip('.csv')
    season_number = csv_name[-2:]

    csv_names = []

    for product in clowder_products:
        csv_name = 'search_cache_'+season_number+' '+product+'.csv'
        csv_names.append(csv_name)

    return csv_names

def get_product_csv_writers(path_to_search_list_csv):

    csv_writers = []

    csv_name = os.path.split(path_to_search_list_csv)[-1]
    csv_name = csv_name.rstrip('.csv')
    season_number = csv_name[-2:]
    for product in clowder_products:
        csv_name = 'search_cache_' + season_number + ' ' + product + '.csv'
        csv_path = os.path.join(split_csv_dir, csv_name)
        f = open(csv_path, 'w')
        current_writer = csv.writer(f)
        csv_writers.append(current_writer)

    csv_name = 'search_cache_' + season_number + ' ' + 'other' + '.csv'
    csv_path = os.path.join(split_csv_dir, csv_name)
    f = open(csv_path, 'w')
    current_writer = csv.writer(f)
    csv_writers.append(current_writer)

    return csv_writers


def get_product_csv_writer_map(path_to_search_list_csv):
    product_file_map = {}

    csv_name = os.path.split(path_to_search_list_csv)[-1]
    csv_name = csv_name.rstrip('.csv')
    season_number = csv_name[-2:]

    for product in clowder_products:
        csv_name = 'search_cache_' + season_number + ' ' + product + '.csv'
        csv_path = os.path.join(split_csv_dir, csv_name)
        f = open(csv_path, 'w')
        product_file_map[product] = f

    csv_name = 'search_cache_' + season_number + ' ' + 'other' + '.csv'
    csv_path = os.path.join(split_csv_dir, csv_name)
    f = open(csv_path, 'w')
    writer = csv.writer(f)
    product_file_map['other'] = writer

    return product_file_map

def split_full_csv(path_to_search_list_csv):
    csv_writers = get_product_csv_writers(path_to_search_list_csv)
    f = open(path_to_search_list_csv, 'r')
    reader = csv.reader(f)
    for row in reader:
        dataset_name = row[1]
        if dataset_name.startswith(clowder_products[0]):
            csv_writers[0].writerow(row)
        elif dataset_name.startswith(clowder_products[1]):
            csv_writers[1].writerow(row)
        elif dataset_name.startswith(clowder_products[2]):
            csv_writers[2].writerow(row)
        elif dataset_name.startswith(clowder_products[3]):
            csv_writers[3].writerow(row)
        elif dataset_name.startswith(clowder_products[4]):
            csv_writers[4].writerow(row)
        else:
            csv_writers[5].writerow(row)
    return 'Done'

#a = get_product_csv_writers(path_to_csv)
b = split_full_csv(path_to_csv)

print('done')
