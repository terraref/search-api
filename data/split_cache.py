import csv

"""
INPUT: CSV with rows for Clowder datasets e.g.:

datasetId                   datasetName                             plotName
5af228294f0ce7c7a0fd3cf2	RGB GeoTIFFs - 2018-05-05__10-31-06-331	MAC Field Scanner Season 6 Range 43 Column 4
5af228284f0ce7c7a0fd3c96	RGB GeoTIFFs - 2018-05-05__10-31-07-844	MAC Field Scanner Season 6 Range 43 Column 4
...

OUTPUT: CSVs organized by product and month, e.g.:
RGB GeoTIFFs - 2018-05.csv
RGB GeoTIFFs - 2018-06.csv
...
"""

clowder_products = [
    'RGB GeoTIFFs',
    'Thermal IR GeoTIFFs',
    'Laser Scanner 3D LAS',
    'Full Field RGB Images',
    'Full Field IR Images'
]

csv_dict = {}
with open("cache_S6.csv", 'r') as input_file:
    rows = csv.reader(input_file)
    for row in rows:
        prod  = row[1].split(" - ")[0]
        month = row[1].split(" - ")[1][:7]
        key = "%s - %s" % (prod, month)

        if key not in csv_dict:
            csv_dict[key] = csv.writer(open("%s.csv" % key, 'w'))

        csv_dict[key].writerow(row)
