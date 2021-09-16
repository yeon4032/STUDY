# -*- coding: utf-8 -*-
"""
step06_regression_model_iris.py
    - csv file data 이용
    - 정규화: 입력변수 x 에 대한 정규화
"""
import tensorflow as tf # 최적화 알고리즘
import pandas as pd # csv file
from sklearn.metrics import mean_squared_error # model 평가
from sklearn.preprocessing import minmax_scale # 정규화

iris = pd.read_csv('C:\\ITWILL\\5_Tensoflow\\data\\iris.csv')
print(iris.info())

#1. X,y 생성
x_data = iris['Sepal.Length']
y_data = iris['Petal.Length']

x_data.mean() #5.843333333333334
y_data.mean() #3.7580000000000005


# 2. X 정규화
X=minmax_scale(x_data)
X.mean() # 0.42870370370370364

# other way for normalize
y_data.max() #6.9
y = y_data/6.9
y.mean() # 0.5446376811594204

# 상수 생성 : float64 -> float32 변환
X=tf.constant(X,dtype=tf.float32)
y=tf.constant(y,dtype=tf.float32)

# 3. a,b 변수 정의: 초기값 - 난수 -> update
a = tf.Variable(tf.random.normal([1])) # 기울기=입력수 : 난수
b = tf.Variable(tf.random.normal([1])) # 절편 = 출력수  : 난수


# 4. 회귀 모델 
def linear_model(X): # 입력: X -> y 예측치
    y_pred = tf.math.multiply(X,a) + b # 회귀 방정식 : 행렬곱
    return y_pred


# 5. 손실/비용 함수(loss function) : 손실반환(MSE) 
def loss_fn(): # 인수 없음
    y_pred=linear_model(X) # 예측치
    err = tf.math.subtract(y, y_pred)
    loss = tf.reduce_mean(tf.square(err)) # MSE
    return loss

# 6. model 최적화 객체 : 오차의 최소점을 찾는 객체 
optimizer = tf.optimizers.Adam(learning_rate=0.5) # learning_rate :0.9~0.0001(e-04) 
# 학습률 : 클수록 수렴(오차=0)속도 빠름 but 정밀도는 낮아진다.


print(f'기울기(a)초기값 = {a.numpy()}, 절편(b)초기값={b.numpy()}')

# 7. 반복학습 : 100 회
for step in range(100) :
    optimizer.minimize(loss=loss_fn, var_list=[a,b]) # (손실값, update 대상변수)

    # step 단위 -> 손실값 -> a,b 출력
    print('step=',(step+1), ",loss value=",loss_fn().numpy())
    # a, b 변수 update
    print(f'기울기(a) = {a.numpy()}, 절편(b)={b.numpy()}')

'''
step= 1 ,loss value= 1.1369102
기울기(a)초기값 = [1.0259533], 절편(b)초기값=[-1.6607504]
 :
step= 100 ,loss value= 0.015609413
기울기(a) = [0.96969354], 절편(b)=[0.12745348]
'''

# 8.. 최적화된 model 검증

# 1) 회귀선
import matplotlib.pyplot as plt

y_pred= linear_model(X) # 예측치

plt.plot(X, y, 'bo') # 산점도
plt.plot(X,y_pred,'r-') #회귀선
plt.show()

# MSE
mse = mean_squared_error(y,y_pred)
print('mse=',mse) # mse= 0.015609413



