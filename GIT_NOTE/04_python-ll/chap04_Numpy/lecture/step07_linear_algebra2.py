# -*- coding: utf-8 -*-
"""
step07_linear_algebra2.py

-행렬곱과 연립방정식의 해
"""

import numpy as np


# 1. 행렬곱: 행렬 vs 행렬 곱셈 연산 
'''
u,v행렬
행렬내적 : u.T @ v
행렬 외적: u @ v.T
'''

#행렬내적 : u.T @ v
u=np.array([[1,2]])
v=np.array([[2,3]])
u #array([[1, 2]])
u.shape #(1, 2)

v # array([[2, 3]])
v.shape #(1, 2)

re=u.T.dot(v) #행렬곱
print(re)
'''
array([[2, 3],
       [4, 6]])
'''

'''
1.행렬
2.수 일치: 앞행렬(열수)=뒤행렬(행수)
'''

#기호 표현
u.T #(2,1)
'''
array([[1],
       [2]])
'''
v #(1,2)
'''
 array([[2, 3]])
'''
u.T @ v #(2,2) 행열 내적 기호 표현
'''
array([[2, 3],
       [4, 6]])
'''

#2) 행렬 외적
u
#array([[1, 2]])
v.T
'''
array([[2],
       [3]])
'''
re=u @ v.T
re#array([[8]])
re.shape#(1, 1)

#2.연립방식의 해
'''
연립방식: 2개 이상의 방정식을 묶어놓은 것
3*x+2*y=53
-4*x+3*y=-35
'''
a=np.array([[3,2],[-4,3]]) #2차원
b=np.array([53,-35])  #1차원

x,y=  np.linalg.solve(a,b)
print(x,y)

#test
3*x+2*y  #53.0
-4*x+3*y #-35


