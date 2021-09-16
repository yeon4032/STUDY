# -*- coding: utf-8 -*-
"""
step06_softmax_classfier.py

활성함수: softmax함수
손실함수: cross entropy 함수
y_data: one hot encoding 변환
"""
import tensorflow as tf
from sklearn.metrics import accuracy_score # model 평가
import numpy as np

#1. x, y 공급 data 
# [털, 날개]
x_data = np.array(
    [[0, 0], [1, 0], [1, 1], [0, 0], [0, 1], [1, 1]]) # [6, 2]

# [기타, 포유류, 조류] : [6, 3] 
y_data = np.array([  # one hot encoding 
    [1, 0, 0],  # 기타[0]
    [0, 1, 0],  # 포유류[1]
    [0, 0, 1],  # 조류[2]
    [1, 0, 0],  # 기타[0]
    [1, 0, 0],  # 기타[0]
    [0, 0, 1]   # 조류[2]
])

# 2. X, Y 변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [관측치, 입력수] - [6, 2]
Y = tf.constant(y_data, tf.float32) # [관측치, 출력수] - [6, 3]

# 3. w,b 변수 정의: 초기값(난수) -> update  
w = tf.Variable(tf.random.normal(shape=[2,3])) #[입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[3])) # [출력수]

# 4. 회귀모델
def linear_model(X):
    model = tf.linalg.matmul(X,w) + b #[100,1] = X[100,4] @ w[4,1]
    return model

# 5. softmax 함수 : 다항분류 활성함수
def soft_fn(X):
    model=linear_model(X)
    y_pred = tf.nn.softmax(model)
    return y_pred 

# 6. 손실함수 : 정답(Y) vs 예측치(y_pred) -> 손실값 반환
def loss_fn(): # 인수 없음
    y_pred = soft_fn(X)
    # cross entropy : loss value
    loss = -tf.reduce_mean(Y*tf.math.log(y_pred) + (1-Y)*tf.math.log(1-y_pred))
    return loss

# 7. 최적화 객체
opt = tf.optimizers.Adam(learning_rate=0.1)

# 8. 반복학습
for step in range(100):
    opt.minimize(loss=loss_fn, var_list=[w,b])
    
    # 10 배수 단위 출력
    if (step+1) % 10 == 0:
        print('step=',(step+1),",loss val =", loss_fn().numpy())


### 최적화된 model 검증
y_pred =soft_fn(X).numpy()
print(y_pred)
'''
[[9.8715383e-01 1.1232670e-02 1.6134403e-03] - 1번 관측치
 [8.6457115e-03 9.6585196e-01 2.5502235e-02] - 2번 관측치
 [1.6007904e-02 6.8944502e-03 9.7709763e-01]
 [9.8715383e-01 1.1232670e-02 1.6134403e-03]
 [9.6724385e-01 4.2431613e-05 3.2713730e-02]
 [1.6007904e-02 6.8944502e-03 9.7709763e-01]] - 6번 관측치
'''

y_pred.sum(axis = 1)
# array([0.99999994, 0.9999999 , 1.        , 0.99999994, 1.        , 1.        ], dtype=float32)

# index 반환 : 확률 -> 10진수
y_pred = tf.argmax(y_pred, axis = 1)
print(y_pred.numpy()) # [0 1 2 0 0 2]

# 정답: one hot encoding -> 10진수
y_true = tf.argmax(Y, axis = 1)
print(y_true.numpy()) # [0 1 2 0 0 2]

acc = accuracy_score(y_true,y_pred)
print('accuracy=',acc)
# accuracy= 1.0
























