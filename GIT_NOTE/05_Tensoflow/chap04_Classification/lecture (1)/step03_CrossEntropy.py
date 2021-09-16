"""
Entropy : 일반 용어 
 - 확률변수 p에 대한 불확실성의 측정 지수 
 - 값이 클 수록 일정한 방향성과 규칙성이 없는 무질서(chaos)를 의미
 - Entropy = -sum(p * log(p))
"""

import numpy as np

# 1. 불확실성이 큰 경우(p1: 앞면, p2: 뒷면)
p1 = 0.5; p2 = 0.5

entropy = -p1 * np.log2(p1) + -p2 * np.log2(p2)
print('entropy =', entropy) # entropy = 1.0

entropy = -(p1 * np.log2(p1) + p2 * np.log2(p2)) # 공통부호 정리
print('entropy =', entropy) # entropy = 1.0

# Entropy = -sum(Y * log(model))
entropy = -np.sum([p1 * np.log2(p1), p2 * np.log2(p2)]) # sum() 함수 
print('entropy =', entropy) # entropy = 1.0

# 전체 관측치의 오차 = -(sum(err) / n) = -mean(sum(Y * log(model)))
entropy = -np.mean(p1 * np.log2(p1) + p2 * np.log2(p2)) # 공통부호 정리
print('entropy =', entropy) # entropy = 1.0

# 분류기(classifier)에서 cost function 이용 
#cost = -tf.reduce_mean(Y * tf.log(model) + (1 - Y) * tf.log(1 - model))
# 식이 다른 이유 : 실제 model은 0~1 확률값(sigmoid)이고 정답은 10진수 


# 2. 불확실성이 작은 경우(x1: 앞면, x2: 뒷면) 
p1 = 0.9; p2 = 0.1

entropy = -p1 * np.log2(p1) + -p2 * np.log2(p2)
print('entropy =', entropy) # entropy = 0.4689955935892812

# p1 -> Y, p2 -> model 
Y = p1; model = p2
entropy = -(Y * np.log2(Y) + model * np.log2(model)) # 공통부호 정리
print('entropy =', entropy) # entropy = 0.4689955935892812

# Entropy = -sum(Y * log(model))
entropy = -np.sum([Y * np.log2(Y), model * np.log2(model)]) # sum() 함수 
print('entropy =', entropy) # entropy = 0.4689955935892812

# 전체 관측치의 오차 = -(sum(err) / n)
entropy = -np.mean(np.sum([Y * np.log2(Y), model * np.log2(model)])) # 공통부호 정리
print('entropy =', entropy) # entropy = 0.4689955935892812

'''
cross Entropy
  - 두 확률변수 x,y에서 x를 관찰한 후 y에 대한 불확실성 줄인다.
  - 딥러닝 분류기 : 정답 (Y) VS 예측치(y_pred)
      -> 정답(Y)을 관찰한 후 예측치의 손실을 줄인다.
      -> 정답(Y)과 예측치(y_pred) 간의 손실(LOSS) 값 계산
  - Cross 의미: Y=1, Y=0 일때 동시에 손실값 계산  
  - 식= -(Y*log(y_pred) + (1-Y)*log(1-y_pred))
  
  왼쪽 식: Y*log(y_pred) -> Y=1 일때 손실값 계산
  오른쪽 식: (1-Y)*log(1-y_pred)-> Y=0 일때 손실값 계산
'''

import tensorflow as tf 

model = [0.02,0.98] # model 예측값[0수렴, 1수렴]

Y =1 # 정답(Y)
for y_pred in model:
   loss_val = -( Y * tf.math.log(y_pred)) # Y=1 일때 손실값 계산
   print(loss_val.numpy())
'''
3.912023    -> 0.02 vs 1: 손실값 커짐
0.020202687 -> 0.98 vs 1: 손실값 작음
'''

Y =0 # 정답(Y)
for y_pred in model:
   loss_val = -((1-Y)*tf.math.log(1-y_pred)) # Y=0 일때 손실값 계산
   print(loss_val.numpy())
'''
0.020202687  -> 0.02 vs 0 : 손실값 적음
3.912023     -> 0.98 vs 0 : 손실값 큼
'''

# cross Entropy
Y =1 # 정답(Y) =1  or 0
for y_pred in model:
   loss_val = -(Y * tf.math.log(y_pred) + (1-Y)*tf.math.log(1-y_pred)) # Y=1 일때 손실값 계산
   print(loss_val.numpy())
'''
Y=1
3.912023     -> 0.02
0.020202687  -> 0.98
'''
Y =0 # 정답(Y) =1  or 0
for y_pred in model:
   loss_val = - tf.reduce_mean(Y * tf.math.log(y_pred) + (1-Y)*tf.math.log(1-y_pred)) # Y=0 일때 손실값 계산
   print(loss_val.numpy())

'''
Y=0
0.020202687 -> 0.02
3.912023    -> 0.98
'''

























