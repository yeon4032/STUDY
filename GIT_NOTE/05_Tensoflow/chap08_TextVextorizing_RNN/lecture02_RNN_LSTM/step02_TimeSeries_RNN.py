# -*- coding: utf-8 -*-
"""
step02_TimeSeries_RNN.py

  - 시계열 데이터 + RNN model = 시계열 분석
"""

import pandas as pd # CSV file read
import tensorflow as tf # seed value
import numpy as np # ndarray
from tensorflow.keras import Sequential # model
from tensorflow.keras.layers import SimpleRNN, Dense # RNN layer
import matplotlib.pyplot as plt # 시계열 분석 결과

tf.random.set_seed(12) # seed값 지정 <-중요 # seed 값 조사 해보자. 정확도 영향있음

# 1. csv file read
path=r'C:\ITWILL\5_Tensoflow\workspace\chap08_TextVextorizing_RNN\data'
timeSeries = pd.read_csv(path+'/timeSeries.csv')
timeSeries.info()
'''
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   no      100 non-null    int64  
 1   data    100 non-null    float64
'''

data = timeSeries['data']
len(data) # 100
print(data)

# 2. RNN 구제에 맞게 reshape 
#x_data
x = np.array([data[i+j] for i in range(len(data)-10) for j in range(10)])
# 90 * 10 =900
'''
0~9
1~10
2~11
3~12
  :
89~98      
'''
len(x) #900

# train/val split for x
x_train = x[:700].reshape(70,10,1)
x_test = x[700:].reshape(-1,10,1)

x_train.shape #(70,10,1) - (batch_size, time steps, features)
x_test.shape # (20, 10, 1) - (batch_size, time steps, features)

#y_data
y = np.array([data[i+10] for i in range(len(data)-10)]) # 0 ~ 89
'''
10
11
 :
99
'''
len(y) # 90

# train/val split for y (70 vs 20)  
y_train = y[:70].reshape(70,1)
y_test = y[70:].reshape(20,1)
y_train.shape # (70, 1)
y_test.shape #  (20, 1)

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