import requests
import json
import pandas as pd
import datetime
import time
import re
import scipy
import numpy as np


pd.set_option('display.max_columns', 100)

#url = 'http://yield.chinabond.com.cn/cbweb-mn/yc/searchYc?workTimes=2020-06-24&&xyzSelect=txy&&dxbj=0&&qxll=0,&&yqqxN=N&&yqqxK=4&&ycDefIds=2c9081e50a2f9606010a309f4af50111,8a8b2ca045e879bf014607ebef677f8e,2c908188138b62cd01139a2ee6b51e25,2c90818812b319130112c279222836c3,8a8b2ca045e879bf014607f9982c7fc0,2c9081e91b55cc84011be40946ca0925,2c9081e91e6a3313011e6d438a58000d,8a8b2ca04142df6a014148ca880f3046,2c9081e91ea160e5011eab1f116c1a59,&&wrjxCBFlag=0&&locale=zh_CN'


def get_url(workTimes):
    ycDefIds = ['2c9081e50a2f9606010a309f4af50111',
                 '8a8b2ca045e879bf014607ebef677f8e',
                 '2c908188138b62cd01139a2ee6b51e25',
                 '2c90818812b319130112c279222836c3',
                 '8a8b2ca045e879bf014607f9982c7fc0',
                 '2c9081e91b55cc84011be40946ca0925',
                 '2c9081e91e6a3313011e6d438a58000d',
                 '8a8b2ca04142df6a014148ca880f3046',
                 '2c9081e91ea160e5011eab1f116c1a59',
                 '8a8b2ca0455847ac0145650780ad68fb',
                 '8a8b2ca0455847ac0145650ba23b68ff']

    base_url = 'http://yield.chinabond.com.cn/cbweb-mn/yc/searchYc?'
    ycDefIds_value = ''
    for item in ycDefIds:
        ycDefIds_value = ycDefIds_value + item + ','
    ycDefIds = ('ycDefIds', ycDefIds_value)

    params = (workTimes, ('xyzSelect', 'txy'), ('dxbj', '0'), ('qxll', '0,'), ('yqqxN', 'N'), ('yqqxK', '4'), ycDefIds, ('wrjxCBFlag', '0'), ('locale', 'zh_CN'))

    for item in params:
        base_url = base_url + item[0] + '=' + item[1] + '&&'

    url = base_url[:-2]
    return url


def get_curve():
    headers = {
        'Host': 'yield.chinabond.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Referer': 'http://yield.chinabond.com.cn/cbweb-mn/yield_main',
        'X-Requested-With' : 'XMLHttpRequest',}
    for n_day in range(365):
        workTimes = ('workTimes',str((datetime.datetime.now()-datetime.timedelta(days=n_day)).strftime('%Y-%m-%d')))
        url = get_url(workTimes)
        response = requests.post(url=url,headers=headers)
        data = response.text
        if data:
            data = json.loads(data)
            break
    #data = pd.DataFrame(data)
    pattern = re.compile(r'\((.*?)\)')
    #data['评级'] = data['ycDefName'].map(lambda x : pattern.search(x).group(1).strip())
    ret_data = {}

    ''' @一种数据结构 {'AA': [[x,y]]}, 注意AA+为'AA＋'
        for item in data:
        num_valid = []
        for num_list in item['seriesData']:
            if str(num_list[1]).strip() != 'None':
                num_valid.append(num_list)
        ret_data[pattern.search(item['ycDefName']).group(1)] = num_valid
    '''
    #另一种数据结构 {'AA':[x,y]}
    for item in data:
        X = []
        Y = []
        for num_list in item['seriesData']:
            if str(num_list[1]).strip() != 'None':
                X.append(num_list[0])
                Y.append(num_list[1])
        temp = pattern.search(item['ycDefName']).group(1)
        key = temp if (temp[-1] != '＋') else (temp[:-1] + '+')
        ret_data[key] = [X, Y]
    return ret_data
