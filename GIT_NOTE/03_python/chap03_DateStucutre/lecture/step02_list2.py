# -*- coding: utf-8 -*-
"""
step02_list2.py

리스트 내포
-list 에서 for와 if문을 한 줄로 표혀한 문법

형식1) 변수=[실행문 for 변수 in 열거형 객체]
    실행 순서: 1.for문 > 2.실행문 > 3.변수 저장
    입력대이터 수 = output수

형식2) 변수=[실행문 for 변수 in 열거형 객체 if 조건식]
    실행 순서: 1.for문> 2.if 문 >3.실행문 > 4.변수 저장 -> 조건이 참일때
    실행 순서: 1.for문> 2.if 문 >3. for문               -> 조건이 거짓일때
    입력데티어수 != output수

"""

# 형식1) 변수=[실행문 for 변수 in 열거형 객체]

#1) x변량에 제곱(**) 계산
x=[2,4,1,5,8]

print(x**2) #TypeError:

#list +for
lst = [] #계산결과 저장
for i in x:
    lst.append(i**2)

print(lst) #[4, 16, 1, 25, 64]

#list 내포 
lst=[i**2 for i in x]
print(lst) #[4, 16, 1, 25, 64]

# 2) 짝수/홀수 판단 :한줄 if문 = 실행문
lst2=['짝수'if i%2==0 else '홀수' for i in x]
print(lst2) #['짝수', '짝수', '홀수', '홀수', '짝수']

# 형식2) 변수=[실행문 for 변수 in 열거형 객체 if 조건식]
dataset=list(range(1000))
dataset

#10 배수 값 추출
dataset2=[ data  for data in dataset if data%10 == 0]
print(len(dataset2))100
print(dataset2)













