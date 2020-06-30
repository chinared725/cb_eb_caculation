import baostock as bs
import pandas as pd
import numpy as np
import datetime

'''
@从baostock拉股票的数据

'''


class BS_Api:
#### 登陆系统 ####
    def __init__(self):
        self.lg = bs.login()
        self.end_date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.start_date = (datetime.datetime.now()-datetime.timedelta(days=365)).strftime('%Y-%m-%d')

    def get_daily_data(self, stock_id):
        stock_id = stock_id[:2].lower() + '.' + stock_id[2:]
        rs = bs.query_history_k_data_plus(stock_id,'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST',
        start_date=self.start_date, end_date=self.end_date, frequency='d', adjustflag='2')

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result = result.apply(pd.to_numeric, errors='ignore')
        return result

    def logout(self):
        print('logout')
        bs.logout()
