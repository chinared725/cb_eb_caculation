from cb_eb_class import CbEb
import pandas as pd
import numpy as np

bond_type = 'cb'
bond_price = 105
premium_rate = 0.3
status = True
pb = 1

if __name__ == '__main__':


    print('\n--------------------双低可转债，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    print(CbEb().get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, status=status, pb=pb, adjusted = False))

    print('-------------------------------------------------------------------------------------------------------')
    print('\n  ------------------可转债熟女+双低，价格 < {}元，溢价率 < {}, 已上市，正股PB > {}----------------------\n\n'.format(bond_price, premium_rate, pb))
    print(CbEb().get_double_low_bond(bond_type=bond_type, bond_price=bond_price, premium_rate=premium_rate, status=status, pb=pb, adjusted = True))
