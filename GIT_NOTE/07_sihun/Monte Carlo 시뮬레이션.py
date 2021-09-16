"""
Python을 사용한 주가의 간단한 Monte Carlo 시뮬레이션
"""
#pip install pandas-datareader # datareader 설치

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2016, 11, 20)
end = dt.datetime(2017, 11, 20)

prices = web.DataReader('AAPL', 'yahoo', start, end)['Close']
returns = prices.pct_change() # pct_change() -> 판다스의 데이터프레임은 앞서 계산한 수익률을 계산해주는 pct_change()라는 메소드가 존재합니다.
len(returns)
last_price=prices[-1]
returns.dtype
# Number of Simulations
num_simulations =1000
num_days = 252

simulation_df =pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series=[]
    
    price = last_price * (1+ np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count ==251:
            break
        price= price_series[count] * (1+ np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series
    

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation:AAPL(APPLE)')
plt.plot(simulation_df)
plt.axhline(y=last_price, color ='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()



















