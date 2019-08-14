import os
import csv

search_csv = 'search_list_s6.csv'

current_location = os.getcwd()

path_to_map = os.path.join(current_location, search_csv)

clowder_products = ['RGB GeoTIFFs', 'Thermal IR GeoTIFFs', 'Laser Scanner 3D LAS',
                    'Full Field RGB Images', 'Full Field IR Images']

rgb_geotiffs_csv = 'rgb_geotiffs_search_list_s6.csv'
thermal_ir_geotiffs_csv = 'thermal_ir_geotiffs_search_list_s6.csv'
laser_3d_scanner_3d_las_csv = 'laser_3d_scanner_3d_las_search_list_s6.csv'
full_field_rgb_images_csv = 'full_field_rgb_images_search_list_s6.csv'
full_field_ir_images_csv = 'full_field_ir_images_search_list_s6.csv'

print(os.path.isfile(path_to_map))
f= open(path_to_map, 'r')
full_reader = csv.reader(f)

other = 'other_search_list_s6.csv'

f1=  open(rgb_geotiffs_csv, 'w')
rgb_geotiff_writer = csv.writer(f1)

f2 = open(thermal_ir_geotiffs_csv, 'w')
therma_ir_writer = csv.writer(f2)

f3 = open(laser_3d_scanner_3d_las_csv, 'w')
laser_3d_writer = csv.writer(f3)

f4 = open(full_field_rgb_images_csv, 'w')
full_field_rgb_writer = csv.writer(f4)

f5 =  open(full_field_ir_images_csv, 'w')
full_field_ir_images_csv = csv.writer(f5)

f6 = open(other, 'w')
other_writer = csv.writer(f6)


for row in full_reader:
    dataset_name = row[1]
    if dataset_name.startswith(clowder_products[0]):
        rgb_geotiff_writer.writerow(row)
    elif dataset_name.startswith(clowder_products[1]):
        therma_ir_writer.writerow(row)
    elif dataset_name.startswith(clowder_products[2]):
        laser_3d_writer.writerow(row)
    elif dataset_name.startswith(clowder_products[3]):
        full_field_rgb_writer.writerow(row)
    elif dataset_name.startswith(clowder_products[4]):
        full_field_ir_images_csv.writerow(row)
    else:
        other_writer.writerow(row)
print('done')