# -*- coding: utf-8 -*-
"""
step03_universal.py
-범용함수(universal functino)-ppt.28
    -다차원 배열 대상 수학/통계 등의 함수

"""

import numpy as np


#1. numpy 제공 함수: np.함수 (object)
data = np.random.randn(5) #1차원 난수 배열
data
# array([ 0.72897503, -0.02176288,  0.04540745,  1.38931228,  1.338835  ])
type(data) #numpy.ndarray


#수학/통계 함수
np.abs(data) #절대값 
np.sqrt(data)#제곱근
np.squrare(data)#제곱
np.sign(data) # 부호 array([ 1., -1.,  1.,  1.,  1.]) 양수=1 음수=-1
np.var(data) # 모집단 분산
np.std(data) # 모집단 표준편차
np.sqrt(np.var(data)) #모집단 표준편차

# 로그: data 정규화
data2=np.array([1,2.5,3.36,4.6])
type(data2)#numpy.ndarray

np.log(data2)# 밑수e -자연로그
#array([0.        , 0.91629073, 1.21194097, 1.5260563 ])

#지수: signoid 함수 이용
e=np.exp(1)
e#2.718281828459045


#반올림 함수
np.ceil(data2)# 큰 정수 올림
#array([1., 3., 4., 5.])
np.rint(data2) # 가장 가까운 정수 올림
#array([1., 2., 3., 5.])
np.round(data2,1)#자리수 지정
#array([1. , 2.5, 3.4, 4.6])

np.exp(data2)
# array([ 2.71828183, 12.18249396, 28.78919088, 99.48431564])

#결측 처리
data2=np.array([1,2.5,3.36,4.6,np.nan]) #NA
data2#array([1.  , 2.5 , 3.36, 4.6 ,  nan])

np.isnan(data2) #is.na(data)
#array([False, False, False, False,  True]) False-> 격측치 없다. ,True-> 결측치 있다.

#결측치 제거: 조건식 색인 
data2[np.isnan(data2)] # array([nan]) 결측치만 반환
new_data = data2[np.logical_not(np.isnan(data2))] # not 조건식 사용.
new_data # array([1.  , 2.5 , 3.36, 4.6 ])

new_data = data2[~np.isnan(data2)] #~ 은 not 조건식 과 같은 의미
#array([1.  , 2.5 , 3.36, 4.6 ])

#2. 객체 메서드 이용: object.함수()
data2=np.random.randn(3,4) #2 차원 난수 배열
data2
data2.shape #(3, 4)

#전체 원소 대상
data2.sum() #-1.3588151135315543
data2.mean()#-0.1132345927942962

data2.var()
data2.std()

# axis 속성
data2.sum(axis=0) # 행축: 같은 열들의 모음 (열 단위 합계)
data2.sum(axis=1) # 열축: 같은 행들의 모음 (행 단위 합계)
data2.sum()#전체 합계

