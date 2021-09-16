# -*- coding: utf-8 -*-
"""
step06_variable_feed.py

Tensorflow 변수유형
1. 초기값을 갖는 변수
    -형식) tf.Variable(초기값)
2. 초기값이 없느 변수
    -형식) tf.placeholder(dtype,shape)
    dtype: 자료형(tf.int32,tf.float32,tf.string)
    shape: 자료모양(1차원:[n], 2차원:[[m,n]], 생략: 공급data 결정)
"""
import tensorflow.compat.v1 as tf # ver 1.x -> ver2.x 마이그래시션
tf.disable_v2_behavior() # ver 2.x 사용안함 

# 변수 정의: 공급형 변수
a = tf.placeholder(dtype=tf.float32) # shape 생략: 가변형, 실수형
b = tf.placeholder(dtype=tf.float32) # shape 생략: 가변형, 실수형

c = tf.placeholder(dtype=tf.float32,shape=[5]) # 고정형, 실수형
d = tf.placeholder(dtype=tf.float32,shape=[None, 3]) # [가변형,고정형]

# 식 정의: 변수 참조
mul = tf.multiply(a,b) # mul = a * b
add = tf.add(mul, 10) # add = mul + 10

with tf.Session() as sess:
    #식 실행:a,b 자료 공급
    feed_data ={a : [2.5,3.5], b :3.5}
    mul_re = sess.run(mul,feed_dict = feed_data) #공급형 변수 에 값 넣기 실행후 넣은 값은 사라진다.
    print('mul=',mul_re) # mul= 8.75 when a =2.5 / mul= [ 8.75 12.25], when a = [2.5,3.5]
    
    add_re = sess.run(add, feed_dict = feed_data)
    print('add=',add_re) # add= 18.75 when a =2.5 / add= [18.75 22.25], when a = [2.5,3.5]
    
    # c 변수:공급 data 생성
    c_data = sess.run(tf.random_normal([5]))# 난수 1차원 5개
    c_re = sess.run(c, feed_dict={c : c_data})
    print('c=',c_re) #c= [-1.1083605  1.2209637  1.5889338 -2.1617515  2.1283562]
    
    #d변수 : 공급 data 
    d_data = sess.run(tf.random_normal([7, 3])) # 70%
    d_data2= sess.run(tf.random_normal([3,3]))  # 30%

    d_re = sess.run(d,feed_dict={d: d_data2})
    print(d_re)
    print(d_re.shape) # (10,3) -> (3,3)













