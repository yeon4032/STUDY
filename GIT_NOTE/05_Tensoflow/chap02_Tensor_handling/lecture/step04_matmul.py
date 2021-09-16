
.
# -*- coding: utf-8 -*-
"""
step04_matmul.py

 - 행렬곱 전제조건
 1. 모두 행렬
 2. 수일치: A의 열수== B의 행수

"""

import tensorflow as tf

A = tf.constant([[1,2,3],[3,4,2],[3,2,5]]) # A행렬
B = tf.constant([[15,3],[3,42],[25,4]]) # B행렬

A.get_shape()#[3,3]
B.get_shape()#[3,2] 

# 행렬곱 연산
mat_mul=tf.linalg.matmul(a=A, b=B)
print(mat_mul.numpy())
'''
[[ 96  99]
 [107 185]
 [176 113]]
'''

mat_mul.get_shape() #[3, 2]












