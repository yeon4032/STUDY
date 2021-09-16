# -*- coding: utf-8 -*-
"""
step02_variable.py

변수 초기화
 - 변수 정의
 - 변수 초기화
"""

# Tensorflow code
import tensorflow.compat.v1 as tf # ver1.x -> ver2.x 마이그레이션
tf. disable_v2_behavior() #ver2.x 사용 안함

''' 프로그램 정의 영역'''
# 상수 정의: 수정 불가
x = tf.constant([1.5,2.5,3.5]) # 1차원 상수

# 변수 정의: 수정 가능
y=tf.Variable([1.0,2.0,3.0]) # 1차원 변수
print('y=',y)
#y= <tf.Variable 'Variable:0' shape=(3,) dtype=float32_ref>

# 식 정의: 상수 or 변수 참조
mul = x * y
print('mul=',mul)
# mul= Tensor("mul:0", shape=(3,), dtype=float32)

'''프로그램 실행 영역'''
sess = tf.Session() # 세션 객체 생성: device 할당 역할 

with tf.Session() as sess:    # 세션 객체 생성 # sess.close() 필요 없음
    # 상수 device 할당
    print('x=',sess.run(x))#x= [1.5 2.5 3.5]
    
    #변수 device 할당: 변수 초기화 필요
    sess.run(tf.global_variables_initializer()) # 변수 초기화
    print('y=',sess.run(y)) # 초기화 전/ Error:uninitialized /  after 초기화 y= [1. 2. 3.]
    '''
    상수: 초기화 필요 없음
    변수: 초기화 필요
    '''
    # 식 device 할당: 연산
    mul_re = sess.run(mul) # 상수 * 변수
    print('mul=',mul_re)  
    # mul= [ 1.5  5.  10.5]
    type(mul_re) # numpy.ndarray
    
    mul_re.shape  # (3,)
    mul_re.mean() # 5.6666665



