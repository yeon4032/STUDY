# -*- coding: utf-8 -*-
"""
팀 프로젝트 Monte Carlo Simulation
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style
path='C:\\ITWILL\\sihun\\팀 프로젝트\\data'
Dataset= pd.read_csv(path+'/국제_원유가격20100101_20210831.csv', encoding='cp949')


Price= Dataset.iloc[-256:,1]
Price=Price.transform(pd.to_numeric, errors='coerce')
Price=Price.fillna(np.mean(Price))
returns = Price.pct_change()
#Price.dtype #dtype('float64')

#Price = Price.reset_index(drop=True)


# Monte Carlo 시뮬레이션
last_price=Price.iloc[-1]


# Number of Simulations
num_simulations =1000
num_days = 101

simulation_df =pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series=[]
    
    price = last_price * (1+ np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count ==100:
            break
        price= price_series[count] * (1+ np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series


fig = plt.figure()
fig.suptitle('Monte Carlo Simulation:oil')
plt.plot(simulation_df)
plt.axhline(y=last_price, color ='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

