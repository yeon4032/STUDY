# -*- coding: utf-8 -*-
"""
step04_set.py

set 특징
-순서 없음(색인 사용불가)
-중복 허용 불가
-수정 불가 (추가,삭제 가능)
형식)변수={값1, 값2,....}
-집합 개념 사용
"""

#1.set 생성
st={1,3,5}
print(st,len(st)) # {1, 3, 5} 3

#중복 허용 불가
st={1,3,5, 1, 5}
print(st,len(st)) # {1, 3, 5} 3

# for + set
for s in st:
    print(s, end=' ') #1 3 5

# 삭인 사용 불가 
print(st[0]) #순서가 없음으로 색인 사용 불가능
#TypeError: 'set' object is not subscriptable

#2. 중복 불가 
gender=['남','여','남','여'] #list
gender

#list-> set
sgender=set(gender)
print(sgender) #{'남', '여'}

#set -> list
re=list(sgender)
print(re[0]) # 남

#집합관련 
set1={3,6}
set2={1, 3, 5}

#원소 추가 
set2.add(7)
print(set2) # set2={1, 3, 5,7}

set1.union(set2) # 합집합: {1, 3, 5, 6}
set1.difference(set2) # 차집합: {6}
set1.intersection(set2) # 교집합: {3}

#원소 사제
set2.discard(7)
print(set2) # {1, 3, 5}

#update:수정 불가능 - 여러 가지 값 추가 
set2.update([7,9,11])
print(set2) # {1, 3, 5, 7, 9, 11}

























































