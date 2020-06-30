import math
import scipy.stats as st


'''
@计算B-S期权模型下的可转债期权价值
stock_price：正股价
convert_price:转股价
year_left: 剩余年限
rate: 为连续复利下的年化收益率, 可以使用同年限的国债利率
std：正股的年化收益率标准差，股票每日的收益率（就是每日涨跌幅）数据标准差。最终用于计算的，应该乘以1年内交易日250的开方

'''
def get_bs_option_value(stock_price, convert_price, year_left, rate, std):
    rate_continue = math.log(1+rate)
    std_continue_year = std * (250)**0.5

    d1 = (math.log(stock_price/convert_price) + (rate_continue + 0.5*(std_continue_year)**2) * year_left) / (std_continue_year * (year_left)**0.5)
    d2 = d1 - std_continue_year * (year_left)**0.5
    Nd1 = st.norm.cdf(d1)
    Nd2 = st.norm.cdf(d2)
    C = stock_price * Nd1 - convert_price * math.exp(rate_continue * -1 * year_left) * Nd2
    bs_option = (100 / convert_price) * C

    return bs_option
