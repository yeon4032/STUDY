# -*- coding: utf-8 -*-
"""
step01_eager_execution.py

Tensorflow 2.x 특징
1. 즉시 실행(eager execution) 모드
    - seesion 사용 없이 자동으로 컴파일
    - python 처럼 즉시 실행 하는 모드 제공 (python 코드 사용 권장)
    - API(library) 정리: tf.global_variables_initializer() 삭제됨

"""
# spyder 재실행
import tensorflow as tf
print(tf.__version__) #2.3.0

# 즉시실행 모드 전환
tf.executing_eagerly() # default 활성화 (생략 가능)

# 상수 정의 + 생성
a= tf.constant(value=[[1,2], [3,4]], dtype=tf.float32)
print(a)
'''
tf.Tensor(
[[1. 2.]
 [3. 4.]], shape=(2, 2), dtype=float32)
'''

# 식 정의 + 실행
b=tf.add(x=a, y=0.5) # b= a + 0.5
print(b)
'''
tf.Tensor(
[[1.5 2.5]
 [3.5 4.5]], shape=(2, 2), dtype=float32)
'''

# 행렬곲(행렬 내적)
#python data
X=[[2.0,3.0]] # (1, 2)
a=[[1.0],[1.5]] # (2,1)

mat = tf.matmul(X, a)
print(mat)
'''
tf.Tensor([[6.5]], shape=(1, 1), dtype=float64)
'''

######################################################
#### lecture _1.x :step02_variable.py
#######################################################3
# 상수 정의: 수정 불가
x = tf.constant([1.5,2.5,3.5]) # 1차원 상수
print('x=',x)
#x= tf.Tensor([1.5 2.5 3.5], shape=(3,), dtype=float32)
print('x=',x.numpy())
#x= [1.5 2.5 3.5]


# 변수 정의: 수정 가능
y=tf.Variable([1.0,2.0,3.0]) # 1차원 변수
print('y=',y)
#y= <tf.Variable 'Variable:0' shape=(3,) dtype=float32, numpy=array([1., 2., 3.], dtype=float32)>
print('y=',y.numpy())
#y= [1. 2. 3.]


# 식 정의: 상수 or 변수 참조
mul = x * y
print('mul=',mul)
#mul= tf.Tensor([ 1.5  5.  10.5], shape=(3,), dtype=float32)
print(mul.numpy()) #[ 1.5  5.  10.5]

























