# -*- coding: utf-8 -*-
"""
step04_sigmiod_classfier.py

활성함수 : sigmoid 함수 - 이항분류
손실함수 : cross entropy 함수 - 손실값
"""

import tensorflow as tf
from sklearn.metrics import accuracy_score # model 평가

# 1. x, y 공급 data 
# x변수 : [hours, video]
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] # [6,2]

# y변수 : binary data (fail or pass)
y_data = [[0], [0], [0], [1], [1], [1]] # [6, 1] : 이항분류 

# 2. X, Y 변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [관측치, 입력수] - [6, 2]
Y = tf.constant(y_data, tf.float32) # [관측치, 출력수] - [6, 1]


# 3. w,b 변수 정의: 초기값(난수) -> update  
w = tf.Variable(tf.random.normal(shape=[2,1])) #[입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[1])) # [출력수]

# 4. 회귀모델
def linear_model(X):
    model = tf.linalg.matmul(X,w) + b #회귀방정식
    return model

# 5. sigmoid 함수 : 이항분류 활성함수
def sig_fn(X):
    model=linear_model(X)
    y_pred = tf.nn.sigmoid(model)
    return y_pred 

# 6. 손실함수 : 정답(Y) vs 예측치(y_pred) -> 손실값 반환
def loss_fn(): # 인수 없음
    y_pred = sig_fn(X)
    # cross entropy : loss value
    loss = -tf.reduce_mean(Y*tf.math.log(y_pred) + (1-Y)*tf.math.log(1-y_pred))
    return loss

# 7. 최적화 객체
opt = tf.optimizers.Adam(learning_rate=0.5)

# 8. 반복학습
for step in range(100):
    opt.minimize(loss=loss_fn, var_list=[w,b])
    
    # 10 배수 단위 출력
    if (step+1) % 10 == 0:
        print('step=',(step+1),",loss val =", loss_fn().numpy())


### 최적화된 model 검증
y_pred = sig_fn(X) # sigmoid 함수
print(y_pred.numpy())
'''
[[0.00211871]
 [0.06858039]
 [0.08671191]
 [0.90795636]
 [0.99131775]
 [0.997738  ]]
'''


# cut off=0.5 적용 : T/F -> 1.0/0.0
y_pred = tf.cast(sig_fn(X).numpy() > 0.5, dtype=tf.float32)
print(y_pred.numpy())
'''
[[0.]
 [0.]
 [0.]
 [1.]
 [1.]
 [1.]]
'''

acc = accuracy_score(Y,y_pred)
print('accuracy =',acc)
#accuracy = 1.0





















