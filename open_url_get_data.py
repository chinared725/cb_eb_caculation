
import json
import requests
import pandas as pd
import numpy as np

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }

    try:
        response = requests.get(url, headers=headers)
    except:
        print('Connect url fail')
    data = response.content.decode('utf-8')
    data = json.loads(data)
    data = data['rows']
    ls_data = []
    for row in  data:
        ls_data.append(row['cell'])

    return pd.DataFrame(ls_data)
