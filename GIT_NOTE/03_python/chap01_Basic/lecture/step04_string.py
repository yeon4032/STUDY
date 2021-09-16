# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
step04_string.py

1. 문자열(string) 처리 
2. escape 문자 
"""


# 1. 문자열(string) 처리 
'''
 - 문자열(string) : 문자들의 집합 
 - 문자 분리 가능 : 순서 존재 
 - indexing/slicing 가능 
 - 수정불가(상수) : 새로운 객체 생성 
'''

# 1) 문자열 유형 
lineStr = "this is one line string" # 한 줄 문자열 
print(type(lineStr)) # 자료형 반환 - <class 'str'>
# <class 'str'> -> 객체의 출처를 제공 

# 여러줄 문자열 
multiLine = """This
is multi line
string"""
print(type(multiLine)) # <class 'str'>
print(multiLine)

multiLine2 = "this\nis multi line\nstring"
print(multiLine2)

# sql문 
query ="""select * from emp
where deptno = 1001
order by sal desc"""
print(query)


# 2) indexing/slicing 가능 
'''
R index : 1부터 -> [1]
Python index : 0부터 -> [0]
'''
print(lineStr) # this is one line string

# 왼쪽 기준 색인 
print('왼쪽의 첫번째 문자 : ', lineStr[0]) # t
print(lineStr[0:4]) # this : [start:stop-1]
print(lineStr[:4]) # this

# 오른쪽 기준 색인 
print(lineStr[-1]) # g
print(lineStr[-6:]) # string : [start:end]

# slicing : new object
subStr = lineStr[:4]
print(subStr) # this

# 객체 주소 
print(id(subStr), id(lineStr))
# 3086682858096 3086682915184


# 3) 문자열 연산 
print('python' + ' program') # 결합연산자 
print('-'*50) # 반복연산자 

#4) 문자열 처리 함수

#(1) 글자수 변환
print(len(lineStr)) #23 전체 문자길이

# 객체.멤버(속성+메서드) 
type(lineStr) #str

print(lineStr.count('t')) # 2 # 객체.메소드()

#(2) 접두어 판다 -> T/F
lineStr.startswith('this') # True
lineStr.startswith('that') # False

'''
함수(function) vs 메서드
일반함수 : 함수
객체의 함수 : 메서드
'''

#(3) 문자열 분리 & 결합 (join)
# 문단 -> 문장 split
# 문장 -> 단어 split

print(multiLine)
'''
This
is multi line
string
'''
# 문단 -> 문장 split
sent=multiLine.split(sep='\n') # 구분자 기준 토근 생성
print(sent, len(sent))
# ['This', 'is multi line', 'string'] 3

#문장-> 단어 split
words = multiLine.split() # sep='' : 공백 기준 토큰 생성
print(words,len(words))
#['This', 'is', 'multi', 'line', 'string'] 5


#문자열 결합(join)
lines = ' '.join(words)
print(lines)
# This is multi line string



# 2. escape 문자 
'''
escape 문자 : 특수기능의 문자(\n,\t,\b,\r,'',"")
-> 제어문자, 문자열 
'''

print('escape 문자')
print('\n출력') 
print('\n출력')
#escape 문자
#
#출력
#
#출력

print('escape 문자')
print('\\n출력') # escape 기능 차단1-> \ 
print(r'\n출력')# escape 기능 차단2 -> r
#escape 문자
#\n출력
#\n출력

#경로 표현
print('c:\python\test')
#c:\python	est <- because of 특수기능의 문자 \t

# want to print 'c:\python\test'
print('c:\\python\\test')
#c:\python\test
#or
print(r'c:\python\test')
#c:\python\test





















