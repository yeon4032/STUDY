# -*- coding: utf-8 -*-
"""
black-Scholes Model

"""

from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame

# d1 & d2 함수
def d1(S,K,T,r,sigma):
    return(log(S/K)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*sqrt(T)

# call price & put price
def bs_call(S,K,T,r,sigma):
    return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
def bs_put(S,K,T,r,sigma):
    return K*exp(-r*T)-S+bs_call(S,K,T,r,sigma)

'''
We are able to calculate the sigma value, volatility of the stock,
by multiplying the standard deviation of the stock returns over the past year by the square root of 252 (number of days the market is open over a year). 
As for the current price I will use the last close price in our dataset. 
I will also input r, the risk-free rate, as the 10-year U.S. 
treasury yield which you could get from ^TNX
'''

## 가격 측정 
from datetime import datetime, date
import numpy as np
import pandas as pd
import pandas_datareader.data as web

# 기간, 체권, exercise price setting
stock = 'SPY'
expiry = '12-18-2022'
strike_price = 370

# 오늘 부터 1년 후
today = datetime.now()
one_year_ago = today.replace(year=today.year-1)

# 체권 가격 가지고 오기
df = web.DataReader(stock, 'yahoo', one_year_ago, today)

# 체권 가격 전처리
df = df.sort_values(by="Date")
df = df.dropna()
df = df.assign(close_day_before=df.Close.shift(1))
df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)

# 변수 측정
sigma = np.sqrt(252) * df['returns'].std() # sigma (volatility of the asset)
uty = (web.DataReader( # risk-free interest rate
    "^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100 
lcp = df['Close'].iloc[-1] # spot price of an asset # SPY
t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365 # time(기간)

print('The Option Price is: ', bs_call(lcp, strike_price, t, uty, sigma))



























