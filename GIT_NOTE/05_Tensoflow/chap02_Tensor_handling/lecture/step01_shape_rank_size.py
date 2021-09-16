'''
Tensor의 차원(rank)과 shape 이해
 1. tensor shape
 2. tensor rank
 3. tensor size
 4. tensor reshape 
'''

import tensorflow as tf
print(tf.__version__) # 2.0.0

scala = tf.constant(1234)# 상수 scala
vector = tf.constant([1,2,3,4,5]) # 1 차원
matrix = tf.constant([ [1,2,3], [4,5,6] ]) # 2 차원
cube = tf.constant([[ [1,2,3], [4,5,6], [7,8,9] ]]) #3차원


# 1. tensor shape 
print(scala.get_shape()) # scalar.shape->() 
print(vector.get_shape()) #(5,)
print(matrix.get_shape()) #(2, 3)
print(cube.get_shape()) #(1, 3, 3)


print(scala)
print(vector)
print(matrix)
print(cube)
  
# 2. tensor rank
print('\ntensor rank')
print(tf.rank(scala)) 
print(tf.rank(vector)) 
print(tf.rank(matrix)) 
print(tf.rank(cube))

# 3. tensor size
print('\ntensor size')
print(tf.size(scala)) 
print(tf.size(vector)) 
print(tf.size(matrix)) 
print(tf.size(cube))

# 4. tensor reshape 
# print('\ntensor reshape')
cube_2d = tf.reshape(cube, (3, 3)) # 모양 변경 : 3d -> 2d 
print(cube_2d)


