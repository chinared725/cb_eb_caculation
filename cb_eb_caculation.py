from cb_eb_class import CbEb
import pandas as pd
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


pd.set_option('display.max_columns',100)

bond_type = 'cb'
bond_price = 100
premium_rate = 0.2
pb = 1



if __name__ == '__main__':
    cb_eb = CbEb(daily_source='f')    #类初始化

    print('\n双低可转债，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    cb = cb_eb.get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, pb=pb, adjusted = False)
    cb = cb.sort_values(by=['理论偏离度'])
    print(cb)

    print('-------------------------------------------------------------------------------------------------------')
    print('\n双低值<{},转债价格<{}-----------------------------------------------------------------\n\n'.format(115,115))
    print(cb_eb.get_double_low_bond_by_value(bond_type=bond_type, bond_price=115, double_low_value=115))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n可转债熟女+双低，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    print(cb_eb.get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, pb=pb, adjusted = True))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n待上市可转债-----------------------------------------------------------------\n\n')
    print(cb_eb.get_bond_not_list(bond_type=bond_type))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n你想了解的可转债可转债-----------------------------------------------------------------\n\n')
    bond_names = ['钧达转债','永鼎转债','国城转债','城地转债','科华转债','华锋转债','永安转债']
    bond = cb_eb.get_bond_data_by_name(bond_names)
    print(bond)
