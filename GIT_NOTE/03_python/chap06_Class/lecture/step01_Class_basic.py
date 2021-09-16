# -*- coding: utf-8 -*-
"""
step01_Class_basic.py

클래스(class)
 - 여러 개의 함수와 자료를 묶어서 객체 생성 역할 
 - 구성 : 메서드(함수) + 변수(자료) + 생성자(객체 생성)
 - 멤버 : 멤버메서드, 멤버변수 
 - 유형 : 사용자정의클래스, 모듈 클래스(python 제공)
 
 형식)
 class 클래스명 :
     멤버변수 = 자료 
     def 멤버메서드() :
         명령문
     생성자 : 객체 생성 
"""

# 1. 중첩함수 
def calc_fn(a, b) : # outer : data 생성 
    # data 생성 
    x = a # x=10
    y = b # y=20
    
    # inner : data 처리 
    def plus() :
        p = x + y
        return p
    
    def minus() :
        m = x - y
        return m
    
    return plus, minus

p, m = calc_fn(10, 20)

print('plus =', p()) # plus = 30
print('minus =', m()) # minus = -10


# 2. 클래스 : 중첩함수 -> 클래스 변경 
class calc_class :
    #멤버 변수(전역변수) : data 생성
    x = 0 # 10
    y = 0 # 20
    
    # 생성자 : 객체 생성 + 멤버변수 초기화 역할 
    def __init__(self, a, b) :
        self.x = a
        self.y = b
    
    # 멤버메서드 : inner(data 처리)
    def plus(self) :
        p = self.x + self.y
        return p
    
    def minus(self) :
        m = self.x - self.y
        return m
    
# 1) 객체 생성 : 생성자 이용    
obj1 = calc_class(10, 20) # 생성자  -> 객체 생성    

# 2) object.member(멤버변수 + 멤버메서드)
print('x=', obj1.x)
print('y=', obj1.y)
print('plus =', obj1.plus()) # plus = 30
print('minus =', obj1.minus()) # minus = -10


# 두번째 객체 생성 
obj2 = calc_class(100, 200)
print('plus =', obj2.plus()) # plus = 300
print('minus =', obj2.minus()) # minus = -100

# 객체 주소 확인 
print(id(obj1), id(obj2))
# 1775547108512 1775551190640


# 3. 모듈 클래스(python 제공)
from datetime import date # from 모듈 import 클래스  
'''
모듈(함수+클래스)
'''

# 생성자 -> object 생성 
today = date(2021, 6, 2) # 클래스() -> 생성자 

# object.member(변수, 메서드)
today.year # 2021
today.month # 6
today.day # 2

# object.method()
print('요일 :', today.weekday()) # 요일 숫자 반환 
# 요일 : 2 -> 0(월) ~ 6(일)



















