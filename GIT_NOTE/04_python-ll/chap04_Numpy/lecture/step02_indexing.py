# -*- coding: utf-8 -*-
"""
step02_indexing.py

 - 1차원 indexing: list 동일
 - 2,3차원 indexing
 - boolean indexing
"""

import numpy as np

#1. 색인(indexing): 자료 참조-ppt21쪽
'''
1차원: object[index]
2차원: object[행index,열index]
        cf)DF.iloc[행index,열index]
3차원: object[면index, 행index, 열index]
'''
#1)1차원 색인
data=[0,1,2,3,4,5]

arr = np.array(data)
arr # array([0, 1, 2, 3, 4, 5])
arr[:] # 전체원소
arr[:3] # array([0, 1, 2])
arr[3:] # array([3, 4, 5])
arr[:-1]# array([0, 1, 2, 3, 4])

#2) slicing:특정 부분을 이용하여 new object 생성
arr=np.arange(10)
arr
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#주소 복사
arr_obj=arr[1:4]
arr_obj#array([1, 2, 3])<-slicing

arr_obj[:]=100 #블록 수정
arr_obj #array([100, 100, 100])

#원본수정 (slicing 한내용을 블록 수정 또는 수정하면 원본 인 객체의 정보도 수정된다.)-> 이유는 slicing은 주소 복사이기 때문이다
arr
#array([  0, 100, 100, 100,   4,   5,   6,   7,   8,   9])


#내용복사
arr_obj2=arr[1:4].copy()
arr_obj2[:]=200
arr_obj2 #array([200, 200, 200])

#원본 수정(x)
arr
# array([  0, 100, 100, 100,   4,   5,   6,   7,   8,   9])




# 2. 고차원 색인

# 1)2차원 색인 - ppt.21
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d.shape
arr2d


#행 index 기본
arr2d[0,:] #1행 전체
arr2d[0] # 1행 전체
arr2d[1:] # 2행부터 전체

arr2d[1:,1:] #2행 2열 시작해 전체

arr2d[::2]#[start,stop,step] - 홀수 행만 선택시


#비연속 행렬
arr2d[[0,2],:] # 1,3행 
arr2d[:,[0,2]] # 1,3열 




# 2) 3차원 색인
arr3d= np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ])
arr3d
'''
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
'''

#면 index기본
arr3d[0] # 1면
'''
array([[1, 2, 3],
       [4, 5, 6]])
'''

arr3d[0,1] # 면,행
#array([4, 5, 6])

arr3d[0,1,1:] #[면,행,열]
#array([5, 6])


#4차원 : images = [size,h,w,c]
#image # size 기본 색인

#3.조건식 색인(boolean index)
dataset = np.random.randn(3,4) #(shape)
dataset


# 0.7이상 
dataset[dataset>=0.7]
'''
array([0.96484171, 1.38506057, 0.85018041, 0.8155078 ])
'''

#0.1~0.7 -> 논리식 사용 불가
dataset[dataset>=0.1 and dataset<=0.7] #error

'''
numpy 에서 제공하는 논리식 함수
'''

np.logical_and()#논리곱
np.logical_or()#논리합
np.logical_not()# 부정
np.logical_xor()#배타적 논리합

dataset[np.logical_and(dataset>=0.1, dataset<=0.7)]
'''
array([0.24331297])
'''

dataset[np.logical_or(dataset>=0.1, dataset<=0.7)]
'''
array([-0.02172319, -0.60713544,  0.96484171,  1.38506057, -0.43952868,
       -0.91037619,  0.85018041,  0.8155078 , -1.34929391, -0.21580704,
        0.24331297, -0.67939152])
'''

dataset[np.logical_not(dataset<=0.7)] # not 조건
#array([0.96484171, 1.38506057, 0.85018041, 0.8155078 ])


# pandas 객체 적용
import pandas as pd
ser=pd.Series([2,1,3,4,5])

ser[ser>=3]
#2~4
#ser[ser>=2 and ser<=4]
ser[np.logical_and(ser>=2,ser<=4)]






























