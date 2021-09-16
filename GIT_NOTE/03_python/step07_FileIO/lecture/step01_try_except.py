# -*- coding: utf-8 -*-
"""
step01_try_except.py

예외처리: 예상치 못한 오류 처리 방법

try:
    예외발생 코드
except 예외처리클래스 as 별칭:
    예외처리 코드
finally:
    항상 실행 코드
    
"""

x = [10,20,35.5,15, 'num' ,14]
len(x) # 6

# 예외처리 전
for i in x:
    print('i-',i)
    y=i**2 #산술연산 : TypeError: pow(): 'str' and 'int'
    print('y=', y)

# 예외처리 후
for i in x:
    try:        
        print('i-',i) # 정상 문장
        y=i**2 #산술연산 
        print('y=', y)
    except :
        print('숫자 아님')
'''
i- 10
y= 100
i- 20
y= 400
i- 35.5
y= 1260.25
i- 15
y= 225
i- num
숫자 아님
i- 14
y= 196
'''


#유형별 예외처리
# 산술적 예외
try:
    # 예외 발생 가능 코드
    div = 1000/25.5 # 정상 코드
    print('div=%.3f' %(div)) #div=39.216
    #div2=1000/0 #1차 - 산술적 예외
    file=open('c:/text.txt', mode='r') # 2차 -파일입출력 예외
 
except ZeroDivisionError as e:
    print('오류 정보 :', e) #오류 정보 : division by zero
except FileNotFoundError as e:
    print('오류정보:', e)



#파일 입출력 예외
try:
    # 예외 발생 가능 코드
    div = 1000/25.5 # 정상 코드
    print('div=%.3f' %(div)) #div=39.216
    #div2=1000/0 #1차 - 산술적 예외
    file=open('c:/text.txt', mode='r') # 2차 -파일입출력 예외
 
except ZeroDivisionError as e:
    print('오류 정보 :', e) 
except FileNotFoundError as e:
    print('오류정보:', e) #오류정보: [Errno 2] No such file or directory: 'c:/text.txt'



#예상하지 못한 오류의 예외처리
try:
    # 예외 발생 가능 코드
    div = 1000/25.5 # 정상 코드
    print('div=%.3f' %(div)) #div=39.216
    #div2=1000/0 #1차 - 산술적 예외
    #file=open('c:/text.txt', mode='r') # 2차 -파일입출력 예외
    num=int(input('숫자 입력: ')) #3차 - 기타예외
    print('num=',num)
except ZeroDivisionError as e:
    print('오류 정보 :', e) 
except FileNotFoundError as e:
    print('오류정보:', e) #오류정보: [Errno 2] No such file or directory: 'c:/text.txt'
except Exception as e: #Exceptino class 는 생략가능 -> 오류의 유형을 판단하기 힘들때 사용. # 마지막 블럭에서 사용
    print('기타 오류 정보:', e) #기타 오류 정보: invalid literal for int() with base 10: 'text'
finally:
    print('항상 실행되는 영역')




































