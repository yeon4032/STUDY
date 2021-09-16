# -*- coding: utf-8 -*-
"""
step06_inner_func.py

중첩함수(inner function)

형식)
def outer(인수):
    명령문
    def inner(인수):
        명령문
    return inner
"""

#1. 중첩함수 예 
def a(): #outer                # 데이터 생성
    print('a 함수')    
    
    def b(): #inner            # 자료처리
        print('b 함수')
        
    return b # inner 함수 반환

# outer 호출
b = a() #a 함수 = b: 일급함수

# inner호출
b() # b함수

#2. 중첩함수 응용
'''
-outer 함수 역할:dataset 생성, inner 함수 포함
-inner 함수 역할:dataset 조작
'''

def outer_func(data): #outer
    dataset=data # dataset 생성
    
    # 합계 : inner
    def tot():
        tot_val=sum(dataset)
        return tot_val
    
    #평균:inner
    def avg(tot_val):
        avg_val=tot_val/len(dataset)
        return avg_val
    
    return tot, avg

data=list(range(1,1001))
data

#outer 호출
tot, avg = outer_func(data)

#inner 호출
tot_val=tot()
avg_val=avg(tot_val)
print('tot=%d,avg=%.5f'%(tot_val,avg_val))
