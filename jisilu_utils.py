
import pandas as pd
import numpy as np

def remove_per (str):           #remove '%' in data
    str = str[:-1]
    return str

def data_process(data, columns): #
    for col in columns:
        data[col] = data[col].apply(remove_per)
        data[col] = data[col].apply(pd.to_numeric, errors = 'ignore')*0.01
    return data.apply(pd.to_numeric, errors = 'ignore')

def get_name_part(str):
    str = str[-2:]
    return str

def get_bond_time(str):

    if str != '待上市':
        str = str[-8:]
    return str
