﻿'''
문) 정규분포를 따르는 난수 1,000개를 x변수에 저장하고, 
     y변수는 x변수의 코사인 값을 저장하여 산점도 차트를 출력하시오.     
    <조건1> x, y 변수 : placeholder()함수 이용 
    <조건2> x변수 : x_data 공급
    <조건3> y변수 : y_data 공급 
    <조건4> 산점도 차트 : matplotlib.pyplot 함수 이용   
tensorflow 가상환경에서 matplotlib 설치
(base) > conda activate tensorflow
(tensorflow) > conda install -c conda-forge matplotlib
'''

import numpy as np # 공급 data 생성 
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

# 공급 data 생성 : numpy data
x_data = np.random.randn(1000) # numpy : 정규분포를 따르는 난수 1,000개 
y_data = np.cos(x_data) #  numpy : x변수의 코사인 값
print(x_data)
print(y_data)

# <조건1> : 1차원 배열 공급형 변수 정의  
x = tf.placeholder(dtype=tf.float32, shape=[1000]) # x_data 공급
y = tf.placeholder(dtype=tf.float32, shape=[1000]) # y_data 공급 

# 세션 생성 : <조건2> ~ <조건4>
with tf.Session() as sess :
    # <조건2> : x변수 실행 
    x_re=sess.run(x, feed_dict={x:x_data})
    
    # <조건3> : y변수 실행 
    y_re=sess.run(y, feed_dict={y:y_data})
    
    #<조건4> 산점도 차트 : matplotlib.pyplot 함수 이용
    plt.scatter(x=x_re,y=y_re, c='red')
    plt.show

    
    
    
    