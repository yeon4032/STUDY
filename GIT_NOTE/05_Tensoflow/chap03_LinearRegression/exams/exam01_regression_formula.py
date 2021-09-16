'''
문1) 다음과 같이 다중선형회귀방정식으로 모델의 예측치와 오차를 이용하여 
     비용함수를 정의하고 결과를 출력하시오.

    <조건1> a변수[기울기] : Variable()이용 표준정규분포 난수 상수 4개
    <조건2> b변수[절편] : Variable()이용 표준정규분포 난수 상수 1개     
    <조건3> model 예측치 : pred_Y = (X * a) + b -> 행렬곱 함수 적용  
    <조건4> model 손실함수 출력 
        -> 손실함수는 python 함수로 정의 : 함수명 -> loss_fn(err)
    <조건5> 결과 출력 : << 출력 예시 >> 참고     

<< 출력 예시 >>    
a[기울기] =
[[-0.8777014 ]
 [-2.0691    ]
 [-0.47918326]
 [ 1.5532079 ]]
b[절편] = [1.4863125]
Y[정답] = 1.5
pred_Y[예측치] = [[0.7273823]]
loss function = 0.59693813 
'''

import tensorflow as tf 

# 1. X,Y 변수 정의 
X = tf.constant([[1.2, 2.2, 3.5, 4.2]]) # [1,4] - 입력수 : 4개 
Y = tf.constant(1.5) # 출력수(정답) - 1개  

# 2. 기울기(a), 절편(b) 변수 정의 
a = tf.Variable(tf.random.normal([4,1])) # [내용 채우기] : 초기값 지정 
b = tf.Variable(tf.random.normal([1])) # [내용 채우기] : 초기값 지정 

# 3. model 예측치/오차/비용
y_pred = tf.matmul(X, a) + b # 예측치
err = tf.subtract(Y, y_pred) # 오차

# 4. 손실함수 정의 
# model 오차

def loss_fu(err):
    loss = tf.reduce_mean(tf.square(err)) # MSE
    return loss


# 5. 결과 출력 : [내용 채우기]
print('<<기울기, 절편 초기값>>')
print('기울기(a)=',a.numpy(),'\n절편(b)=',b.numpy(),'\nY[정답] =',Y.numpy())
print('pred_Y[예측치] =',y_pred)
print('loss value=%.3f'%(loss_fu(err)))

'''
<<기울기, 절편 초기값>>
기울기(a)= 
[[ 0.19361258]
 [ 0.61843103]
 [ 1.67869   ]
 [-2.5004973 ]] 
절편(b)= [1.8860607] 
Y[정답] = 1.5
pred_Y[예측치] = tf.Tensor([[-1.1477299]], shape=(1, 1), dtype=float32)
loss value=7.010
'''



