# -*- coding: utf-8 -*-
"""
step07_softmax_classfier_iris.py

Softmax +iris
활성함수: softmax함수
손실함수: cross entropy 함수
y_data: one hot encoding 변환
"""
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder # y_data -> encoding
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import accuracy_score # model 평가

tf.random.set_seed(123) # seed값 고정 - 동일한 결과

#1. x, y 공급 data
X,y = load_iris(return_X_y=True)
X.shape
x_data = X #[150,4]

# x변수 정규화
x_data = minmax_scale(x_data)

#[class0, class1, class2] : [150,3]
y_data = y
y_data.shape #(150,)
'''
0~2
'''

#one hot encoding
obj = OneHotEncoder()
y_data = obj.fit_transform(y_data.reshape([150,1])).toarray()
'''
1 0 0 <- class0
0 1 0 <- class1
0 0 1 <- class2
'''

# 2. X, Y 변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [관측치, 입력수] - [150, 4]
Y = tf.constant(y_data, tf.float32) # [관측치, 출력수] - [150, 3]

# 3. w,b 변수 정의: 초기값(난수) -> update  
w = tf.Variable(tf.random.normal(shape=[4,3])) #[입력수, 출력수]
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

y_pred.sum(axis = 1)
# array([0.99999994, 0.9999999 , 1.        , 0.99999994, 1.        , 1.        ], dtype=float32)

# index 반환 : 확률 -> 10진수
y_pred = tf.argmax(y_pred, axis = 1)
# print(y_pred.numpy()) 

# 정답: one hot encoding -> 10진수
y_true = tf.argmax(Y, axis = 1)
# print(y_true.numpy()) 

acc = accuracy_score(y_true,y_pred)
print('accuracy=',acc)
# accuracy= 1.0
























