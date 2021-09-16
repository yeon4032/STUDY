# -*- coding: utf-8 -*-
"""
step04_func_args.py

함수의 가벼인수
 - 한 개 가인수로 여러 개의 실인수를 받는 인수
 형식) def 함수명(인수1, *인수2)
"""

# 1. 가변인수 예 : tuple
def Func1(name, *names):
    print(name) # 인수:홍길동
    print(names) #가변인수: ('이순신', '유관순')

Func1("홍길동", "이순신","유관순") 
#       name     names    names
#결과
#홍길동
#('이순신', '유관순')

#2. 가변인수 예: dict
def person(w,h,**other):
    print('몸무게:', w)
    print('키:', h)
    print('키타:', other) #키타: {'name': '홍길동', 'addr': '서울시'} 
person(65, 175, name='홍길동', addr='서울시')
#결과
#몸무게: 65
#키: 175
#키타: {'name': '홍길동', 'addr': '서울시'} 

'''
df_con={'user': 'scott',
        'pass': 'tiger'}
'''


# 3. 함수를 인수로 넘기
def square(x):
    return x**2

def my_func(func,datas): #(함수, 데이터셋)
    re=[]
    for x in datas:
        re.append(func(x))
    return re

datas=[2,4,6]

result=my_func(square,datas)
print(result)
































































































