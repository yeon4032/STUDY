# -*- coding: utf-8 -*-
"""
step04_regression_formul2.py

다중선형회귀방정식: X(입력) 2개 이상
y_pred = (X1*a1 +X2*a2) + b
y_pred = tf.matmul(X,a) + b
"""

import tensorflow as tf


# X,y 변수 정의 : 상수
X=[[1.0,2.0]] #독립변수 (1,2)
y=2.5 # 종속변수 (정답)
print(X)
# a,b 변수 정의: 변수  (수정 가능)
a = tf.Variable(tf.random.normal([2,1])) # 2개 난수: (2,1)
b = tf.Variable(tf.random.normal([1])) # 1개 난수

# 회귀 모델 
def linear_model(X): # 입력: X -> y 예측치
    y_pred = tf.linalg.matmul(X,a) + b # 회귀 방정식 : 행렬곱
    return y_pred

# model 오차
def model_err(X,y): # 입력 : X,y -> 오차(error)
    y_pred=linear_model(X) # 예측치
    err = tf.math.subtract(y, y_pred) # 정답 - 예측치
    return err

# 손실함수(loss function) : 손실반환(MSE)
def loss_fu(X,y):
    err = model_err(X,y) # 오차
    loss = tf.reduce_mean(tf.square(err)) # MSE
    return loss


print('<<기울기, 절편 초기값>>')
print('기울기(a)=',a.numpy(),'\n절편(b)=',b.numpy())
print('model error=%.3f'%(model_err(X,y)))
print('loss value=%.3f'%(loss_fu(X,y)))

# varibale 값이 임의 값이기 때문에 variable 실행 할때 마다 
#var값이 변하고 이로 기울기,절편,오차,등이 계속 변한다.
#1
'''
<<기울기, 절편 초기값>>
기울기(a)= [[-0.50711364]
 [ 1.0035167 ]] 
절편(b)= [-1.1458942]
model error=2.146
loss value=4.605
'''
#2
'''
<<기울기, 절편 초기값>>
기울기(a)= [[-0.09344053]
 [-0.15483168]] 
절편(b)= [-2.3115234]
model error=5.215
loss value=27.192
'''

# 다음 step 에서는 이러한 variable 의 특성을 이용해서 알고리즘을 바탕으로 학습을 시키고 
# 최고로 이상적인 varaible 을 찾는 프로그램방법을 학습해보자

