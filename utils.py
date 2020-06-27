
import pandas as pd
import numpy as np


def data_remove_percent(data, columns):  #remove '%' symble in columne
    for col in columns:
        data[col] = data[col].apply(lambda x : x[:-1])
        data[col] = data[col].apply(pd.to_numeric, errors = 'ignore')*0.01
    return data.apply(pd.to_numeric, errors = 'ignore')


def get_bond_time(str):    #function to get the bond quote time

    if str != '待上市':
        str = str[-8:]
    return str

def rate_add_percent(serie):
    serie = serie.map(lambda x : format(x, '0.2%'))
    return serie
