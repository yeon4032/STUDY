# -*- coding: utf-8 -*-
"""
step01_keras_dnn_binary.py

 Keras :DNN model생성을 위한 고수준 API
 
 - iris dataset 이항분류기
X변수 : 스케이링
Y변수 : one hot encoding(binary) 
"""

from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # split
from sklearn.preprocessing import minmax_scale # x변수 : 스케일링(0~1)

from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense # DNN layer 구축

import tensorflow as tf
import numpy as np 
import random as rd

########################################################################
### keras 내부 seed 적용
########################################################################3
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)

# 1. dataset load & 전처리
X,y = load_iris(return_X_y=True)
X.shape #(150, 4)
y.shape #(150,)

# X변수 : 정규화(0~1) 
X = minmax_scale(X[:100])

# Y변수 : one hot encoding
y_one = to_categorical(y[:100])
print(y_one)
y_one.shape # (100, 2)
'''
[0, 1] <- class 0
[0, 1] <- class 1 
'''

# 2. 공급 data 생성 : 훈련용, 검증용
x_train, x_val, y_train, y_val = train_test_split(
    X, y_one, test_size=0.3,random_state=123)

# 3. Keras model
model = Sequential()

# 4. DNN model layer 구축
'''
model.add() : layer 추가 매소드
Dense(units= 뉴런수, input_shape=입력수, activation=활성홤수)  - 1층 
Dense(units= 뉴런수, activation=활성홤수)  - 2층 ~ n층 

'''

# hidden layer1 : [4, 8] -> [input, output] 
model.add(Dense(units=8, input_shape=(4,), activation = 'relu')) # 1층

# hidden layer1 : [8, 4] -> [input, output] 
model.add(Dense(units=4, activation = 'relu')) # 2층

# output layer: [4, 2] -> [input, output] 
model.add(Dense(units=2,activation ='sigmoid')) # 3층

# layer 확인
model.summary()

'''
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param -> (IN*OUT)+b
=================================================================
dense_3 (Dense)              (None, 8)                 40 =[(4*8)+8]      
_________________________________________________________________
dense_4 (Dense)              (None, 4)                 36 =[(8*4)+4]       
_________________________________________________________________
dense_6 (Dense)              (None, 2)                 10 =[(4*2)+2]       
=================================================================
Total params: 86
Trainable params: 86
Non-trainable params: 0
'''


# 5. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='adam',
              loss = 'binary_crossentropy', # y: one hot encoding 
              metrics=['accuracy'])
'''
optimizer : 죄적화 알고리즘('adma' or 'sdg')
loss : 비용함수('binary_crossentropy' or 'categorical_crossentropy' or 'mse')
metirics: 평가방법('accuracy' or 'mae')
'''

# 6. model training : train(105) vs val(45)
model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=30, # 반복학습
          verbose=1, # 출력여부
          validation_data=(x_val, y_val)) # 검증셋

# 7. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)

