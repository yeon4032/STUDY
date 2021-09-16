# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징
 - pandas 1차원 자료구조
 - DataFrame의 칼럼 구성요소
 - 수학/통계 관련 함수 제공
 - 범위 수정,  broadcast 연산
 - indexing/slicing 기능 : list 유사함 
 - 시계열 데이터 생성/처리 
"""

import pandas as pd # 별치 -> pd.Series()
from pandas import Series #class Seriec()

#1. Series 객체 생성

#1) list 이용
price = pd.Series([3000,2000,1000,5200]) #생성자
print(price)
'''
index  value
0      3000
1      2000
2      1000
3      5200
dtype: int64
'''
#price 의 index정보 추출
print(price.index) #RangeIndex(start=0, stop=4, step=1)

#price 의 값들을 추출
print(price.values) #[3000 2000 1000 5200]

#색인 사용
price[1] #2000

#index 적용
price2=Series([2000,3000,4500,3500], 
              index=['a','b','c','d'])
print(price2)
'''
a    2000
b    3000
c    4500
d    3500
dtype: int64
'''

price2['b'] #3000

#boolean 조건식 
price2[price2 >= 3500]
'''
c    4500
d    3500
dtype: int64
'''

# 2)dict 이용 : (key : value) -> (index : values)
person = pd.Series({'name':'홍길동', 'age':35,'addr':'서울시'}) # 생성자
print(person)
'''
name    홍길동
age      35
addr    서울시
dtype: object -> 자료형 통일(숫자와 문자 가 있으나 문자가 우선)
'''

person['age'] #35

#2. indexing/slicing: list 동일
ser= pd.Series([4,4.5,6,8,10.5]) #[정수,실수]
print(ser)
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
dtype: float64 -> 자료형 통일 (정수 실수 썩이면 실수 우선)
'''

ser[:] # 전체원소 
ser[0] # 1번 원소
ser[:3]# 0~2 까지 원소
ser[3:]# 3~end 까지 원소
# ser[-1] # key error (사용 불가)


#3. Series 결합 NA 처리
s1 =pd.Series([3000,None,2500,2000],
              index = ['a','b','c','d'])

s2 =pd.Series([4000,2000,3000,1500],
              index = ['a','c','b','d'])

#Series 결합(사측연산)
s3=s1 + s2
print(s3)
'''
a    7000.0
b       NaN <- 결측치
c    4500.0
d    3500.0
dtype: float64
'''

#결측치 처리(통계(평균,중위수), 특정 상수)
result=s3.fillna(s3.mean())
print(result)
'''
a    7000.0
b    5000.0
c    4500.0
d    3500.0
dtype: float64
'''

result2=s3.fillna(0)
print(result2)
'''
a    7000.0
b       0.0
c    4500.0
d    3500.0
dtype: float64
'''

# 결측치 제거
result3=s3[pd.notnull(s3)]
print(result3)
'''
a    7000.0
c    4500.0
d    3500.0
dtype: float64
'''

# 4. Series 연산

#1) 블럭 수정
print(ser)
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
dtype: float64
'''
ser[1:4]=5.0
print(ser)
'''
print(ser)
0     4.0
1     5.0
2     5.0
3     5.0
4    10.5
dtype: float64
'''

# 2) broadcast 연산
# 차원이 큰쪽으로 늘어난 후 연산
ser.shape # (5,) -> 1차원  
print(ser*0.5) #1차원(vextor) * 0차원(scala)
'''
0    2.00
1    2.50
2    2.50
3    2.50
4    5.25
dtype: float64
'''
'''
lst =[1,2,3,4]
lst *0.5 #error 임 즉 리스트에서는 broadcast 연산이 안됨
'''

# 3) 수학/통계 함수
ser.mean() # 5.9
ser.sum()  # 29.5
ser.var()  # 6.8
ser.std()  # 2.6076809620810595
ser.max()  # 10.5
ser.min()  # 4.0

#object.method()
dir(ser) #해당 object의 멤버 확인 (어떠한 함수나 기능을 ser에 사용 가능한지 확인)

# 값의 출현 빈도수
ser.value_counts()
'''
5.0     3
10.5    1
4.0     1
dtype: int64
'''

#중복되지 않은 값
ser.unique() #array([ 4. ,  5. , 10.5]) 

#최빈수
ser.mode() 
#0    5.0




