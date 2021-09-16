# -*- coding: utf-8 -*-
"""
step05_sigmiod_classfier_iris.py

dataset :iris
활성함수 : sigmoid 함수 - 이항분류
손실함수 : cross entropy 함수 - 손실값
"""
import tensorflow as tf
from sklearn.datasets import load_iris # dataset
from sklearn.preprocessing import minmax_scale # x변수 정규화
from sklearn.metrics import accuracy_score # model 평가


# 1. x, y 공급 data
X, y = load_iris(return_X_y=True) 

# x변수 : iris(4)
x_data = X[:100] # 
x_data.dtype #tf.float32
x_data.shape # (100, 4)

# x변수 정규화
x_data = minmax_scale(x_data) # 0~1

# y변수 : iris(5)
y_data = y[:100] # class0,class1
y_data.shape # (100,)

#차원 일치: 1d -> 2d
y_data = y_data.reshape(100,1)


# 2. X, Y 변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [관측치, 입력수] - [100, 4]
Y = tf.constant(y_data, tf.float32) # [관측치, 출력수] - [100, 1]


# 3. w,b 변수 정의: 초기값(난수) -> update  
w = tf.Variable(tf.random.normal(shape=[4,1])) #[입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[1])) # [출력수]

# 4. 회귀모델
def linear_model(X):
    model = tf.linalg.matmul(X,w) + b #[100,1] = X[100,4] @ w[4,1]
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
'''
Y(2차원) vs y_pred(2차원)
'''

# 7. 최적화 객체
opt = tf.optimizers.Adam(learning_rate=0.1)

# 8. 반복학습
for step in range(500):
    opt.minimize(loss=loss_fn, var_list=[w,b])
    
    # 10 배수 단위 출력
    if (step+1) % 10 == 0:
        print('step=',(step+1),",loss val =", loss_fn().numpy())

### 최적화된 model 검증
# cut off=0.5 적용 : T/F -> 1.0/0.0
y_pred = tf.cast(sig_fn(X).numpy() > 0.5, dtype=tf.float32)
print(y_pred.numpy())

acc = accuracy_score(Y,y_pred)
print('accuracy =',acc)
#accuracy = 1.0
