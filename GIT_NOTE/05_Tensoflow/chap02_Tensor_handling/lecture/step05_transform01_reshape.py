'''
Tensor 모양변경  
 - tf.transpose : 전치행렬 
 - tf.reshape : 모양 변경 
'''

import tensorflow as tf
import numpy as np

print("numpy")
x = np.random.rand(2, 3)
print(x)

x_t = x.transpose() # 전치행렬 (행 과 열 변경)
print(x_t)

x_r = x.reshape([1,6])
print(x_r)

print("\ntensorflow")
x = tf.random.normal([2, 3])
print(x)
xt = tf.transpose(x)
print(xt)
x_r = tf.reshape(x, [1,6])
print(x_r)

#2d->3d
print(tf.reshape(tensor=x, shape=[2,1,3]))
'''
tf.Tensor(
[[[-1.3886037  -0.2500177   0.47068143]]

 [[-0.4018107  -0.91429067 -0.4475066 ]]], shape=(2, 1, 3), dtype=float32)
'''
