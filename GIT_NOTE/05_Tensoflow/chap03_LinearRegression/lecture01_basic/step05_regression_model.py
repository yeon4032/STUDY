# -*- coding: utf-8 -*-
"""
step05_regression_model.py
    - 회귀모델: 딥러닝 최적화 알고리즘
"""

import tensorflow as tf # 딥러닝 최적화 알고리즘
import numpy as np # dataset 생성 

#따라서 행은 관측치, 열은 입력(feature)수라고 할 수 있습니다
#그런데 list로 1차원을 정의해서 입력으로 사용되면 기본적으로 열은 1개이고 
#원소의 수는 관측치(열)가 됩니다.
#feature수 = 입력수

# 1. X,y변수 생성
X = np.array([1, 2, 3]) # 독립변수(입력) : [n] -> n:관측치
y = np.array([2, 4, 6]) # 종속변수(출력) : [n] -> n:관측치
X.shape
# 2. a,b 변수 정의
a = tf.Variable(tf.random.normal([1])) # 기울기 : 난수
b = tf.Variable(tf.random.normal([1])) # 절편  : 난수

# 3. 회귀 모델 
def linear_model(X): # 입력: X -> y 예측치
    y_pred = tf.math.multiply(X,a) + b # 회귀 방정식 : 행렬곱
    return y_pred


# 4. 손실/비용 함수(loss function) : 손실반환(MSE) 
def loss_fn(): # 인수 없음
    y_pred=linear_model(X) # 예측치
    err = tf.math.subtract(y, y_pred)
    loss = tf.reduce_mean(tf.square(err)) # MSE
    return loss

# 5. model 최적화 객체 : 오차의 최소점을 찾는 객체 
optimizer = tf.optimizers.Adam(learning_rate=0.5) # learning_rate :0.9~0.0001(e-04) 
# 학습률 : 클수록 수렴(오차=0)속도 빠름 but 정밀도는 낮아진다.

print(f'기울기(a)초기값 = {a.numpy()}, 절편(b)초기값={b.numpy()}')

# 6. 반복학습 : 100 회
for step in range(100) :
    optimizer.minimize(loss=loss_fn, var_list=[a,b]) # (손실값, update 대상변수)

    # step 단위 -> 손실값 -> a,b 출력
    print('step=',(step+1), ",loss value=",loss_fn().numpy())
    # a, b 변수 update
    print(f'기울기(a) = {a.numpy()}, 절편(b)={b.numpy()}')


# 7. 최적화된 model 검증

# 1) 회귀선
import matplotlib.pyplot as plt

y_pred= linear_model(X) # 예측치

plt.plot(X, y, 'bo') # 산점도
plt.plot(X,y_pred,'r-')#회귀선
plt.show()

#y vs y_pred
print('y_pred=', y_pred.numpy())
print('y=',y)
'''
y_pred= [1.9956156 4.0060315 6.0164475]
y= [2 4 6]
'''

# test set 적용 -> 학습 되지 않은 데이터를 가지고 예측 가능
X_test=[2.5]

y_pred=linear_model(X_test)
print('X=2.5:','y=',y_pred.numpy())
# X=2.5: y= [5.0112395]
















