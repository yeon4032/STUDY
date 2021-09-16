# -*- coding: utf-8 -*-
"""
black-Scholes Model

"""

import numpy as np
import scipy.stats as stat

#black-Scholes Option Formula
def europian_option(S, K, T, r, sigma, option_type):
    
    d1 = (np.log(S/K)+(r++0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        V = S * stat.norm.cdf(d1) - K * np.exp(-r * T) * stat.norm.cdf(d2)
        
    else:
        V = K * np.exp(-r*T) * stat.norm.cdf(-d2) - S * stat.norm.cdf(-d1)
        
    return V

#구현화
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot #이거 다운로드시 유료인지?
init_notebook_mode(connected=True)


#함수 입력값
K=100
r=0.01
sigma=0.25

#variables
T=np.linspace(0,1,100)
S=np.linspace(0,200,100) # lstm 시계열 예측  -> 과거 데이터로 modeling 해보고 그다음 과거 데이터를 기반으로 비교
T,S=np.meshgrid(T,S)

#Output
Call_Value = europian_option(S, K, T, r, sigma, 'call')
Put_Value = europian_option(S, K, T, r, sigma, 'put')




#################################3
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot #이거 다운로드시 유료인지?
init_notebook_mode(connected=True)
#다운로드 못해서 안됨
# 아래 것들도 
##########################################

#3차원 서피스
#Call
trace = go.Surface(x=T,y=S,z=Call_Value)
data=[trace]
layout = go.Layout(title='Call Option',
                   scene={'xaxis':{'title':'Maturity'},'yaxis':{'title':'Spot Price'},'zaxis':{'title':'Option Price'}}
                   )
fig = go.Figure(data=data, layout=layout)
iplot(fig)

#Put
trace = go.Surface(x=T,y=S,z=Call_Value)
data=[trace]
layout = go.Layout(title='Put Option',
                   scene={'xaxis':{'title':'Maturity'},'yaxis':{'title':'Spot Price'},'zaxis':{'title':'Option Price'}}
                   )
fig = go.Figure(data=data, layout=layout)
iplot(fig)


####################################################################################
#시계열 예측분석

#삼성전야 주가 예측
# pip install tensorflow
import tensorflow as tf
import pandas as pd
import os
# 시작
#데이터 다운로드
os.chdir('C:/ITWILL/4_python-ll/data')
df_price = pd.read_csv('Samsung.csv')
df_price.describe()













