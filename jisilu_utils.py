
import pandas as pd
import numpy as np


def data_remove_percent(data, columns): #
    for col in columns:
        data[col] = data[col].apply(lambda x : x[:-1])
        data[col] = data[col].apply(pd.to_numeric, errors = 'ignore')*0.01
    return data.apply(pd.to_numeric, errors = 'ignore')

def get_name_part(str):
    str = str[-2:]
    return str

def get_bond_time(str):

    if str != '待上市':
        str = str[-8:]
    return str
