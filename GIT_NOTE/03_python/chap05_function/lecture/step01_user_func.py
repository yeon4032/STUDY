# -*- coding: utf-8 -*-
"""
step01_user_func.py

함수(function)
-중복 코드 제거
-재사용
-특정 기능 1 개 정의
-유형:사용자정의함수, 라이브러리 함수(*.py)

사용자정의함수: 사용자가 작성한 함수

형식)
def 함수명(매개변수):
    실행문
    실행문
    [return 값]

"""

# 2차 방정식 예
def fx(x) :
    y= x**2 + 2*x + 3
    return y # 함수 반환값(y 값)

#함수 호출
fx(1) # 6
fx(2) # 11
fx(3) # 18

# 1. 인수가 없는 함수
def userFunc1():
    print('userFunc1')
    print('인수가 없는 함수')

#함수 호출
userFunc1()

#2. 인수가 있는 함수
def userFunc2(x, y):
    z=x+y
    print('z=',z)

# 함수 호출
userFunc2(10, 20) # 실인수 

# 3. return 있는 함수
def userFunc3(x, y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add, sub, mul, div # 호출한 곳 반환
    
# 함수 호출
x=int(input('x:')) # 키보드 입력
y=int(input('y:')) 

a, s, m, d = userFunc3(100,50)
print(a, s, m, d) # 150 50 5000 2.0











