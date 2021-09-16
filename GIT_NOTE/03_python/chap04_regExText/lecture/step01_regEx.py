# -*- coding: utf-8 -*-
"""
step01_regEx.py

정규표현식
[주요 메타문자]
. : 임의의 한 문자 
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc) 
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.) 
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속 
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치   
"""

#findall( 규칙, string(list 안됨))

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

#import 모듈
import re # 정규표현식 모듈(re.py) -방법 1

#from 모듈 import 함수1,함수2,....
from re import findall,match,sub #방법2
# re 모듈의 함수: findall(), match(), sub()

#1. re.findall(pattern, string)
#패턴과 일치하는 문자열 찾기-> list 반환

#1) 숫자 찾기
print(re.findall('1234',st1)) #['1234']
print(re.findall('[0-9]', st1)) #['1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall('[0-9]{3}', st1)) #['123', '555']  -> 3개의 숫자가 연속된 경우 
print(re.findall('[0-9]{3,}', st1)) #['1234', '555'] -> 3개 이상의 숫자가 연속된 경우
print(re.findall('\\d{3,}', st1))#['1234', '555']  -> \\d=[0-9]

#2) 문자열 찾기
print(findall('[가-힣]{3,}',st1)) #['홍길동', '이사도시']
print(findall('[a-z]{3}',st1)) #['abc']
print(findall('[a-z|A-Z]{3}',st1)) #['abc', 'ABC']

words=st1.split(sep=' ') # 공백 기준 토큰 생성 (sep=' '생략가능)
words #['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names=[] #이름 저장
for w in words:
    re=findall('[가-힣]{3,}',w)
    print(re) #[] -> 
    
    if re : #True = not null([])
        names.append(re[0])

print(names) 
# ['홍길동', '이사도시']


#3. 접두어/접미어 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'

print(findall('^test',st2)) # ['test']

print(findall('test$',st2)) # ['test']

# abc, mbc
print(findall('.bc', st2)) # ['abc', 'mbc']


#4. 단어(\\w) 찾기 - 한글,영문,숫자(특수문자, 문장부호, 공백 제외)
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{3,}', st3)
print(words) # ['test', '홍길동', 'abc', '123', 'tbc']

#5. 문자열 제외:[^제외문자]
print(findall('[^t]',st3))
# ['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']

#특수문자 제외: ^ $
print(findall('[^^$]', st3))
# ['t', 'e', 's', 't', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', 't', 'b', 'c']

print(findall('[^^*$]+', st3))
# ['test', '홍길동 abc 대한', '민국 123', 'tbc']



# 2. re.match(pattern,string) : YES : object, No : Null
#- 패턴 일치 여부 반환

jumin='123456-1234567'

re= match('[0-9]{6}-[1-4][0-9]{6}', jumin)

if re: # true = object
    print('주민번호 양식')
else:
    print('잘못된 양식')
#주민번호 양식

jumin='123456-5234567'

re= match('[0-9]{6}-[1-4][0-9]{6}', jumin)

if re: # true = object
    print('주민번호 양식')
else:
    print('잘못된 양식')
#잘못된 양식


# 3. re.sub(pattern, replace,string) #gsub()유사함

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

text = sub('[\^*$]', '',st3)
print(text)
# test홍길동 abc 대한민국 123tbc

























