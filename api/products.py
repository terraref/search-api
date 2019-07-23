import json
bety_products = ['Canopy Cover', 'Canopy Height', 'Mean Temperature']
clowder_products = ['RGB GeoTIFFs', 'Thermal IR GeoTIFFs', 'Laser Scanner 3D LAS',
                    'Full Field RGB Images', 'Full Field IR Images']


full_products = []

def search():
    for each in bety_products:
        entry = {}
        entry['product_type'] = 'bety'
        entry['name'] = each
        full_products.append(each)

    for each in clowder_products:
        entry = {}
        entry['product_type'] = 'clowder'
        entry['name'] = each
        full_products.append(each)
    return full_products

def get():
    for each in bety_products:
        entry = {}
        entry['product_type'] = 'bety'
        entry['name'] = each
        full_products.append(each)

    for each in clowder_products:
        entry = {}
        entry['product_type'] = 'clowder'
        entry['name'] = each
        full_products.append(each)
    return full_products



