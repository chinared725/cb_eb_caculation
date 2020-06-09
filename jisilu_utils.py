
def remove_per (str):           #remove '%' in data
    str = str[:-1]
    return str

def data_process(data, columns): #
    for col in columns:
        data[col+'1'] = data[col].apply(remove_per).convert_objects(convert_numeric=True) * 0.01
    return data.convert_objects(convert_numeric=True)

def get_name_part(str):
    str = str[-2:]
    return str

def get_bond_time(str):

    if str != '待上市':
        str = str[-8:]
    return str
