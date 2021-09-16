'''
(base) > conda activate tensorflow
(tensorflow) > conda install matplotlib
'''

import tensorflow as tf # ver2.x
import matplotlib.pyplot as plt # chart


#######################
# 난수 생성 함수 
#######################
''' 
 ver1.x : tf.random_normal(shape, mean, stddev) : 평균,표준편차 정규분포
 ver2.0 : tf.random.normal(shape, mean, stddev)
 ver1.x : tf.truncated_normal(shape, mean, stddev) : 표준편차의 2배 수보다 큰 값은 제거하여 정규분포 생성 
 ver2.0 : tf.truncated.normal(shape, mean, stddev) 
 ver1.x : tf.random_uniform(shape, minval, maxval) : 균등분포 난수 생성
 ver2.0 : tf.random.uniform(shape, minval, maxval) 
 ver1.x : tf.random_shuffle(value) : 첫 번째 차원 기준으로 텐서의 원소 섞기
 ver2.0 : tf.random.shuffle(value)
 ver1.x : tf.set_random_seed(seed) : 난수 seed값 설정 
 ver2.0 : tf.random.set_seed(seed)
'''

# 2행3열 구조의 표준정규분포를 따르는 난수 생성  
norm = tf.random.normal([2,3], mean=0, stddev=1) # default : 0, 1
print(norm) # 객체 보기 

uniform = tf.random.uniform([2,3], minval=0, maxval=1) # default : 0, 1
print(uniform) # 객체 보기 

matrix = [[1,2], [3,4], [5,6]] # # (3, 2)
shuff = tf.random.shuffle(matrix) 
print(shuff) # 첫번째 차원(3행 단위로 섞음) 

# seed값 지정 : 이전 난수와 동일한 난수 생성   
tf.random.set_seed(1234)
a = tf.random.uniform([1]) # seed 생략 
b = tf.random.normal([1]) # seed 생략 

print(a)  
print(b)  

####################################
# 2. 정규분포, 균등분포 차트 시각화
####################################

# 정규분포(평균:0, 표준편차:2) 
norm = tf.random.normal([1000], mean=175, stddev=5.5)  # N(175, 5.5^2)
plt.hist(norm.numpy()) # numpy() 추가 
plt.show()
 
# 균등분포(0~1) 
uniform = tf.random.uniform([1000], minval=2.5, maxval=5.5) # 0 ~ 1
plt.hist(uniform.numpy()) # # numpy() 추가
plt.show() 
