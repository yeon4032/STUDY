# -*- coding: utf-8 -*-
"""
step02_while.py

반복문(while)

형식)
While 조건식:
    실행문
    실행문
    
@author: sihun
"""

#카운터 변수, 누적 변수
cnt=tot=0 #변수 초기화

while cnt<5 :
    cnt += 1 # cnt = cnt + 1
    tot += cnt # tot = tot + cnt
    print(cnt,tot)
'''
1 1
2 3
3 6
4 10
5 15
'''


# 무한 루프 -> exit 조건 지정 해야한다. 

while True:
    num = int(input('숫자 입력: '))
    
    if num == 0: #exit 조건
        print('프로그램 종료')
        break #Loop exit
    
    print('입력값->',num)
    
#컴퓨터 난수 생성
import random # 난수 생성 모듈 (class, function)

#0~1 사이 난수 실수
r=random.random() # 모듈.함수()
print('r=',r) #r= 0.9960551420316253

help(random.random)
# x in the interval [0, 1).  -> 0 <= r < 1


#문제) 난수 0.01미만이면 프로그램 종료 아니면 난수 개수 출력
cnt=0 #난수 개수 카운트

while True:
    r=random.random()
    cnt += 1
    
    if r <0.01: #exit 조건
        print('프로그램 종료')
        break


print('난수 개수=',cnt)


print('>>숫자 맞추기 게임<<')
'''
숫자 범위 : 1~10 -> 난수 정수 이용
myinput == computer:'성공(exit)'
myinput > computer: '더 작은 수 입력'
myinput < computer: '더 큰 수 입력'
'''

com = random.randint(1, 10) # [a ~ b] 난수 정수

while True:
    my = int(input('예상 숫자 입력: '))
    
    if my==com:  #exit 조건
        print('~성공~')
        break
    elif my>com:
        print('더 작은 수를 입력')
    elif my<com:
        print('더 큰 수 입력')
    
'''
break, continue : 반복문에서 사용된느 명령어
- break : 해당 반복문 탈출 (exit)
- continue : 계속 반복, 다음 문장 skip
'''
i=0 
while i<10:
    i+=1#카운터
    
    if i==3:
        continue
    if i==6:
        break
    print(i,end=' ') #1 2 4 5 













