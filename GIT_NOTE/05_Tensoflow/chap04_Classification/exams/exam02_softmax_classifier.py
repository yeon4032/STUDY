'''
문) bmi.csv 데이터셋을 이용하여 다음과 같이 softmax classifier 모델을 생성하시오. 
   조건1> bmi.csv 데이터셋 
       -> x변수 : height, weight 칼럼 
       -> y변수 : label(3개 범주) 칼럼
    조건2> 딥러닝 최적화 알고리즘 : Adam
    조건3> learning rage : 0.001 or 0.005 선택(분류정확도 높은것) 
    조건4> 반복학습, step 단위로 loss : <출력결과> 참고 
    조건5> 분류정확도 출력
    조건6> 예측치와 정답 15개 출력   
    
  <출력 결과>
step = 500 , loss = 0.44498476
step = 1000 , loss = 0.34861678
step = 1500 , loss = 0.28995454
step = 2000 , loss = 0.24887484
step = 2500 , loss = 0.2177721
step = 3000 , loss = 0.19313334
step = 3500 , loss = 0.17303815
step = 4000 , loss = 0.15629826
step = 4500 , loss = 0.1421249
step = 5000 , loss = 0.12996733
========================================
accuracy = 0.9769
========================================
y_pred :  [0 0 1 1 1 1 0 2 0 2 1 2 1 0 2]
y_true :  [0 0 1 1 1 1 0 2 0 2 1 2 1 0 2]  
========================================
'''

import tensorflow as tf # ver1.x
from sklearn.preprocessing import minmax_scale # x data 정규화(0~1)
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
 
bmi = pd.read_csv('C:\\ITWILL\\5_Tensoflow\\data/bmi.csv')
print(bmi.info())

# 칼럼 추출 
col = list(bmi.columns)
print(col) 

# x,y 변수 추출 
x_data = bmi[col[:2]] # x변수

# x_data 정규화 
x_data = minmax_scale(x_data)


# label one hot encoding 
label_map = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
bmi["label"] = bmi["label"].apply(lambda x : np.array(label_map[x]))

y_data = list(bmi["label"]) # 중첩list : [[1,0,0], [1,0,0]]

# numpy 객체 변환 
x_data = np.array(x_data)
y_data = np.array(y_data) 

################# X,Y 데이터 전처리 완료 #####################

# 1. X,Y변수 정의 : 공급형 변수 
X = tf.constant(x_data, tf.float32)# [? 2]
Y = tf.constant(y_data, tf.float32)# [? 3]

# 2. w,b 변수 정의 
w = tf.Variable(tf.random.normal([2, 3])) # [입력수, 출력수]
b = tf.Variable(tf.zeros([3]))  # [출력수]

# 3. 회귀방정식 
def linear_model(X) : # train, test
    y_pred = tf.matmul(X, w) + b  # 행렬곱 : [None,3]*[3,1]=[None,1]
    return y_pred

# 4. softmax 활성함수 적용 
def soft_fn(X):
    y_pred = linear_model(X)
    soft = tf.nn.softmax(y_pred)
    return soft

# 5. 손실 함수 정의 : 손실계산식 수정 
def loss_fn() : #  인수 없음 
    soft = soft_fn(X) # 훈련셋 -> 예측치 : 회귀방정식  
    loss = -tf.reduce_mean(Y*tf.math.log(soft)+(1-Y)*tf.math.log(1-soft))
    return loss


# 6. 최적화 객체 
opt = tf.optimizers.Adam(learning_rate=0.005)

# 7. 반복학습 
for step in range(5000):
    opt.minimize(loss=loss_fn, var_list=[w,b])
    
    # 10 배수 단위 출력
    if (step+1) % 500 == 0:
        print('step=',(step+1),",loss val =", loss_fn().numpy())

# 8. 최적화된 model 검증 
y_pred =soft_fn(X).numpy()
print(y_pred)
'''

'''

y_pred.sum(axis = 1)
# array([0.99999994, 0.9999999 , 1.        , 0.99999994, 1.        , 1.        ], dtype=float32)

# index 반환 : 확률 -> 10진수
y_pred = tf.argmax(y_pred, axis = 1)
#print(y_pred.numpy()) 

# 정답: one hot encoding -> 10진수
y_true = tf.argmax(Y, axis = 1)
#print(y_true.numpy()) 

acc = accuracy_score(y_true,y_pred)
print('accuracy=',acc)
# accuracy= 1.0

print('y_pred :' ,y_pred[0:14].numpy())
print('y_true :',y_true[0:14].numpy())


