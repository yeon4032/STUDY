'''
문) 다음과 같이 Convolution layer와 Max Pooling layer를 정의하고, 실행하시오.
  <조건1> input image : volcano.jpg 파일 대상    
  <조건2> Convolution layer 정의 
    -> Filter : 6x6
    -> featuremap : 16개
    -> strides= 1x1, padding='SAME'  
  <조건3> Max Pooling layer 정의 
    -> ksize= 3x3, strides= 2x2, padding='SAME' 
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# <조건1> input image : volcano.jpg 파일 대상 
img = imread('C:\\ITWILL\\5_Tensoflow\\data/images/volcano.jpg') # 이미지 읽어오기
plt.imshow(img)
plt.show()
print(img.shape)(405, 720, 3)
Img = img.reshape(1, 405, 720, 3) # (size, h, w, c)

#  <조건2> Convolution layer 정의 

# Filter 
Filter = tf.Variable(tf.random.normal([6,6,3,16])) #[h, w, c, fmap]

# 1. Convolution layer 
conv2d = tf.nn.conv2d(Img, Filter, strides=[1,1,1,1], padding='SAME')


#  <조건3> Max Pooling layer 정의 

# 2. Pool layer 
pool = tf.nn.max_pool(conv2d, ksize=[1,3,3,1], strides=[1,2,2,1],
                      padding='SAME')

# 합성곱 연산 
conv2d_img = np.swapaxes(conv2d, 0, 3)
    
fig = plt.figure(figsize = (20, 6))  
for i, img in enumerate(conv2d_img) :
    fig.add_subplot(1, 5, i+1) 
    plt.imshow(img.reshape(256, 384)) # 2d
plt.show()

# 폴링 연산 
pool_img = np.swapaxes(pool, 0, 3)

fig = plt.figure(figsize = (20, 6))    
for i, img in enumerate(pool_img) :
    fig.add_subplot(1,5, i+1)
    plt.imshow(img.reshape(64, 96)) # 2d
plt.show()







