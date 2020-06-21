from cb_eb_class import CbEb
import pandas as pd
import numpy as np


if __name__ == '__main__':
    cb_price_ascending = CbEb().get_cb_data()

    cb_double_low= cb_price_ascending[(cb_price_ascending['转债价格']<105)  & (cb_price_ascending['溢价率']<0.3) \
     & (cb_price_ascending['上市状态']!='待上市') & (cb_price_ascending['pb'] > 1)]    # find cb with price lower than 105, premium rate <0.3 and pb>1

    cb_adjusted_double_low = cb_price_ascending[(cb_price_ascending['下调次数']>=1) & (cb_price_ascending['转债价格'] < 105) \
     & (cb_price_ascending['溢价率']<0.3)  & (cb_price_ascending['pb'] > 1)].sort_values(by=['转债价格', '溢价率'])  # find cb with price lower than 105, premium rate <0.3 and pb>1 and ajust for at lease one time


    print('\n--------------------双低可转债，价格 < 105元，溢价率 < 30%, 已上市，正股PB > 1----------------------\n\n')
    print(cb_double_low)
    cb_double_low.to_excel('double_low_cb.xls', index=False)

    print('-------------------------------------------------------------------------------------------------------')
    print('\n  ------------------可转债熟女+双低，价格 < 105元，溢价率 < 30%, 已上市，正股PB > 1------------------\n\n')
    print(cb_adjusted_double_low)
    cb_adjusted_double_low.to_excel('ajusted_double_low_cb.xls',index=False)
