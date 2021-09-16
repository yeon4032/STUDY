'''
문) 다음과 같이 합성곱층과 폴링층을 작성하고 결과를 확인하시오.
  <조건1> input image : mnist.train의 7번째 image     
  <조건2> input image shape : [-1, 28,28,1] 
  <조건3> 합성곱 
         - strides= 2x2, padding='SAME'
         - Filter : 3x3, 특징맵 = 10
  <조건4> Max Pooling 
    -> ksize= 3x3, strides= 2x2, padding='SAME' 
'''

import tensorflow as tf # ver1.x

from tensorflow.keras.datasets.mnist import load_data # ver2.0 dataset
import numpy as np
import matplotlib.pyplot as plt

# 1. image read  
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)

# 2. 실수형 변환 : int -> float
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32')

# 3. 정규화 
x_train = x_train / 255 # x_train = x_train / 255
x_test = x_test / 255

# 7번째 image 
img = x_train[6]
plt.imshow(img, cmap='gray') # 숫자 5 -> x-ray 방식 
plt.show()


# <조건2> input image shape : [-1, 28,28,1] 
firstImg = img.reshape(-1,28,28,1) # [size, h, w, color]
print(firstImg) 


# <조건3> 합성곱 
#         - strides= 2x2, padding='SAME'
#         - Filter : 3x3, 특징맵 = 10

# Filter(W) 변수 정의 : [h, w, color, map_size]
Filter = tf.Variable(tf.random.normal([3,3,1,10])) # 난수 
 
# Convolution layer 
conv2d = tf.nn.conv2d(firstImg, Filter, strides=[1,2,2,1], padding='SAME')



# <조건4> Max Pooling 
#    -> ksize= 3x3, strides= 2x2, padding='SAME'

# Pool layer : 
pool = tf.nn.max_pool(conv2d, ksize=[1,3,3,1], strides=[1,2,2,1],
                      padding = 'SAME')

  
# 합성곱 연산 
print(conv2d.shape) # (1, 28, 28, 5)
conv2d_img = np.swapaxes(conv2d, 0, 3) # 축 교환 

for i, img in enumerate(conv2d_img) :
    plt.subplot(1, 5, i+1) # 1행5열,1~5 
    plt.imshow(img.reshape(28, 28), cmap='gray')  
plt.show()

# 폴링 연산 
print(pool.shape) # (1, 14, 14, 5)
pool_img = np.swapaxes(pool, 0, 3)

for i, img in enumerate(pool_img) :
    plt.subplot(1,5, i+1)
    plt.imshow(img.reshape(14, 14), cmap='gray') 
plt.show()


