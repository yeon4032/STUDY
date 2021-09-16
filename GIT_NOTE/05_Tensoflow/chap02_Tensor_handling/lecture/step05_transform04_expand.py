'''
expand_dims
 - tensor에 축 단위로 차원을 추가하는 함수 
'''

import tensorflow as tf
const = tf.constant([1,2,3,4,5]) # 1차원 

print(const)
print(const.shape) # (5,)

d0 = tf.expand_dims(const, axis=0) # 행 축 2차원 
print(tf.shape(d0)) # [1 5]
print(d0) # [[1 2 3 4 5]], shape=(1, 5)
    
d1 = tf.expand_dims(const, axis=1) # 열 축 2차원 
print(tf.shape(d1)) # [5 1]
print(d1)
'''
[[1]
 [2]
 [3]
 [4]
 [5]], shape=(5, 1)
'''
   
# 행렬곱 차수 불일치 예
x_data = tf.constant([10,20])
x_data.shape#TensorShape([2])

y_data= tf.constant([[1,2,3],[3,4,5]])
y_data.shape # TensorShape([2, 3])

mat=tf.linalg.matmul(a=x_data,b=y_data)
#InvalidArgumentError: In[0] is not a matrix. Instead it has shape [2] [Op:MatMul]

#오류 해결방안: 차원 확대
x_data_ex = tf.expand_dims(input=x_data, axis=0)
x_data_ex.shape#TensorShape([1, 2])

mat=tf.linalg.matmul(a=x_data_ex,b=y_data)
print(mat)
# tf.Tensor([[ 70 100 130]], shape=(1, 3), dtype=int32)









































    




