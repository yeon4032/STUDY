'''
KNN(K-Nearest Neighbor) 알고리즘
  - 학습과정 없음 
  - Euclidean 거리계산식
'''
import numpy as np
import tensorflow as tf

# x : 분류집단 
p1 = [1.2, 1.1] 
p2 = [1.0, 1.0]
p3 = [1.8, 0.8]
p4 = [2, 0.9]

x_data = np.array([p1, p2, p3, p4]) # 알려진 범주 
label = ['A','A','B','B'] # 분류범주(Y변수)
y_data = [1.6, 0.85] # y : 분류대상 

# x,y 변수 선언 : tensor 생성 
X = tf.constant(x_data, tf.float32) # 알려진 집단
Y = tf.constant(y_data, tf.float32) # 아려지지 않은 집단 (분류 대상)

# Euclidean 거리계산식 
distance = tf.math.sqrt(tf.math.reduce_sum(tf.math.square(X-Y),axis=1))
'''
브로드캐스팅 연산 : sqrt( sum( (x-y)^2 ) )
distance : 거리계산 결과 4개 원소를 갖는 vector 
'''
print(distance)
#tf.Tensor([0.47169903 0.61846584 0.20615523 0.40311286], shape=(4,), dtype=float32)

# 가장 가까운 거리 index 반환 
idx = tf.argmin(distance, 0) # input, dimension

print('분류 index :', idx.numpy())   
print('분류결과  : ', label[idx]) # 분류대상 : B
    
      
 
