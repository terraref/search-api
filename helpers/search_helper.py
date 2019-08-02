import csv
import os

search_csv = 'search_list_s6.csv'

current_location = os.getcwd()

path_to_map = os.path.join(current_location, 'helpers', search_csv)


def findDatasetIds(dataset_name):
    results = []

    f = open(path_to_map, 'r')
    reader = csv.reader(f)
    for row in reader:
        current_name = row[1]
        current_id = row[0]
        if current_name.startswith(dataset_name):
            current_entry = {}
            current_entry["name"] = current_name
            current_entry["id"] = current_id
            results.append(current_entry)
    return results