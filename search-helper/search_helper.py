import csv
import os

map_file_name = 'dataset_name_map.csv'

current_location = os.getcwd()

path_to_map = os.path.join(current_location, map_file_name)


def findDatasetIds(dataset_name):
    dataset_ids = []

    f = open(path_to_map, 'r')
    reader = csv.reader(f)
    for row in reader:
        current_name = row[1]
        if current_name.startswith(dataset_name):
            dataset_ids.append(row[0])
    return dataset_ids