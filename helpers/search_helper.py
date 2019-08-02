import csv
import os

search_csv = 'search_list_s6.csv'

current_location = os.getcwd()

path_to_map = os.path.join(current_location, 'helpers', search_csv)


def findDatasetsFromCSV(dataset_name, sites= []):
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
