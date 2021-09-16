# -*- coding: utf-8 -*-
"""
step02_keras_history.py

keras history: model 학습과정과 검증 과정의 손실값 기억하는 기능
"""
# dataset
from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import mean_squared_error,r2_score # 평가

# keras model
import tensorflow as tf
from tensorflow.keras import Sequential # Keras model
from tensorflow.keras.layers import Dense # DNN layer 추가
import numpy as np
import random as rd

# tensorflow version
print(tf.__version__) # 2.3.0
# keras version
print(tf.keras.__version__) # 2.4.0

###karas 내부 weight seed 적용
tf.random.set_seed(123) # global seed 값
np.random.seed(123) # numpy seeed 
rd.seed(123) # random seed

# 1. dataset load
X,y = load_iris(return_X_y= True)
y # 0~2 

# 2. 공급 dataset 생성: 훈련셋, 검정셋
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3,random_state=123)

x_train.shape # (105, 4)
x_train.dtype # dtype('float64')

y_train.shape #(105,)

# 3. DNN model 생성
model = Sequential() # keras model 
print(model)
# <tensorflow.python.keras.engine.sequential.Sequential object at 0x000001F7E76A2D00>

# DNN model layer 구축
'''
model.add(Dense(unit수, input_shape,activation)): hidden1
model.add(Dense(unit수, activation)): hidden 1 ~ hidden n
'''

#######################################################################################
####### hidden layer 2개 : unit = 12, unit=6
#######################################################################################
#뉴런은 외부의 입력데이터와 가중치를 받아서 연산한 후 또 다른 뉴런으로 결과를 넘기는 역할을 합니다.
#최적화 알고리즘은 이러한 뉴런의 연산 결과를 이용하여 이전 레이어의 가중치를 수정하는데 이용합니다.

# hidden Layer 1:unit = 12-> w[4(입력 x변수),12(unit)]
model.add(Dense(units=12, input_shape=(4,), activation='relu')) # 1층 
model.add

# hidden Layer 2:unit = 6 -> w[12(1층 unit), 6(2층 unit)] 
model.add(Dense(units=6, activation='relu')) # 2층 

# output layer ->w[6,1]
model.add(Dense(units=1)) # 3층

print(model.summary())
'''
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param # (input*output)+b(절편)   
=================================================================
dense (Dense)                (None, 12)                60 =(4*12)+12       
_________________________________________________________________
dense_4 (Dense)              (None, 6)                 78 =(12*6)+ 6      
_________________________________________________________________
dense_5 (Dense)              (None, 1)                 7  = (6*1) + 1      
=================================================================
Total params: 145
Trainable params: 145
Non-trainable params: 0
'''

# 4. model complie:학습 과정 설정
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
'''
optimizer : 최적화 알고리즘('adam' or 'sgd')
loss : 손실함수('mse', or 'crossentropy')
metrics= 평가방법('mae' or 'accuracy')
'''

# 5. [수정] model training: train(105) vs test(45)
model_fit=model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=100,# 학습횟수
          verbose = 1, # 출력여부
          validation_data=(x_val,y_val)) # 검증셋

# 6.model evaluation: validation data
loss_val,mae = model.evaluate(x_val,y_val)
print('loss value=',loss_val) # loss value= 0.04995540902018547
print('mae=',mae) # mae= 0.16836898028850555
'''
loss value= 0.04995540902018547
mae= 0.16836898028850555
'''

# [추가] 7. model history : epoch에 따른 손실값 확인
#epochs=100이면 훈련셋을 100번 반복하여 학습한다는 의미이고 이 과정에서 손실값을 history 기능에 의해서 저장하게 됩니다.
# 그 저장된 데이터를 가지고 오는 역할
print(model_fit.history.keys())
#dict_keys(['loss', 'mae', 'val_loss', 'val_mae'])
print(model_fit.history['loss']) # 훈련셋 손실값
print(model_fit.history['val_loss']) # 검증셋 손실값

#train loss val vs val loss val
#그래프를 이용해 train loss value(훈련셋) 와 val loss value(검증셋)을 비교해서 예측값의 정확도를 확인하는 작업
# overfitting 도 확인 가능
# epochs 수 결정에 사용 가능
import matplotlib.pyplot as plt
plt.plot(model_fit.history['loss'], 'y', label='train loss value')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss value')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

#model평가 : mae vs val_mae
plt.plot(model_fit.history['mae'], 'y', label='train mae')
plt.plot(model_fit.history['val_mae'], 'r', label='val_mae')
plt.xlabel('epochs')
plt.ylabel('mae')
plt.legend(loc='best')
plt.show()


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
'''
mse= 0.06588136840917383
score= 0.9101399861053339
'''

# 9. model save & load: HDF5 파일 형식

# 1) model save
model.save('keras_model_iris.h5')

# 2) model load
from tensorflow.keras.models import load_model
my_model=load_model('keras_model_iris.h5')
y_pred = my_model.predict(x_test)

mse = mean_squared_error(y_true,y_pred)
score=r2_score(y_true,y_pred)
print('mse=',mse)
print('score=',score)


