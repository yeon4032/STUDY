# -*- coding: utf-8 -*-
"""
step05_variable _assign.py

난수 관련 함수
     tf.constant(상수)
     tf.random_normal([shape]) : 정규본포 난수
     tf.randdom_unifrom([shape]): 균등분포 난수
"""

import tensorflow.compat.v1 as tf # ver 1.x -> ver2.x 마이그래시션
tf.disable_v2_behavior() # ver 2.x 사용안함 

# 상수 정으
num = tf.constant(10.0) # scala - 0차원

# 0차원: 변수 정의
var = tf.Variable(num+20) # scala +20
print(var)  
#<tf.Variable 'Variable:0' shape=() dtype=float32_ref>

# 1차원 : 변수 정의:표준정규분포 난수
var1d = tf.Variable(tf.random_normal([3])) # [n] -> n개의 원소를 가지는 1차원 
#([n]-1차원 (n개 원소))

# 2차원 : 변수 정의:표준정규분포 난수
var2d = tf.Variable(tf.random_normal([3,2])) # [r,c] -> 3행 2열 원소를 가지는 2차원
#[r,c]-2차원(r*c개 원소)

# 2차원 : 변수 정의:균등분포:0~1
var3d = tf.Variable(tf.random_uniform([2,3,2])) # [s,r,c] 3차원(s*r*c개 원소

# 세션 객체
with tf.Session() as sess:
    # 변수 초기화: 4 개 변수
    sess.run(tf.global_variables_initializer()) # var,var1d,var2d,var3d
    
    # 0차원 변수 실행
    print('var=',sess.run(var)) # var=30.0
    
    # 1차원 변수 실행
    print('var1d=',sess.run(var1d))
    #var1d= [-0.2403285   0.20538315 -0.60621923]
    
    #2차원 변수 실행
    print('var2d=',sess.run(var2d))
    '''
    var2d= [[-0.49319375 -0.22502892]
            [ 0.42024067  0.8906636 ]
            [ 0.29803547  0.6620856 ]]
    '''
    #3차원 변수 실행
    print('var3d=',sess.run(var3d))
    '''
    var3d= [[[0.8749628  0.41850984]
             [0.8227974  0.6314148 ]
             [0.8356054  0.6247817 ]]

            [[0.20410419 0.14980686]
             [0.241395   0.920063  ]
             [0.5187665  0.8279177 ]]]
    '''
    

















