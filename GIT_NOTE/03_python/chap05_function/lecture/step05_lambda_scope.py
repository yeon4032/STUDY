# -*- coding: utf-8 -*-
"""
step05_lambda_scope.py

1. 축약함수(lambda)
- 한 줄 함수
형식) 변수= lambda 인수: 명령문 or 리턴값
ex) lambda x,y: x+y

2. scope: 변수의 사용범위
-전역변수 : 함수 내부 외부 사용 가능한 변수
-지역변수: 함수에서 정의된 변수(매개변수)
    ->, 함수가 종료되면 자동 소멸된다.
"""

#1. 축약함수(lambda)
def Adder(x,y):
    add = x + y
    return add

Adder(10, 30) #40


#형식) 변수= lambda 인수: 명령문 or 리턴값
Adder2 = lambda x, y : x + y 

print('add=',Adder2(10,20)) # add= 30

#x 변량에 제곱
dataset=[2,4,5,6,8,3]
len(dataset)

square = lambda datas : [x**2 for x in datas]
print('square=', square(dataset))
# square= [4, 16, 25, 36, 64, 9]

#혈액형 dummy 변수 : AB(1), A,B,O(0)
datas={'A':0,'B':0,'O':0,'AB':1} # table

dummy= lambda x:[datas[i] for i in x]
x=['O','B','A','O','AB']

print('dummy=',dummy(x))



# 2. scope: 변수의 사용범위
#-전역변수 : 함수 내부 외부 사용 가능한 변수
#-지역변수: 함수에서 정의된 변수(매개변수)

x= 50 # 전역변수

#지역변수 :x
def local_func(x):
    x+=50 #지역변수
    print('local func(x)=',x)#local func(x)= 100

local_func(x) #전역변수 

print('x=',x)#x= 50


#전역변수 :x

def global_func(x):
    global x # 전역변수 x
    x+=50
    print('global_func(x)=', x) #global_func(x)=100

global_func()
print('x=',x) #x=100



#난수 생성
import random # 난수 함수 제공 모듈 - 방법 1  -> random.random()
from random import uniform, randint # 방법2 -> random() 

#방법 1  -> random.random()
r1 = random.uniform(0,1) #모듈함수() : [a,b] #실수 난수 생성

# 방법2 -> random() 
r2 = uniform(0, 1)  # 함수()  #실수 난수 생성

print(r1,r2)
#0.3569949085601598 0.6114398013951978

r3=randint(1,10) #정수 난수 생성 
print(r3) #9


# size 만큼 난수 생성
size =1000
rdata = [uniform(0,1) for i in range(size)]
rdata #1000개 난수 생성

tot=0.0 #전역변수
def calc_func(data):
    global tot #전역변수 
    for x in data:
        tot +=x
    return tot/len(data) #평균

avg = calc_func(rdata)
print('나수 평균=',avg)
#난수 평균= 0.4898201577278601

















































