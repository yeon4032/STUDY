# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 22:12:40 2021

@author: sihun
"""

##################################################################################################
### RNN 으로 각주식의 수익 예측 후 수익성 좋은 주식을 로만 다시 주식 선택 <- tensorflow 사용
##################################################################################################
# data 가지고 오기
import pandas as pd # CSV file read
import tensorflow as tf # seed value
import numpy as np # ndarray
from tensorflow.keras import Sequential # model
from tensorflow.keras.layers import SimpleRNN, Dense # RNN layer
import matplotlib.pyplot as plt # 시계열 분석 결과

tf.random.set_seed(12) # seed값 지정 <-중요 # seed 값 조사 해보자. 정확도 영향있음
dataset=pd.read_csv("C:\ITWILL\sihun\최종프로잭트\\price_Date_Dataset")
len(dataset) # 100
print(dataset)

# 3가지 주식가격 데이터
Dong_price=dataset.iloc[:,2]
Sin_price=dataset.iloc[:,3]
Han_price=dataset.iloc[:,4]

###########################################################################################
## Dong_price
############################################################################################
# 2. RNN 구제에 맞게 reshape 
#x_data
Dong_price=dataset.iloc[:,2]
max(Dong_price) # 307000
min(Dong_price) # 201500

Dong_price = (Dong_price-min(Dong_price))/(max(Dong_price)-min(Dong_price))
x = np.array([Dong_price[i+j] for i in range(len(Dong_price)-10) for j in range(10)])
# 190 * 30 =5100

len(x) #5100
# train/val split for x                                         <- 질문 for check 
x_train = x[:1400].reshape(140,10,1)
x_test = x[1400:].reshape(-1,10,1)

x_train.shape #(70,10,1) - (batch_size, time steps, features)
x_test.shape # (20, 10, 1) - (batch_size, time steps, features)

#y_data                                                         <- 질문 for check 
y = np.array([Dong_price[i+10] for i in range(len(Dong_price)-10)]) 

len(y) # 170190
# train/val split for y
y_train = y[:140].reshape(140,1)
y_test = y[140:].reshape(50,1)
y_train.shape #(140, 1)
y_test.shape  # (50, 1)

# 3. model 생성
input_shape = (10, 1)

model = Sequential()

#RNN layer 추가
model.add(SimpleRNN(units=6, input_shape=input_shape, activation='tanh'))

#hidden layer 추가가능 (복잡한 계산의 경우)

# DNN layer 추가
model.add(Dense(units=1)) # 출력 : 회귀모델 - MSE, MAE
#최종 출력은 예측된 숫자나 class 분류 결과이기 때문에 DNN을 이용합니다.

# model 학습환경
model.compile(optimizer='sgd', loss='mse', metrics=['mae']) # sgd, adam 비교해서 선택

# model training
model.fit(x_train,y_train, epochs=400, verbose=1)

# model prediction
y_pred = model.predict(x_test)
print(y_pred)
len(y_pred) #50
# real value vs predict value
plt.plot(y_test, 'y--', label='real value')
plt.plot(y_pred, 'r--',label='predict value')
plt.legend(loc='best')
plt.show()
len(y_test)

###########################################################################################
## Sin_price
############################################################################################


# 2. RNN 구제에 맞게 reshape 
#x_data
Sin_price=dataset.iloc[:,3]
max(Sin_price) # 307000
min(Sin_price) # 201500

Sin_price = (Sin_price-min(Sin_price))/(max(Sin_price)-min(Sin_price))
x = np.array([Sin_price[i+j] for i in range(len(Sin_price)-10) for j in range(10)])
# 190 * 30 =5100

len(x) #5100
# train/val split for x                                         <- 질문 for check 
x_train = x[:1400].reshape(140,10,1)
x_test = x[1400:].reshape(-1,10,1)

x_train.shape #(70,10,1) - (batch_size, time steps, features)
x_test.shape # (20, 10, 1) - (batch_size, time steps, features)

#y_data                                                         <- 질문 for check 
y = np.array([Sin_price[i+10] for i in range(len(Sin_price)-10)]) 

len(y) # 170190
# train/val split for y
y_train = y[:140].reshape(140,1)
y_test = y[140:].reshape(50,1)
y_train.shape #(140, 1)
y_test.shape  # (50, 1)

# 3. model 생성
input_shape = (10, 1)

model = Sequential()

#RNN layer 추가
model.add(SimpleRNN(units=8, input_shape=input_shape, activation='tanh'))

#hidden layer 추가가능 (복잡한 계산의 경우)

# DNN layer 추가
model.add(Dense(units=1)) # 출력 : 회귀모델 - MSE, MAE
#최종 출력은 예측된 숫자나 class 분류 결과이기 때문에 DNN을 이용합니다.

# model 학습환경
model.compile(optimizer='sgd', loss='mse', metrics=['mae']) # sgd, adam 비교해서 선택

# model training
model.fit(x_train,y_train, epochs=400, verbose=1)

# model prediction
y_pred = model.predict(x_test)
print(y_pred)

# real value vs predict value
plt.plot(y_test, 'y--', label='real value')
plt.plot(y_pred, 'r--',label='predict value')
plt.legend(loc='best')
plt.show()


###########################################################################################
## Han_price
############################################################################################


# 2. RNN 구제에 맞게 reshape 
#x_data
Han_price=dataset.iloc[:,4]
max(Han_price) # 307000
min(Han_price) # 201500

Han_price = (Han_price-min(Han_price))/(max(Han_price)-min(Han_price))
x = np.array([Han_price[i+j] for i in range(len(Han_price)-10) for j in range(10)])
# 190 * 30 =5100

len(x) #5100
# train/val split for x                                         <- 질문 for check 
x_train = x[:1400].reshape(140,10,1)
x_test = x[1400:].reshape(-1,10,1)

x_train.shape #(70,10,1) - (batch_size, time steps, features)
x_test.shape # (20, 10, 1) - (batch_size, time steps, features)

#y_data                                                         <- 질문 for check 
y = np.array([Han_price[i+10] for i in range(len(Han_price)-10)]) 

len(y) # 170190
# train/val split for y
y_train = y[:140].reshape(140,1)
y_test = y[140:].reshape(50,1)
y_train.shape #(140, 1)
y_test.shape  # (50, 1)

# 3. model 생성
input_shape = (10, 1)

model = Sequential()

#RNN layer 추가
model.add(SimpleRNN(units=9, input_shape=input_shape, activation='tanh'))

#hidden layer 추가가능 (복잡한 계산의 경우)

# DNN layer 추가
model.add(Dense(units=1)) # 출력 : 회귀모델 - MSE, MAE
#최종 출력은 예측된 숫자나 class 분류 결과이기 때문에 DNN을 이용합니다.

# model 학습환경
model.compile(optimizer='sgd', loss='mse', metrics=['mae']) # sgd, adam 비교해서 선택

# model training
model.fit(x_train,y_train, epochs=400, verbose=1)

# model prediction
y_pred = model.predict(x_test)
print(y_pred)

# real value vs predict value
plt.plot(y_test, 'y--', label='real value')
plt.plot(y_pred, 'r--',label='predict value')
plt.legend(loc='best')
plt.show()


##################################################################################################
### ARIMA model
##################################################################################################
'''
p is the order of the AR term

q is the order of the MA term

d is the number of differencing required to make the time series stationary

Reason of the stationarity 
‘Auto Regressive’ in ARIMA means it is a linear regression model that uses its own 
lags as predictors. Linear regression models, as you know, work best when the 
predictors are not correlated and are independent of each other.

The value of d, therefore, is the minimum number of differencing needed 
to make the series stationary. And if the time series is already stationary, 
then d = 0.

‘p’ is the order of the ‘Auto Regressive’ (AR) term. It refers to the number of 
lags of Y to be used as predictors. And ‘q’ is the order of the ‘Moving Average’ (MA) term.
 It refers to the number of lagged forecast errors that should go into the ARIMA Model.
'''

dataset=pd.read_csv("C:\ITWILL\sihun\최종프로잭트\\price_Date_Dataset")
dataset.set_index('Date', inplace=True)
dataset=dataset.iloc[:,1:]

# 시각화
dataset['Dong_price'].plot()
dataset['Sin_price'].plot()
dataset['Han_price'].plot()

# Test for Stationarity
from statsmodels.tsa.stattools import adfuller

def adf_test(df):
    result=adfuller(df)
    print('ADF Statistics: %f' % result[0])
    print('p_vlaue: %f' % result[1])
    print('Critical values')
    for Key, value in result[4].items():
        print('\t%s: %.3f' % (Key, value))

adf_test(dataset['Han_price'])
'''
ADF Statistics: -1.995729
p_vlaue: 0.288449
Critical values
	1%: -3.464
	5%: -2.876
	10%: -2.575

P 값이 0.05 보다 크다 그럼으로 stationarity 즉 안정성이 없다.
'''
      
# 차분 or return 값 을 이용하여 정상성(stationarity)를 부여할수있다.
#차분 (difference between t and t-1)
diff = dataset['Han_price'].diff()
diff.dropna(inplace=True)
adf_test(diff)
'''
ADF Statistics: -11.550499
p_vlaue: 0.000000
Critical values
	1%: -3.464
	5%: -2.876
	10%: -2.575
'''

########
import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Import data
df = dataset['Han_price']

# Original Series
fig, axes = plt.subplots(3, 2, sharex=True)
axes[0, 0].plot(df); axes[0, 0].set_title('Original Series')
plot_acf(df, ax=axes[0, 1])

# 1st Differencing
axes[1, 0].plot(df.diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(df.diff().fillna(0), ax=axes[1, 1])

# 2nd Differencing
axes[2, 0].plot(df.diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
plot_acf(df.diff().diff().dropna(), ax=axes[2, 1])

plt.show()
#########################################################################################################
from pmdarima.arima.utils import ndiffs
df = dataset['Han_price']
y = df

## Adf Test
ndiffs(y, test='adf')  # 1

# KPSS test
ndiffs(y, test='kpss')  # 1

# PP test:
ndiffs(y, test='pp')  # 0

# How to find the order of the AR term (p)
# PACF plot of 1st differenced series
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(df.diff().dropna(), ax=axes[1])

plt.show()

# How to find the order of the MA term (q)
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

# Import data
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,1.2))
plot_acf(df.diff().dropna(), ax=axes[1])

plt.show()


# How to build the ARIMA Model
from statsmodels.tsa.arima_model import ARIMA

# 1,1,0 ARIMA Model
model = ARIMA(df.diff().dropna(), order=(1,1,0))#(AR ,D, MA)
model_fit = model.fit(disp=-1)
print(model_fit.summary())

# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
plt.show()

# Actual vs Fitted
model_fit.plot_predict(dynamic=False)
plt.show()

# How to do find the optimal ARIMA model manually using Out-of-Time Cross validation
from statsmodels.tsa.stattools import acf

# Create Training and Test
train = df[:170]
test = df[170:]

# Build Model1
# model = ARIMA(train, order=(3,2,1))  
model = ARIMA(train, order=(1, 1, 0))  
fitted = model.fit(disp=-1)  

# Forecast
fc, se, conf = fitted.forecast(30, alpha=0.05)  # 95% conf

# Make as pandas series
fc_series = pd.Series(fc, index=test.index)
lower_series = pd.Series(conf[:, 0], index=test.index)
upper_series = pd.Series(conf[:, 1], index=test.index)

# Plot
plt.figure(figsize=(12,5), dpi=100)
plt.plot(train, label='training')
plt.plot(test, label='actual')
plt.plot(fc_series, label='forecast')
plt.fill_between(lower_series.index, lower_series, upper_series, 
                 color='k', alpha=.15)
plt.title('Forecast vs Actuals')
plt.legend(loc='upper left', fontsize=8)
plt.show()

'''
# Build Model2
model = ARIMA(train, order=(1, 1, 0))  
fitted = model.fit(disp=-1)  
print(fitted.summary())

# Forecast
fc, se, conf = fitted.forecast(20, alpha=0.05)  # 95% conf

# Make as pandas series
fc_series = pd.Series(fc, index=test.index)
lower_series = pd.Series(conf[:, 0], index=test.index)
upper_series = pd.Series(conf[:, 1], index=test.index)

# Plot
plt.figure(figsize=(12,5), dpi=100)
plt.plot(train, label='training')
plt.plot(test, label='actual')
plt.plot(fc_series, label='forecast')
plt.fill_between(lower_series.index, lower_series, upper_series, 
                 color='k', alpha=.15)
plt.title('Forecast vs Actuals')
plt.legend(loc='upper left', fontsize=8)
plt.show()
'''

#Accuracy Metrics for Time Series Forecast
# Accuracy metrics
def forecast_accuracy(forecast, actual):
    mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
    me = np.mean(forecast - actual)             # ME
    mae = np.mean(np.abs(forecast - actual))    # MAE
    mpe = np.mean((forecast - actual)/actual)   # MPE
    rmse = np.mean((forecast - actual)**2)**.5  # RMSE
    corr = np.corrcoef(forecast, actual)[0,1]   # corr
    mins = np.amin(np.hstack([forecast[:,None], 
                              actual[:,None]]), axis=1)
    maxs = np.amax(np.hstack([forecast[:,None], 
                              actual[:,None]]), axis=1)
    minmax = 1 - np.mean(mins/maxs)             # minmax
    acf1 = acf(fc-test)[1]                      # ACF1
    return({'mape':mape, 'me':me, 'mae': mae, 
            'mpe': mpe, 'rmse':rmse, 'acf1':acf1, 
            'corr':corr, 'minmax':minmax})

forecast_accuracy(fc, test.values)
# Around 2.2% MAPE implies the model is about 97.8% accurate in predicting the next 30 observations.


#How to do Auto Arima Forecast in Python
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm

model = pm.auto_arima(df, start_p=1, start_q=1,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=3, max_q=3, # maximum p and q
                      m=1,              # frequency of series
                      d=None,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

print(model.summary())
#Best model:  ARIMA(0,1,0)(0,0,0)[0] 

#How to interpret the residual plots in ARIMA model
model.plot_diagnostics(figsize=(7,5))
plt.show()

# Forecast
n_periods = 3
fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
index_of_fc = np.arange(len(df), len(df)+n_periods)
'''
op left: The residual errors seem to fluctuate around a mean of zero and have a uniform variance.

Top Right: The density plot suggest normal distribution with mean zero.

Bottom left: All the dots should fall perfectly in line with the red line. Any significant deviations would imply the distribution is skewed.

Bottom Right: The Correlogram, aka, ACF plot shows the residual errors are not autocorrelated. Any autocorrelation would imply that there is some pattern in the residual errors which are not explained in the model. So you will need to look for more X’s (predictors) to the model.
'''
# make series for plotting purpose
fc_series = pd.Series(fc, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc)
upper_series = pd.Series(confint[:, 1], index=index_of_fc)

# Plot
plt.plot(df)
plt.plot(fc_series, color='darkgreen')
plt.fill_between(lower_series.index, 
                 lower_series*1.05, 
                 upper_series, 
                 color='k', alpha=.15)

plt.title("Final Forecast of WWW Usage")
plt.show()

