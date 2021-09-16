# -*- coding: utf-8 -*-
"""
제어문: 조건문 + 반복문

1. 조건문(if)
python 블럭: 콜론과 들여쓰기(tab키)

내어쓰기:tab+shif
@author: sihun
"""
'''
형식1)
if 조건식:
    실행문
'''

var=10 #초기화
if var>= 5:
    print('var=',var)
    print('var는 5보다 크다')

print('항상 실행 영역')

var=4 #초기화
if var>= 5:
    print('var=',var)
    print('var는 5보다 크다')

print('항상 실행 영역')


'''
형식2)
if 조건식 :
    실행문1 :True
else:
    실행문2 :False
'''
var = int(input('var변수에 값 입력:'))
#var=2
if var>=5:
    print('var는 5이상')
else:
    print('var는 5미만')

'''
형식3)
if 조건식1: 
    실행문1 -> 조건식1 True
elif 조건식2: 
    실행문2 -> 조건식2 True
else:
    실행문3 -> 모든조건이 False
'''

#키보드 점수 입력:100~85:'우수 , 84~70: '보통', 69미만: '저조'
score=int(input('점수 입력:'))

if score>= 85 and score<=100:
    print('우수')
    grade='우수'
elif score>=70:
    print('보통')
    grade='보통'
else: 
    print('저조')  
    grade='저조'

print('점수는 %d이고, 등급은 %s 이다'%(score,grade))
#점수는 92이고, 등급은 우수 이다

#블록 if vs 한줄 if

#블록 if예시
num=9

if num>=5:
    result=10
else:
    result=20

print('result=',result) #result= 10

#한줄 if
#형식) 변수 = 참 if 조건문 else 거짓

result = 10 if num>=5 else 20
print('result=',result) # result= 10

#if 조건식 in dataset
names=['홍길동','이순신','유관순'] #vector 변수

if '이순신' in names:
    print('이순신 있음')
else:
    print('이순신 없음')


