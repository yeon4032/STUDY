# -*- coding: utf-8 -*-
"""
step03_regression_formul.py

단순 선형회귀방정식
"""
import tensorflow as tf # ver 2.3 

# X, y 변수 : 상수 정의 -> 수정 불가
X = tf.constant(6.5) # 독립변수
y = tf.constant(5.2) # 종속변수(정답)

#a,b 변수: 변수 정의 -> 수정 가능 
a = tf.Variable(0.5) # 기울기
b = tf.Variable(1.5) # 절편

# 회귀 모델 
def linear_model(X): # 입력: X -> y 예측치
    y_pred = tf.linalg.multiply(X,a) + b # 회귀 방정식
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

'''
tf.square() : +부호, 오차 패널티 
tf.reduce_mean() : 각 관측치의 오차의 평균
'''

print('\n<<기울기, 절편 초기값>>')
print('기울기(a) =%.3f, 절편(b)=%.3f'%(a,b))
'''
<<기울기, 절편 초기값>>
기울기(a) =0.500, 절편(b)=1.500
'''


print('model error=%.3f'%(model_err(X,y)))
# model error=0.450

print('loss value=%.3f'%(loss_fu(X,y)))
# loss value=0.202
# 오류를 수정 or 줄이고 싶으면 a,b 의 값을 변경 또는 최적화 애야한다.



# [2차 기울기, 절편 수정]
a.assign(0.6)
b.assign(1.2)

print('\n<<기울기, 절편 수정(update)>>')
print('기울기(a) =%.3f, 절편(b)=%.3f'%(a,b))
'''
<<기울기, 절편 수정(update)>>
기울기(a) =0.600, 절편(b)=1.200
'''

print('model error=%.3f'%(model_err(X,y)))
# model error=0.100

print('loss value=%.3f'%(loss_fu(X,y)))
# loss value=0.010

'''
 - 최적의 기울기와 절편 update -> 손실(loss) 0에 수렴 
 - 딥러닝 최적화 알고리즘 : Adam
'''
