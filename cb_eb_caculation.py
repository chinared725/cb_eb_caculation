from cb_eb_class import CbEb
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',100)

bond_type = 'cb'
bond_price = 115
premium_rate = 0.25
pb = 1

if __name__ == '__main__':

    '''
    print('\n双低可转债，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    print(CbEb().get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, pb=pb, adjusted = False))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n可转债熟女+双低，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    print(CbEb().get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, pb=pb, adjusted = True))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n待上市可转债-----------------------------------------------------------------\n\n')
    print(CbEb().get_bond_not_list(bond_type=bond_type))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n你想了解的可转债可转债-----------------------------------------------------------------\n\n')
    bond_names = ['长证转债','国君转债','浙商转债','华安转债']
    bond = CbEb().get_bond_data_by_name(bond_names)
    print(bond)
    '''
    bond = CbEb().data
    print(bond)
