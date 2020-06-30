import math
import scipy.stats as st


def get_bs_option_value(stock_price, convert_price, year_left, rate, std):
    rate_continue = math.log(1+rate)

    d1 = (math.log(stock_price/convert_price) + (rate_continue + 0.5*(std)**2) * year_left) / (std * (year_left)**0.5)
    d2 = d1 - std * (year_left)**0.5
    Nd1 = st.norm.cdf(d1)
    Nd2 = st.norm.cdf(d2)
    C = stock_price * Nd1 - convert_price * math.exp(rate_continue * -1 * year_left) * Nd2
    bs_option = (100 / convert_price) * C
    
    return bs_option
