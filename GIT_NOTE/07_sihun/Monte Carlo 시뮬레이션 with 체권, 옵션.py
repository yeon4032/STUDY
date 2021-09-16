# -*- coding: utf-8 -*-
"""

예측
FinanceDataReader 이용해서 data load
Data1 2008 to 2009
Data2 2009 to 2011
"""
import FinanceDataReader as fdr

import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style

###Data
# 미국 10년 채권 interest rate
US10YT = fdr.DataReader('DGS10',data_source='fred')
US10YT_2 = fdr.DataReader('DGS10', start='2009-01-01', end='2012-01-01' ,data_source='fred')


# 미국 실업률
UNRATE = fdr.DataReader('UNRATE', start='2009-01-01', end='2012-01-01' ,data_source='fred')

# 통화량 (시중에 풀린 돈의 양을 의미합니다)
M2=fdr.DataReader('M2', start='2009-01-01', end='2012-01-01',data_source='fred')

# 5-Year Breakeven Inflation Rate
T5YIE = fdr.DataReader('T5YIE', start='2009-01-01', end='2012-01-01' ,data_source='fred')

# Consumer Opinion Surveys(소비자심리지수(CCSI))
Consumer_Opinion_Surveys = fdr.DataReader('CSCICP03USM665S', start='2009-01-01', end='2012-01-01',data_source='fred')


## Monte Carlo 시뮬레이션
#data used
US10YT_2 = fdr.DataReader('DGS10', start='2009-01-01', end='2012-01-01' ,data_source='fred')
retruns=US10YT_2.pct_change()
last_US10YT_2 =1.89 # US10YT_2[-1]

# Number of Simulations
num_simulations =3000
num_days = 781


