# -*- coding: utf-8 -*-
"""
문) boston 데이터셋을 이용하여 다음과 같이 Keras DNN model layer을 
    구축하고, model을 학습하고, 검증(evaluation)하시오. 
    <조건1> 4. DNN model layer 구축 
         1층(hidden layer1) : units = 64
         2층(hidden layer2) : units = 32
         3층(hidden layer3) : units = 16 
         4층(output layer) : units=1
    <조건2> 6. model training  : 훈련용 데이터셋 이용 
            epochs = 50
    <조건3> 7. model evaluation : 검증용 데이터셋 이용     
"""
from sklearn.datasets import load_boston  # dataset
from sklearn.model_selection import train_test_split # split
from sklearn.preprocessing import minmax_scale # 정규화(0~1) 
from sklearn.metrics import mean_squared_error, r2_score


# keras model 관련 API
import tensorflow as tf # ver 2.0
from tensorflow.keras import Sequential # model 생성 
from tensorflow.keras.layers import Dense # DNN layer
print(tf.keras.__version__) # 2.2.4-tf


###karas 내부 weight seed 적용
import numpy as np
import random as rd
tf.random.set_seed(123) # global seed 값
np.random.seed(123) # numpy seeed 
rd.seed(123) # random seed

# 1. x,y data 생성 
X, y = boston = load_boston(return_X_y=True)
X.shape # (506, 13)
y.shape # (506,)

# y 정규화 
X = minmax_scale(X)
y = minmax_scale(y)

# 2. 공급 data 생성 : 훈련용, 검증용 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size = 0.5)
x_train.shape 
y_train.shape 


# 3. keras model
model = Sequential() 
print(model) # object info


# 4. DNN model layer 구축 
'''
   <조건1> 4. DNN model layer 구축 
         1층(hidden layer1) : units = 64
         2층(hidden layer2) : units = 32
         3층(hidden layer3) : units = 16 
         4층(output layer) : units=1
'''
model.add(Dense(units=64, input_shape=(13,), activation='relu')) # 1층 
model.add(Dense(units=32, activation='relu')) # 2층 
model.add(Dense(units=16, activation='relu')) # 3층 
model.add(Dense(units=1)) # 4층

# 5. model compile : 학습과정 설정(다항 분류기)
model.compile(optimizer = 'adam', 
         loss = 'mse', 
         metrics = ['mae'])


# model layer 확인 
model.summary()


# 6. model training 
model.fit(x=x_train,y=y_train,
          epochs=50,
          verbose = 1,
          validation_data=(x_val,y_val))


# 7. model evaluation : test dataset
loss_val,mae_val = model.evaluate(x_val,y_val)
print('loss value =',loss_val) # 
print('mae_val =',mae_val) #

# 8. model test: 실제 dataset 적용
print('#### model test #####')
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5,random_state=123)

y_pred=model.predict(x_test) # 예측치
y_true=y_test # 관측치

mse = mean_squared_error(y_true,y_pred )
score = r2_score(y_true, y_pred)
print('mse=',mse)
print('score=', score)

