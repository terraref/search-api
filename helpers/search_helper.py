import csv
import os

map_file_name = 'dataset_name_map.csv'

current_location = os.getcwd()

path_to_map = os.path.join(current_location, map_file_name)


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