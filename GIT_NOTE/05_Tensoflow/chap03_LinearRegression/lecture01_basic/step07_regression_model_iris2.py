# -*- coding: utf-8 -*-
"""
다중선형회귀 모델: iris dataset
    - y변수 : 1 칼럼, X변수; 2~4 칼럼
    - 딥러닝 최적화 알고리즘: Adam 적용
    - learning_rate 적용 : 0.9 ~ 0.0001
    - epoch(step) : 반복학습
    - model 평가: MSE
"""
import tensorflow as tf # 딥러닝 최적화 알고리즘
from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error # 평가
from sklearn.preprocessing import minmax_scale # 정규화(0~1)

# 1. dataset load
X,y = load_iris(return_X_y=True)

# X 변수 정규화                
X_nor = minmax_scale(X)
type(X_nor) #numpy.ndarray

# y 변수 : 1칼럼, X변수 : 2~4칼럼 
y_data = X_nor[:,0] # 1칼럼
X_data = X_nor[:,1:] # 2~4칼럼 
y_data.shape # (150,)
X_data.shape # (150,3)


# 2. train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.3, random_state=123)

x_train.dtype # dtype('float64')

# 3. a, b 변수 정의: update 대상
tf.random.set_seed(123) # a,b 난수 seed 값 지정
a = tf.Variable(tf.random.normal(shape=[3,1],
                                 dtype=tf.float64)) # [입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[1],
                                 dtype=tf.float64)) # [출력수]
'''
X vs a  자료형 일치하기
#일치하지 않으면 회귀 모델에서 error 나온다. 

# 자료형 불일치 오류
InvalidArgumentError: cannot compute MatMul as input 
#1(zero-based) was expected to be a double tensor 
but is a float tensor [Op:MatMul]
'''

# 4. 회귀모델 정의 : 행렬곱 이용
def linear_model(X): # X:입력 -> y 예측치 : 출력
    y_pred = tf.linalg.matmul(X,a) + b
    return y_pred


# 5. 손실/비용 함수 정의 -MSE
def loss_fn() : # 인수 없음
    y_pred = linear_model(x_train)
    err= tf.math.subtract(y_train,y_pred)
    loss= tf.reduce_mean(tf.square(err))
    return loss

# 6. 최적화 객체 생성
opt = tf.optimizers.Adam(learning_rate=0.1)
'''
lr = 0.1 :빠른 속도 최소점 수렴
lr = 0.01 : 안정적으로 최소점 수렴
'''

print('초기값 : a=',a.numpy(), "b=",b.numpy())
'''
초기값 : a= [[ 1.88377388]
 [-2.41307987]
 [ 0.17593841]] b= [1.8437399]
'''

# 7. 반복학습: 100
loss_val=[] # 손실값 저장

for step in range(100):
    opt.minimize(loss=loss_fn, var_list=[a, b])
    # 10 배수 단위 출력
    if (step+1)%10 ==0:
        print('step=', (step+1), ',loss value =', loss_fn().numpy())
    
    loss_val.append(loss_fn().numpy())        
    

# step= 100 ,loss value = 0.05592662787911901

######최적화된 model 검증##############################################
print('최적화 : a=', a.numpy(), "b=",b.numpy())
'''
최적화 : a= [[-0.12988547]
 [-1.10126085]
 [ 1.00828198]] b= [0.54888224]
'''

# model 평가 : test set
y_pred = linear_model(x_test) # 예측치
MSE = mean_squared_error(y_test, y_pred) # (관측치, 예측치)
print('MSE=', MSE)
# MSE= 0.07703066016380891

# loss value 시각화
import matplotlib.pyplot as plt 

plt.plot(loss_val, 'r--')
plt.ylabel('loss value')
plt.xlabel('epochs(step)')
plt.show()







