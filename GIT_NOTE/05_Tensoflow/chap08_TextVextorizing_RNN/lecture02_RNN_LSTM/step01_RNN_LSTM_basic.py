# -*- coding: utf-8 -*-
"""
step01_RNN_LSTM_basic.py

RNN model 
 - 순환신경망 모델
 
 google 개발자 오류때문에 lib에있는 array_ops.py파일을 tensorflow강의 chap08/data 에서  array_ops.로 바꾸어준다.
 C:\\Users\\82104\\anaconda3\\envs\\tensorflow\\Lib\site-packages\\tensorflow\\python\\ops
 (<-array_ops.py 파일교체)
"""

import tensorflow as tf # seed value
import numpy as np # ndarray
from tensorflow.keras import Sequential # model
from tensorflow.keras.layers import SimpleRNN, Dense, LSTM # RNN layer

tf.random.set_seed(123) # seed값 지정

# many-to-one : word(4개) -> 출력(1개)
X = [[[0.0], [0.1], [0.2], [0.3]],
     [[0.1], [0.2], [0.3], [0.4]],
     [[0.2], [0.3], [0.4], [0.5]],
     [[0.3], [0.4], [0.5], [0.6]],
     [[0.4], [0.5], [0.6], [0.7]],
     [[0.5], [0.6], [0.7], [0.8]]] 

Y = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


X = np.array(X)
Y = np.array(Y)

X.shape # (6, 4, 1) - (batch_size, time_steps, features)
''' 
batch_size:훈련/테스트 과정에서 1회 공급되는 data수
time_steps: 문장(sequence)에 포함된 토큰(단어)의 수
features : 한 time_step(시간 단계)에서 사용되는 차원 수
'''

input_shape = (4, 1)

model = Sequential()

#RNN layer 추가
#model.add(SimpleRNN(units=30, input_shape=input_shape, activation='tanh'))

#LSTM
model.add(LSTM(units=30, input_shape=input_shape, activation='tanh'))

#hidden layer 추가가능 (복잡한 계산의 경우)

# DNN layer 추가
model.add(Dense(units=1)) # 출력 : 회귀모델 - MSE, MAE
#최종 출력은 예측된 숫자나 class 분류 결과이기 때문에 DNN을 이용합니다.

# model 학습환경
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# model training
model.fit(X,Y, epochs=100, verbose=1)

#model prediction
y_pred = model.predict(X)
print(y_pred)
'''
SimpleRNN <- simple 한 layer 의 경우 예측력 좋음
[[0.37206325] - 0.4
 [0.49444115] - 0.5
 [0.60844016] - 0.6
 [0.7126006 ] - 0.7
 [0.8061328 ] - 0.8
 [0.8888123 ]] - 0.9
'''

'''
LSTM <- 복잡한 layer의 경우 예측력 좋음
[[0.43407246] - 0.4
 [0.51645815] - 0.5
 [0.6017104 ] - 0.6
 [0.68928045] - 0.7
 [0.77856946] - 0.8
 [0.8689499 ]] - 0.9
'''