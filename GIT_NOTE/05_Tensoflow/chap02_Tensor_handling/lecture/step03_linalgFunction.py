'''
선형대수 연산 함수   
 tf.diag : 대각행렬 -> tf.linalg.diag(x)  
 tf.matrix_determinant : 정방행렬의 행렬식 -> tf.linalg.det(x)
 tf.matrix_inverse : 정방행렬의 역행렬 -> tf.linalg.inv(x)
 tf.matmul : 두 텐서의 행렬곱 -> tf.linalg.matmul(x, y)
'''

import tensorflow as tf
import numpy as np

# 정방행렬 데이터 생성 
x = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 
y = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 
print(x)
'''
[[0.50106566 0.63370173]
 [0.39903798 0.13022766]]
'''
print(y)
'''
[[0.48376994 0.98264968]
 [0.48940723 0.64145439]]
'''

dia = tf.linalg.diag(x) # 대각행렬 
mat_deter = tf.linalg.det(x) # 정방행렬의 행렬식  
mat_inver = tf.linalg.inv(x) # 정방행렬의 역행렬
mat = tf.linalg.matmul(x, y) # 행렬곱 반환 

print(x)
print(dia.numpy())
'''
[[[0.50106566 0.        ]
  [0.         0.63370173]]

 [[0.39903798 0.        ]
  [0.         0.13022766]]]
'''

print(mat_deter.numpy()) #-0.18761845268614205
'''
X =  [[a b]
     [ c d]]
정방행렬 행렬식 = ad - bc
'''
print(mat_inver.numpy())
'''
[[-0.694109    3.37760875]
 [ 2.12685894 -2.670663  ]]

#공식
X =  [[a b]
     [ c d]]

X^-1= 1/(ad-bc) *[[d -b]
                 [-c  a]]
'''
print(mat.numpy())
'''
[[0.55253871 0.89886277]
 [0.25677694 0.47564965]]
#공식(행렬곱)
행렬곱=X*X^-1
'''
# 단위행렬: one-hot-encoding(2진수)
tf.linalg.eye(2).numpy()
'''
array([[1., 0.], - 'cat'
       [0., 1.]],- 'dog' dtype=float32)>
'''

# 다항분류
class_re = tf.linalg.eye(3).numpy()
'''
array([[1., 0., 0.], - class0
       [0., 1., 0.], - class1
       [0., 0., 1.]],- class2  dtype=float32)
'''

#decoding
class_re.argmax(axis=0) #[0, 1, 2]





























