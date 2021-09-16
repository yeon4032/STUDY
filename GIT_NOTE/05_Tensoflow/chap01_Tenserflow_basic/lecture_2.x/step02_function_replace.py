# -*- coding: utf-8 -*-
"""
step02_function_replace.py

2. 함수 (function)사용 권장
    - 공급형 변수 -> 함수 인수 대체 
    - API  정리: tf.placeholder() 사용 안함
"""

import tensorflow as tf # ver2.3
'''
# 변수 정의: 공급형 변수
a = tf.placeholder(dtype=tf.float32) # shape 생략: 가변형, 실수형
b = tf.placeholder(dtype=tf.float32) # shape 생략: 가변형, 실수형

c = tf.placeholder(dtype=tf.float32,shape=[5]) # 고정형, 실수형
d = tf.placeholder(dtype=tf.float32,shape=[None, 3]) # [가변형,고정형]

# 식 정의: 변수 참조
mul = tf.multiply(a,b) # mul = a * b
add = tf.add(mul, 10) # add = mul + 10
'''

# tf.placeholder-> function 대체
def mul_fn(a, b): 
    return tf.multiply(a, b)

def add_fn(mul):
    return tf.add(mul,10)

# a,b 자료 생성
a_data = [1.0,2.0,3.0]
b_data = [2.0,3.0,4.0]

mul_re = mul_fn(a_data, b_data)
print('mul=',mul_re.numpy()) # mul= [ 2.  6. 12.]


add_re = add_fn(mul_re)
print('add=',add_re.numpy()) # add= [12. 16. 22.]






































