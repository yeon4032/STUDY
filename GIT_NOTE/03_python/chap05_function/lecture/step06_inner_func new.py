# -*- coding: utf-8 -*-
"""
step06_inner_func.py

중첩함수(inner function)

형식)
def outer(인수) :
    명령문
    def inner(인수) :
        명령문
    return inner
"""

# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    
    def b() : # inner 
        print('b 함수')
        
    return b # inner 함수 반환 

# outer 호출 
b = a() # a 함수 = b : 일급함수 
# inner 호출 
b() # b 함수


# 2. 중첩함수 응용 
'''
 - outer 함수 역할 : dataset 생성, inner 함수 포함 
 - inner 함수 역할 : dataset 조작 
'''

def outer_func(data) : # outer 
    dataset = data # dataset 생성
    
    # 합계 : inner
    def tot() :
        tot_val = sum(dataset)
        return tot_val
    
    # 평균 : inner
    def avg(tot_val) :
        avg_val = tot_val / len(dataset)
        return avg_val        
    
    return tot, avg


data = list(range(1, 1001))
data

# outer 호출 
tot, avg = outer_func(data)
# 함수 클로저 : 함수를 객체로 저장하는 것, 함수 호출 기능 

tot_val = tot()
avg_val = avg(tot_val)
print('tot = %d, avg = %.5f'%(tot_val, avg_val))
# tot = 500500, avg = 500.50000


# 3. nonlocal : inner -> outer 값 접근 
'''
getter() 함수 : 함수 내 값을 획득하는 함수(획득자) 
setter() 함수 : 함수 내 값을 수정하는 함수(지정자)    
'''

def main_func(num) : # outer
    num_val = num # data 생성 
    
    # inner 
    def get_func() : # 획득자 
        return num_val # 외부 넘김 
    
    def set_func(value) : # 지정자 
        nonlocal num_val
        num_val = value # 값 수정 
        
    return get_func, set_func

# outer 호출 
g, s = main_func(100)

num = g() # 값 획득 
print('num_val =', num) # num_val = 100

s(200) # 값 수정 

num = g() # 값 획득 
print('num_val =', num) # num_val = 200


# 4. 함수 장식자 : Tensorflow2.0 적용 
# - 기존 함수의 시작부분과 종료부분에 장식을 추가 역할 
'''
@함수장식자
def 함수명() :
    실행문
'''

# 함수 장식자 : 1차 
def hello_deco(func) : # outer
    def inner() : # inner
        print('*'*20)
        func() # 함수 본체 
        print('*'*20)
    return inner
    

# 대상 함수 
@hello_deco
def hello() :
    print('my name is 홍길동')


# 함수 호출 
hello()



# 함수 장식자 : 2차 
def hello_deco2(func) : # outer
    def inner(name) : # inner
        print('*'*20)
        func(name) # 함수 본체 
        print('*'*20)
    return inner
    

# 대상 함수 
@hello_deco2
def hello2(name) :
    print('my name is ' + name)


# 함수 호출 
hello2('이순신')



























