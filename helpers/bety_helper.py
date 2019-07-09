import requests
import pandas as pd
import datetime
from datetime import datetime

bety_api = "https://terraref.ncsa.illinois.edu/bety/api/v1/search"
bety_key = 'SECRET'

def get_datetime_object(bety_date_string):
    dt_object = datetime.strptime(bety_date_string, '%Y %b %d')
    return dt_object

def get_canopy_cover_sitename(sitename, bety_key):
    values = []
    column_names = ["date", "sitename", "trait", "trait_description", "mean"]

    traits = ["canopy_cover"]
    t = traits[0]
    offset = 0
    done = False
    while done == False:
        full_url = "%s?trait=%s&sitename=~%s&limit=10000&offset=%skey=%s" % (bety_api, t, sitename, offset, bety_key)
        r = requests.get(full_url, timeout=None)
        if r.status_code == 200:
            data = r.json()["data"]
            if offset == 0:
                for entry in data:
                    vals = entry["traits_and_yields_view"]
                    current_dt = get_datetime_object(vals["date"])
                    current_row = [current_dt, vals["sitename"], vals["trait"], vals["trait_description"],
                                   vals["mean"]]
                    values.append(current_row)
                if len(data) < 10000:
                    done = True
                else:
                    offset += 10000
            else:
                if len(data > 0):
                    for entry in data:
                        vals = entry["traits_and_yields_view"]
                        current_dt = get_datetime_object(vals["date"])
                        current_row = [current_dt, vals["sitename"], vals["trait"], vals["trait_description"],
                                       vals["mean"]]
                        values.append(current_row)

            if len(data) < 10000:
                done = True
            else:
                offset += 10000

    df = pd.DataFrame(values, columns=column_names)
    df.sort_values(by=['date'], inplace=True, ascending=True)

    csv_name = "%s %s.csv" % (sitename, t)

    df.to_csv(csv_name, index=False)