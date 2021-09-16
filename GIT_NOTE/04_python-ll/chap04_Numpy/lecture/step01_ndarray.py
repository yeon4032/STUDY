# -*- coding: utf-8 -*-
"""
step01_ndarray.py

Numpy 패키지
 - 수치과학용 데이터 처리 목적으로 제공되는 패키지이다.
 - 선형대수(백터,행렬 연산) 관련 함수 제공
 - list 보다 이점 
     -> N 차원 배열, broadcast 연산 가능,고속 연산 가능
     -> 수학/통계 함수 제공
     공통점
     -> indexing/slicing
"""
import numpy as np #별칭

#1. list 배열 vs 다차원 배열

#1)list 배열
lst=[1,2,3,4.5,5] # 정수,실수 자료형
print(lst)

#list 는 broadcast 연산 지원 안된다. 
lst*3
#[1, 2, 3, 4.5, 5, 1, 2, 3, 4.5, 5, 1, 2, 3, 4.5, 5]
sum(lst) # 외부함수 이용
#15.5

#2) 다차원 배열
arr = np.array(lst)
type(arr) #numpy.ndarray
print(arr) #[1.  2.  3.  4.5 5. ] 동일한 자료형을 가진다

arr*0.5 #broadcast 연산
# array([0.5 , 1.  , 1.5 , 2.25, 2.5 ])

arr.sum() # object.method()


#2. array(): 다차원 배열 생성

#1) 단일 list -> 일차원 배열
lst1=[3,5.2,4,7]
print(lst1)

#list-> array
arr1d=np.array(lst1)
arr1d.shape#(4,) # 자료모양 확인

print('평균=',arr1d.mean())
print('분산=',arr1d.var())
print('표준편차=',arr1d.std())
#호출가능한 member(속성,메서드) 확인
dir(arr1d)
arr1d.size#4


#2)중첩list-> 2차원 배열
lst2=[[1,2,3,4],[5,6,7,8]]
print(lst2) #[[1, 2, 3, 4], [5, 6, 7, 8]]

arr2d=np.array(lst2)
arr2d.shape#(2, 4)
print((arr2d))
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
n
#3. broadcast 연산
#-작은 차원이 큰 차원으로 늘어난 후 연산

#1) scala(0) vs vector(1d)
print(0.5*arr1d) #[1.5 2.6 2.  3.5]

#1) scala(0) vs matrix(2d)
print(0.5*arr2d)
'''
[[0.5 1.  1.5 2. ]
 [2.5 3.  3.5 4. ]]'''

#3) vector(1d) vs matrix(2d)
print(arr1d*arr2d)
'''
[[ 3.  10.4 12.  28. ]
 [15.  31.2 28.  56. ]]
'''

'''
표본 분산=(sum(x-mu)**2)/n-1
'''
print('분산=',arr1d.var())
#분산= 2.2199999999999998

mu = arr1d.mean()

diff=(arr1d-mu)**2
var = sum(diff)/arr1d.size
print(var)#2.2199999999999998


#4. zeros or ones
zarr = np.zeros((3,10)) # shape=()
print(zarr)#영행렬 -> DTM(문서:3개 단어:10)
'''
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''

oarr=np.ones((3,5))
print(oarr)
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''

#5. arange
'''
range vs arange
range(start,stop,step): 일렬의 정수 생성
arrange(start,stop,step): 일렬의 정수 or  실수
'''

#1) range vs arange
print(list(range(1,11))) #range(1, 11)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range(-1.0,10.5)#TypeError:

#실수형 밷터 생성
arr = np.arange(-1.2,5.5)
print(arr)
#[-1.2 -0.2  0.8  1.8  2.8  3.8  4.8]

arr=np.arange(1,11)
print(arr)#[ 1  2  3  4  5  6  7  8  9 10]

#ex)x의 수열에 대한 2차 방정식
x =np.arange(-1.0,2,0.1)
x.size #30

#f(x)->y
def f(x):
    y=x**2+2*x+3 #broadcast 연산
    return y

print(f(x))
'''
[ 2.    2.01  2.04  2.09  2.16  2.25  2.36  2.49  2.64  2.81  3.    3.21
  3.44  3.69  3.96  4.25  4.56  4.89  5.24  5.61  6.    6.41  6.84  7.29
  7.76  8.25  8.76  9.29  9.84 10.41]
'''

#2차 방정식 그래프
import matplotlib.pyplot as plt
plt.plot(x,f(x))
plt.show()

#2) 색인 반환
zarr=np.zeros((3,5))
zarr
'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
'''
cnt=0
for i in np.arange(3): #0~2
    for j in np.arange(5): #0~4
        cnt+=1
        zarr[i,j]=cnt
    
zarr
'''
 array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
'''

