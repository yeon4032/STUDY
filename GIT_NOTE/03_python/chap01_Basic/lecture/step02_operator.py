# -*- coding: utf-8 -*-
"""
step02_operator.py

연산자(operator)
 1. 할당연산자(=) : 변수에 값 할당 
 2. 연산자 : 산술,관계,논리 연산자 
"""


# 1. 할당연산자(=)
#i = 10
#tot = 10
i = tot = 10 # 변수 초기화 
print(i, tot) # 10 10
i += 1 # i = i + 1 -> 카운터 변수 
tot += i # tot = tot + i -> 누적 변수 
print(i, tot) # 11 21

# 서로 다른값 할당 
v1, v2 = 100, 200
print(v1, v2)

# 변수 값 교체
v2, v1 = v1, v2
print(v1, v2)

# 패킹(packing) 할당 
lst = [1,2,3,4,5] # 1차원 : vector 
print(lst) # [1, 2, 3, 4, 5]

v1, *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5


# 2. 연산자 : 산술,관계,논리 연산자 
num1 = 100 
num2 = 10 

# 1) 산술연산자 
add = num1 + num2
print('add=', add) # add= 110

sub = num1 - num2
print('sub =', sub) # sub = 90

div = num1 / num2 
print('div =', div) # div = 10.0

div = num1 // num2 
print('div =', div) # div = 10

div2 = num1 % num2
print('div2=', div2) # div2= 0

mul = num1 * num2
print('mul=', mul) # mul= 1000

square = num1 ** num2
print('square=', square) # square= 100000000000000000000


# 2) 관계 연산자 
# (1) 동등비교 
result = num1 == num2
print(result) # False

result = num1 != num2
print(result) # True

# (2) 크기비교 
result = num1 > num2
print(result)

result = num1 >= num2
print(result)

result = num1 < num2
print(result)

result = num1 <= num2
print(result)

# 3) 논리 연산자
result = num1 >= 50 and num2 <= 20
print(result) # True

result = num1 < 50 or num2 <= 20
print(result) # True

result = not(num1 < 50)
print(result) # True










