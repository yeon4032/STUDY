# -*- coding: utf-8 -*-
"""
step04_reshape.py

reshape: 모양변경
    1차원-> 2차원
    2차원-> 다른 형태의 차원
T:전치행렬
swapaxis:축 변경
transpose: 축 번호 순서로 구조 변경    
"""

import numpy as np
# 1. reshape
lst=list(range(1,13))# 1 ~ 12
lst#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#1d->2d: 원소 크기 변경 불가
arr2d=np.array(lst).reshape(3,4)
arr2d.shape #(3, 4)
'''
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
'''

#2d-> 3d
arr3d=arr2d.reshape(2,3,2) 
arr3d.size#12
arr3d.shape#(2, 3, 2)
arr3d


#2. T: 전치행렬
arr2d.T
'''
array([[ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11],
       [ 4,  8, 12]])
'''

#3. swapaxis:축 변경
arr2d.swapaxes(0,1)
'''
array([[ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11],
       [ 4,  8, 12]])
'''

#4. transpose: 축번호 순서로 구조변경
'''
1차원: 효과 없음
2차원: 전치행렬
3차원: 축 번호(0,1,2) 순서로 구조 변경
'''

arr3d=np.arange(1,25).reshape(4,2,3) # 면 4 행 2 열 3
arr3d.shape #(4, 2, 3)-> (0,1,2)
arr3d
'''
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]],

       [[13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24]]])
'''
#default:(면, 행, 열)-> (열, 행, 면)
arr2d_def=arr3d.transpose()#default (기본값)-> (2,1,0) soarr2d_def=arr3d.transpose(2,1,0) 인거임
arr2d_def.shape #(3, 2, 4)
arr2d_def

#(면, 행, 열) -> (행 면 열 )
arr2d_user=arr3d.transpose(1,0,2)
arr2d_user.shape # (2, 4, 3)
arr2d_user

#(면, 행, 열)-> (열, 면, 행)
arr2d_user2=arr3d.transpose(2,0,1)
arr2d_user2.shape # (3, 4, 2)
arr2d_user2






















