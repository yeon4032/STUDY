# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:19:05 2021
변수(Variable)
 - 자료가 저장된 메모리 이름 
 - 형식) 변수명 = 값 or 수식 or 변수명 
 - 자료형 선언 없음 : R 동일함 
 - 모든 변수는 객체 : R 동일함 
"""

# 단축키 : F5(전체 실행), F9(블럭 or 줄 단위)
# 1. 변수와 자료형 
var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)

# type : 객체 출처 확인  
print(type(var1), type(var2)) # <class 'str'> <class 'str'>

var1 = 100 # 변수 수정  
print(var1, type(var1)) # 100 <class 'int'>

var3 = 123.2345
print(var3, type(var3)) # 123.2345 <class 'float'>

var4 = True
print(var4, type(var4)) # True <class 'bool'>


# 2. 변수명 작성 규칙(ppt.12)
'''
- 첫자 : 영문자 or _ 사용가능 
- 두번째 : 숫자 사용 가능 
- 대소문자 구분(Score, score)
- 낙타체 : 두 단어 결합(korScore)
- 키워드(클래스명, 함수명) 사용불가, 한글명 비권장
- 점(.) 사용 불가  
'''

_num10 = 10
_Num10 = 20
print(_num10 * 2) # 20
print(_Num10 * 2) # 40

# 키워드 확인 
import keyword # 모듈 임포트(포함) 
kword = keyword.kwlist
print(kword)
print('word 개수 =', len(kword)) # word 개수 = 35

# 낙타체
korScore = 89
matScore = 75
engScore = 55

tot = korScore + matScore + engScore
print('tot =', tot) # tot = 219

# 3. 참조변수 : 객체가 저장된 메모리 주소 저장 
x = 150 # 150 객체의 주소 
y = 45.23 
x2 = x # x 주소 복사 
y2 = 45.23

print(x) # x주소 접근 -> 150 출력 
print(id(x)) # 140727080663504
print(id(x2)) # 140727080663504

print(id(y), y) # 2438250262320 45.23
print(id(y2), y2) # 2438250262320 45.23












