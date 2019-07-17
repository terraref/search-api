import requests
import pandas as pd
import datetime
from datetime import datetime
import os


bety_api = "https://terraref.ncsa.illinois.edu/bety/api/v1/search"
bety_key = 'SECRET'

ignore_fields = ['citation_id', 'site_id', 'treatment_id', 'city', 'result_type', 'citation_year', 'id',
                 'commonname', 'genus', 'species_id', 'cultivar_id', 'author', 'n',
                 'statname', 'stat', 'notes', 'access_level', 'entity', 'method_name',
                 'view_url', 'edit_url',
                 'time', 'raw_date', 'month', 'year', 'dateloc']


def get_datetime_object(bety_date_string):
    if '(America/Phoenix)' in bety_date_string:
        bety_date_string = bety_date_string.replace('(America/Phoenix)', '')
        bety_date_string = bety_date_string.rstrip(' ')
    dt_object = datetime.strptime(bety_date_string, '%Y %b %d')
    return dt_object

def generate_bety_csv_from_filename(filename):
    parts_of_filename = filename.split(' ')
    product = parts_of_filename[-1].replace('.csv', '')
    sitename = filename[:filename.index(product)]
    result = get_trait_sitename(sitename, trait=product, bety_key= os.environ['BETY_KEY'])
    return result


def get_bety_search_result(sitename, trait):
    t = trait.lower().replace(' ', '_')
    csv_name = "%s %s.csv" % (sitename, t)
    apiIP = os.getenv('COUNTER_API_IP', "0.0.0.0")
    apiPort = os.getenv('COUNTER_API_PORT', "5454")
    download_link = 'http://' + apiIP + ':' + apiPort + '/download_bety_file/' + csv_name
    download_link = download_link.replace(' ', '%20')
    return {"name": trait + ' ' + sitename,
            "view": "https://traitvis.workbench.terraref.org/", "download": download_link}

def get_trait_sitename(sitename, trait, bety_key):
    t = trait.lower().replace(' ', '_')
    csv_name = "%s%s.csv" % (sitename, t)
    apiIP = os.getenv('COUNTER_API_IP', "0.0.0.0")
    apiPort = os.getenv('COUNTER_API_PORT', "5454")

    values = []
    full_column_names = []

    offset = 0
    done = False
    while not done:
        full_url = "%s?trait=%s&sitename=~%s&limit=10000&offset=%skey=%s" % (bety_api, t, sitename, offset, bety_key)
        r = requests.get(full_url, timeout=None)
        if r.status_code == 200:
            data = r.json()["data"]
            if offset == 0:
                for entry in data:
                    keys = list(entry.keys())
                    current_entry_dict = entry[keys[0]]
                    current_date = current_entry_dict["date"]
                    current_dt_object = get_datetime_object(current_date)
                    current_entry_dict["date"] = current_dt_object
                    current_entry_dict["plot"] = current_entry_dict["sitename"]
                    current_entry_dict["method"] = current_entry_dict["method_name"]
                    current_row = []
                    row_keys = list(current_entry_dict.keys())
                    if full_column_names == []:
                        for k in row_keys:
                            if k in ignore_fields:
                                pass
                            else:
                                full_column_names.append(k)
                    for each in full_column_names:
                        current_value = current_entry_dict[each]
                        current_row.append(current_value)
                    values.append(current_row)
                if len(data) < 10000:
                    done = True
                else:
                    offset += 10000
            else:
                if len(data > 0):
                    for entry in data:
                        keys = list(entry.keys())
                        current_entry_dict = entry[keys[0]]
                        current_date = current_entry_dict["date"]
                        current_dt_object = get_datetime_object(current_date)
                        current_entry_dict["date"] = current_dt_object
                        current_row = []
                        row_keys = list(current_entry_dict.keys())
                        if full_column_names == []:
                            for k in row_keys:
                                if k in ignore_fields:
                                    pass
                                else:
                                    full_column_names.append(k)
                        for each in full_column_names:
                            current_value = current_entry_dict[each]
                            current_row.append(current_value)
                        values.append(current_row)

            if len(data) < 10000:
                done = True
            else:
                offset += 10000

    df = pd.DataFrame(values, columns=full_column_names)
    df.sort_values(by=['date'], inplace=True, ascending=True)

    df.to_csv(csv_name, index=False)

    return csv_name

    # return {"name": trait+' '+sitename,
    #         "view": "https://traitvis.workbench.terraref.org/", "download":download_link}

