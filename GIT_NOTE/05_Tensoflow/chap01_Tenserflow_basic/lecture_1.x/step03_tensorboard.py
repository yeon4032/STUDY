# -*- coding: utf-8 -*-
"""
step03_tensorboard.py

Tensorboard
    - 그래프 시가화 도구
    - 데이터의 흐름 시각화 기능
"""
import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함 

#tensorboard 초기화
tf.reset_default_graph()

# 상수 정의
x= tf.constant(1)
y= tf.constant(2)

# 산술연산식 정의
a = tf.add(x,y, name='a') # 탄소보드 식 이름 정하기 name=''
b = tf.multiply(a,6, name='b') # b = a*6
c = tf.subtract(20, 10, name='c') # c=20 - 10
d = tf.div(c,2,name='d') # d = c/2

g=tf.add(b,d, name='g') # g = b + d
h=tf.multiply(g,d,name='h') # h = g * d

#session 객체 생성
with tf.Session() as  sess:
    h_clac = sess.run(h) # 식 device 할당 :연산
    print('h=',h_clac) # h=115
    
    # tensorboard graph 생성 과정
    tf.summary.merge_all() # 상수,식 모으는 역할 
    writer = tf.summary.FileWriter("C:/ITWILL/5_Tensoflow/graph",sess.graph)
    writer.close()



























