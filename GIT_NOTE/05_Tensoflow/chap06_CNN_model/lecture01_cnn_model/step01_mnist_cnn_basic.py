# -*- coding: utf-8 -*-
"""
MNIST + CNN basic
 Convolution layer : 특징맵(feature mat)
 Pooling layer : 픽셀 축소(다운샘플링), 특징 강조  
"""
import tensorflow as tf # ver2.x
from tensorflow.keras.datasets.mnist import load_data # ver2.0 dataset
import numpy as np
import matplotlib.pyplot as plt

# 1. image read  
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)
print(y_train.shape) # (60000,) : 10진수 
print(x_test.shape) # (10000, 28, 28)
print(y_test.shape) # (10000,) : 10진수 
print(x_train[0]) # 0 ~ 255

# 2. 실수형 변환 : int -> float
x_train = x_train.astype('float32') # type 일치 
x_test = x_test.astype('float32')

# 3. 정규화 
x_train /= 255 # x_train = x_train / 255
x_test /= 255
print(x_train[0])

# first image 
img = x_train[0]
plt.imshow(img, cmap='gray') # 숫자 5  
plt.show() 
img.shape # (28, 28)

# input image reshape 
firstImg = img.reshape(1,28,28,1) # [size, h, w, color]
print(firstImg) 

# Filter(W) 변수 정의 : [h, w, color, map_size]
Filter = tf.Variable(tf.random.normal([3,3,1,5])) # 난수 
 
# 1. Convolution layer : strides = [2x2], padding = 'SAME'
conv2d = tf.nn.conv2d(firstImg, Filter, strides=[1,1,1,1], padding='SAME')


# 2. Pool layer : ksize=[2x2], strides = [2x2], padding = 'SAME'
pool = tf.nn.max_pool(conv2d, ksize=[1,2,2,1], strides=[1,2,2,1],
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

    