simulation_df =pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = retruns.std() 
    
    yeild_series=[]
    
    yeild = last_US10YT_2 * (1+ np.random.normal(0, daily_vol))
    yeild_series.append(yeild)
    
    for y in range(num_days):
        if count ==780:
            break
        yeild= yeild_series[count] * (1+ np.random.normal(0, daily_vol))
        yeild_series.append(yeild)
        count += 1
        
    simulation_df[x] = yeild_series
    

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation:10year_US_bond yeild')
plt.plot(simulation_df)
plt.axhline(y=last_US10YT_2, color ='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('yeild')
plt.show()

# 시나리오 데이터
simulation_df
simulation_df.shape # (782, 3000)

#시나리오에 따른 체권 가격 변화 
def P_BON(F,Y,T):
    return(F/(1+Y)**T)

# 변수
T=pd.DataFrame([[10] * 3000 ] * 782 )
F=pd.DataFrame([[100000] * 3000 ] * 782) # $100,000 액면가 (예상)
Y=simulation_df *0.01

# 이자율 변화에 따른 체권 가격 변동 예측 
B_price=P_BON(F,Y,T)

# 시각화
fig = plt.figure()
fig.suptitle('Prediction based on Monte Carlo Simulation:10year_US_bond')
plt.plot(B_price)
plt.axhline(y=B_price.iloc[0,0], color ='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('price')
plt.show()
###########################################################################################3
## Var model을 이용한 Y(risk free rate) 예상
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse, aic

#Data used
# 10년 체권 수익률 
US10YT_2 = fdr.DataReader('GS10', start='2003-01-01', end='2021-07-01' ,data_source='fred')
len(US10YT_2) #223
# 미국 실업률
UNRATE = fdr.DataReader('UNRATE', start='2003-01-01', end='2021-07-01' ,data_source='fred')
len(UNRATE)#223
# 통화량 (시중에 풀린 돈의 양을 의미합니다)
M2=fdr.DataReader('MSACSR', start='2003-01-01', end='2021-07-01',data_source='fred')
len(M2) #223
# 5-Year Breakeven Inflation Rate (monthly)
T5YIE = fdr.DataReader('T5YIEM', start='2003-01-01', end='2021-07-01' ,data_source='fred')
len(T5YIE) #223
# Consumer Opinion Surveys(소비자심리지수(CCSI))
Consumer_Opinion_Surveys = fdr.DataReader('CSCICP03USM665S', start='2003-01-01', end='2021-07-01',data_source='fred')
len(Consumer_Opinion_Surveys)#223

# 정상성 검사
adfuller_test = adfuller(US10YT_2, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -1.5099145583998612
p-value: 0.5286011715958072
'''

adfuller_test = adfuller(UNRATE, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -2.818166833167419
p-value: 0.05572525700075728
'''

adfuller_test = adfuller(M2, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -1.8938828732153812
p-value: 0.3349442497516622
'''
#no need 차분
adfuller_test = adfuller(T5YIE, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -4.217793903953344
p-value: 0.0006146626489997537
'''

adfuller_test = adfuller(Consumer_Opinion_Surveys, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -1.818066033032913
p-value: 0.37153001150008147
'''

#차분 (differencing )
US10YT_2_diff = US10YT_2.diff().dropna()
UNRATE_diff = UNRATE.diff().dropna()
M2_diff = M2.diff().dropna()
Consumer_Opinion_Surveys_diff = Consumer_Opinion_Surveys.diff().dropna()

# 다시 정상성 검사
adfuller_test = adfuller(US10YT_2_diff, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -11.630266496746035
p-value: 2.2714659528262503e-21
'''

adfuller_test = adfuller(UNRATE_diff, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -11.538273597879257
p-value: 3.687578033737728e-21
'''

adfuller_test = adfuller(M2_diff, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -8.247722338437008
p-value: 5.496241955119405e-13
'''

adfuller_test = adfuller(Consumer_Opinion_Surveys_diff, autolag= "AIC")
print("ADF test statistic: {}".format(adfuller_test[0]))
print("p-value: {}".format(adfuller_test[1]))
'''
ADF test statistic: -6.068619804055549
p-value: 1.1653541090251455e-07
'''
# 사용할 data set 생성
NEW_data= pd.concat([US10YT_2_diff,UNRATE_diff,M2_diff,T5YIE.iloc[1:-1],Consumer_Opinion_Surveys_diff],axis=1)
len(NEW_data)#222
# test/train set 생성
train = NEW_data.iloc[:-50,:]
test = NEW_data.iloc[-50:,:]

forecasting_model = VAR(train)
results_aic = []
for p in range(1,10):
  results = forecasting_model.fit(p)
  results_aic.append(results.aic)

# 합한 순서에 대한 AIC 점수를 찾기 식가화
sns.set()
plt.plot(list(np.arange(1,10,1)), results_aic)
plt.xlabel("Order")
plt.ylabel("AIC")
plt.show()

# model 생성
results = forecasting_model.fit(2)
results.summary()
'''
Summary of Regression Results   
==================================
Model:                         VAR
Method:                        OLS
Date:           Thu, 09, Sep, 2021
Time:                     18:43:16
--------------------------------------------------------------------
No. of Equations:         5.00000    BIC:                   -14.2646
Nobs:                     170.000    HQIC:                  -14.8674
Log likelihood:           147.624    FPE:                2.31618e-07
AIC:                     -15.2791    Det(Omega_mle):     1.69287e-07
--------------------------------------------------------------------
Results for equation GS10
=====================================================================================
                        coefficient       std. error           t-stat            prob
-------------------------------------------------------------------------------------
const                     -0.076524         0.060324           -1.269           0.205
L1.GS10                    0.171713         0.075255            2.282           0.023
L1.UNRATE                  0.191116         0.097951            1.951           0.051
L1.MSACSR                  0.008538         0.031377            0.272           0.786
L1.T5YIEM                  0.352164         0.069681            5.054           0.000
L1.CSCICP03USM665S         0.074237         0.083261            0.892           0.373
L2.GS10                   -0.177709         0.073595           -2.415           0.016
L2.UNRATE                 -0.041757         0.099908           -0.418           0.676
L2.MSACSR                  0.014882         0.031037            0.480           0.632
L2.T5YIEM                 -0.316155         0.070175           -4.505           0.000
L2.CSCICP03USM665S         0.048415         0.084197            0.575           0.565
=====================================================================================

Results for equation UNRATE
=====================================================================================
                        coefficient       std. error           t-stat            prob
-------------------------------------------------------------------------------------
const                      0.134128         0.047270            2.837           0.005
L1.GS10                   -0.099016         0.058969           -1.679           0.093
L1.UNRATE                  0.076509         0.076754            0.997           0.319
L1.MSACSR                  0.041008         0.024587            1.668           0.095
L1.T5YIEM                 -0.054943         0.054602           -1.006           0.314
L1.CSCICP03USM665S        -0.134143         0.065242           -2.056           0.040
L2.GS10                    0.041598         0.057669            0.721           0.471
L2.UNRATE                  0.280914         0.078287            3.588           0.000
L2.MSACSR                  0.020465         0.024320            0.841           0.400
L2.T5YIEM                 -0.020187         0.054989           -0.367           0.714
L2.CSCICP03USM665S         0.062600         0.065976            0.949           0.343
=====================================================================================

Results for equation MSACSR
=====================================================================================
                        coefficient       std. error           t-stat            prob
-------------------------------------------------------------------------------------
const                     -0.271275         0.149497           -1.815           0.070
L1.GS10                   -0.177050         0.186497           -0.949           0.342
L1.UNRATE                 -0.499796         0.242744           -2.059           0.039
L1.MSACSR                 -0.370351         0.077760           -4.763           0.000
L1.T5YIEM                  0.110706         0.172685            0.641           0.521
L1.CSCICP03USM665S        -0.237477         0.206338           -1.151           0.250
L2.GS10                    0.209961         0.182385            1.151           0.250
L2.UNRATE                  0.076201         0.247595            0.308           0.758
L2.MSACSR                 -0.210993         0.076916           -2.743           0.006
L2.T5YIEM                  0.040368         0.173910            0.232           0.816
L2.CSCICP03USM665S        -0.075005         0.208658           -0.359           0.719
=====================================================================================

Results for equation T5YIEM
=====================================================================================
                        coefficient       std. error           t-stat            prob
-------------------------------------------------------------------------------------
const                      0.233193         0.065308            3.571           0.000
L1.GS10                    0.065522         0.081471            0.804           0.421
L1.UNRATE                 -0.049900         0.106042           -0.471           0.638
L1.MSACSR                  0.005844         0.033969            0.172           0.863
L1.T5YIEM                  1.265642         0.075437           16.777           0.000
L1.CSCICP03USM665S        -0.013400         0.090139           -0.149           0.882
L2.GS10                   -0.050034         0.079675           -0.628           0.530
L2.UNRATE                 -0.057633         0.108161           -0.533           0.594
L2.MSACSR                  0.016549         0.033601            0.493           0.622
L2.T5YIEM                 -0.390867         0.075972           -5.145           0.000
L2.CSCICP03USM665S        -0.042681         0.091152           -0.468           0.640
=====================================================================================

Results for equation CSCICP03USM665S
=====================================================================================
                        coefficient       std. error           t-stat            prob
-------------------------------------------------------------------------------------
const                      0.094398         0.040476            2.332           0.020
L1.GS10                    0.071255         0.050493            1.411           0.158
L1.UNRATE                  0.024653         0.065722            0.375           0.708
L1.MSACSR                 -0.050451         0.021053           -2.396           0.017
L1.T5YIEM                 -0.019865         0.046754           -0.425           0.671
L1.CSCICP03USM665S         1.169730         0.055865           20.939           0.000
L2.GS10                    0.040577         0.049380            0.822           0.411
L2.UNRATE                 -0.115976         0.067035           -1.730           0.084
L2.MSACSR                 -0.040779         0.020824           -1.958           0.050
L2.T5YIEM                 -0.027621         0.047085           -0.587           0.557
L2.CSCICP03USM665S        -0.707639         0.056493          -12.526           0.000
=====================================================================================

Correlation matrix of residuals
                       GS10    UNRATE    MSACSR    T5YIEM  CSCICP03USM665S
GS10               1.000000 -0.082501 -0.050057  0.086788         0.048421
UNRATE            -0.082501  1.000000 -0.010001 -0.062719        -0.058577
MSACSR            -0.050057 -0.010001  1.000000 -0.126753        -0.164036
T5YIEM             0.086788 -0.062719 -0.126753  1.000000        -0.001168
CSCICP03USM665S    0.048421 -0.058577 -0.164036 -0.001168         1.000000
'''


# Input data for forecasting
forecast_input = train.values[-3:]
forecast_input

#########
# Forcasting / 예측하기
fc = results.forecast(y=forecast_input, steps=50)
df_forecast = pd.DataFrame(fc, columns=test.columns)
df_forecast
#########
#######################################################################################################################

## 옵션가격 예측
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



































