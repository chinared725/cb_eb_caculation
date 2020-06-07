import csv
from lxml import etree
import pandas as pd
import numpy as np
import sys
from sqlalchemy import create_engine
import datetime

from open_url_get_data import *
from jisilu_utils import *


pd.set_option('display.max_columns', 100)

url = "https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1584777951900"

data = get_data(url)
data = data_process(data, ['convert_amt_ratio', 'premium_rt', 'sincrease_rt', 'ytm_rt', 'ytm_rt_tax', 'increase_rt'])
data['turnover_rate'] = data.turnover_rt * 0.01
data['报价时间'] = data['price_tips'].apply(get_bond_time)

data.drop(['adjust_tip', 'adjusted', 'apply_cd', 'fund_rt', 'last_time', 'left_put_year', 'margin_flg', 'noted', 'online_offline_ratio', 'option_tip', 'owned',\
           'pre_bond_id', 'put_notes', 'qflag', 'qflag2', 'qstatus', 'real_force_redeem_price', 'ref_yield_info', 'repo_cd', 'sqflg', 'stock_cd', 'stock_net_value','convert_amt_ratio', \
           'premium_rt', 'sincrease_rt', 'ytm_rt', 'ytm_rt_tax','price','put_dt','put_inc_cpn_fl','put_total_days', 'rating_cd','ration', 'redeem_dt', 'redeem_inc_cpn_fl',\
           'repo_valid',  'repo_valid_from', 'repo_valid_to','ration_cd','increase_rt', 'turnover_rt'], axis=1, inplace=True)

cols = {'adj_cnt':'下调次数', 'adj_scnt':'下调成功次数', 'convert_cd':'转债占比',  'convert_cd_tip':'转股提示', 'convert_dt':'转股期开始', 'convert_price':'转股价', 'convert_price_valid':'转股价有效性',\
       'convert_price_valid_from':'转债价格生效日', 'convert_value':'转股价值', 'curr_iss_amt':'当前规模_亿', 'dblow':'双低', 'force_redeem':'最后交易日', 'force_redeem_price':'强赎股价', 'full_price':'转债价格', 'guarantor':'担保',\
       'issuer_rating_cd':'评级', 'maturity_dt':'到期日', 'next_put_dt':'回售日', 'orig_iss_amt':'原始规模_亿','put_convert_price':'回售股价', 'put_convert_price_ratio':'回售价与股价比', 'put_count_days':'回售天', 'put_price':'回售价',\
       'put_real_days':'回售剩余天数','ration_rt':'股东配售率', 'redeem_count_days':'强赎连续日', 'redeem_flag':'是否行使强赎', 'redeem_icon':'是否达到强赎标准', 'redeem_price':'强赎价', 'redeem_price_ratio':'强赎转股价值', 'redeem_real_days':'满足强赎日',\
 'redeem_style':'满足后是否强赎','redeem_total_days':'强赎总日数', 'repo_discount_rt':'折算率',  'short_maturity_dt':'到期日', 'sprice':'正股现价', 'stock_id':'正股代码', 'stock_nm':'正股名字', 'svolume':'正股成交额_万', 'total_shares':'总股本', 'turnover_rate':'换手率', \
 'volume':'可转债成交_万', 'year_left':'剩余年限', 'convert_amt_ratio1':'可转债_股票市值比', 'premium_rt1':'溢价率', 'sincrease_rt1':'正股涨幅', 'ytm_rt1':'年化税前收益率', 'ytm_rt_tax1':'年化税后收益率','bond_id':'转债代码','bond_nm':'转债名称',\
        'increase_rt1':'转债涨幅','price_tips':'上市状态'}

data.rename(columns=cols, inplace=True)

'''
try:
    engine = create_engine('mysql+pymysql://root:china12345@localhost:3306/exchange_bond', encoding='utf8')
    data.to_sql(name='current_exchange_bond', con=engine, if_exists='append', index=False, index_label=False)
    print('insert into mysql db sucess')
except:
    print('insert into mysql db fail')

'''

cb = data[data['转债名称'].apply(get_name_part) != 'EB']
eb =  data[data['转债名称'].apply(get_name_part) == 'EB']


cb_price_ascending = cb[['转债代码', '转债名称', '转债价格','正股现价','转股价','转股价值','溢价率','转债涨幅','正股涨幅','评级','剩余年限','当前规模_亿','原始规模_亿','双低',\
                   '正股名字','正股现价','pb','换手率','上市状态']].sort_values(by=['转债价格', '溢价率'])

cb_double_low= cb_price_ascending[(cb_price_ascending['转债价格']<105)  & (cb_price_ascending['溢价率']<0.3\

                                                                       ) & (cb_price_ascending['上市状态']!='待上市')]

print(cb_double_low)
