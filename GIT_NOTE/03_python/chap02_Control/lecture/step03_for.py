# -*- coding: utf-8 -*-
"""
step03_for.py

반복문(for)

형식)
for 변수 in 열거형객체:
    실행문
    실행문
    
변수 in 열거형객체
-> 원소 순회-> 변수 넘김
열거형객체(iterable) 
-> iterable:반복가능
-> string, list, tuple, set, dict
"""


#1. 문자열(string) 객체
string = "나는 홍길동 입니다."
print(len(string))

#1문자 -> 변수
cnt=0
for s in string:
    cnt+=1 #카운터
    print(s,end='') #나는 홍길동 입니다.

print('cnt=',cnt) #cnt= 11 
#명령어들이 11번 반복되었다. 즉 문장이 복사된것이 아나라 단어 하나하나씩 복사된것이다.

#split-> 변수 넘김 -> 단어 단위로 복사 하고 플시
for word in string.split(sep=' '): # 뛰어쓰기 단위로 단어를 잘라서 넘긴다.
    print(word)
#나는
#홍길동
#입니다.

# 2. list 객체:vector와 동일함
lst=[1,2,3,4,5]
len(lst) #5

for i in lst:
    print(i)
#1
#2
#3
#4
#5

for i in lst:
    print(i, end='')
#12345


# 3. range 객체: 연속된 정수 생성
help(range)
'''
range(stop):0~stop-1 정수 
range(start, stop): strart ~stop -1  정수
range(start, stop, step) : start ~stop -l , step 단위 증감
'''
num1=range(10) #range(0, 10): 0~9
num2=range(1,11) #range(1, 11): 1~10
num3=range(1,11,2)#range(1, 11, 2): 1,3,5,7,9

#배열원소 확인
for n in num1:
    print(n,end=' ')
#0 1 2 3 4 5 6 7 8 9 

for n in num2:
    print(n,end=' ')
#1 2 3 4 5 6 7 8 9 10 

for n in num3:
    print(n,end=' ')
#1 3 5 7 9 


#4. list +range 객체
num=range(5)
print(num) #range(0, 5)

num=list(range(5))
print(num)
#[0, 1, 2, 3, 4]

#1) 자료 생성
lst=list(range(1,101)) #1~100
print(lst)

len(lst) # 100 

for i in lst:
    if i %2 == 0:
        print(i,end=' ')


#2) 색인으로 상용
y_true =[1,0,0,1,0] #정답
y_pred =[1,0,1,1,0] #예측치
 
size=len(y_true) #5

acc=0 #분류정확도

for i in range(size): # range(5) -> 0~4
    fit=int(y_true[i]==y_pred[i]) #Ture/False ->1/0
    acc += fit*0.2 # acc=acc+fit*0.2
    
print('분류정확도 =',acc) # 분류정확도 = 0.8

#5. 중첩 if문
'''
for i in 열거형객체:
    실행문
    for j in 열거형객체:
        실행문

'''

#문장-> 단어 처리
string ="""나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

string
'''
'나는 홍길동 입니다.\n 주소는 서울시 입니다.\n나이는 35세 입니다.'
'''

#빈 list
sents =[] #문장 저장
words=[] # 단어 저장

for sent in string.split(sep='\n'):
    sents.append(sent) #list 문장 추가
    for word in sent.split(sep=' '):
        words.append(word) # list 단어 추가
            
print(sents)
#['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 35세 입니다.']
len(sents) #3

print(words)
#['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
len(words) # 9


#for in vs if in 
'''
for 변수 in 열거형 객체:
    -> 원소 개수 만큼 반복
if 값 in 열거형객체:
    -> 값의 포함 유무(True or False)
'''

if '홍길동' in words:
    print('홍길동 있음')
    
else:
    print('없음')














    
