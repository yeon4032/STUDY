# -*- coding: utf-8 -*-
"""
step03_tuple.py

tuple 특징
-1차원 배열 구조
-형식) 변수 = (값1,값2,...)
-순서존재,색인 사용
-수정 불가
-list  비해 속도 빠름
@author: sihun
"""
#tuple
tp=(10)   # tp=10 #일반적으로 tp에 숫가값 입력
tp=(10,)  # tuple 입력 (#,)-> ,를 꼭 써야한다
print(tp) #(10,)

tp2=(1,2,3,4,5)
print(tp2) #(1, 2, 3, 4, 5)

print(len(tp2),type(tp2)) #5 <class 'tuple'>

#indexing 가능 (색인)
print(tp2[0], tp2[1:4])# 1 (2, 3, 4)
print(tp2[-1],tp2[-3:])# 5 (3, 4, 5)

#수정이 불가능
tp2[0]=100
#TypeError:tuple' object does not support item assignment
#오류 발생

#객체 삭제는 가능
del tp2
print(tp2) # NameError: name 'tp2' is not defined

#원소 삭제는 불가능
del tp2[0]

# for +tuple
datas=(10, 23.4, 6, 8)
print(datas)
for d in datas:
    print(d*2,end=' ')

#zip(): vector 원소 묶음 -> tuple 반환
name= ['hong', 'lee', 'kang']
pay=[100,200,300]

zip_re = zip(name, pay)
zip_re #<zip at 0x1e7eb8857c0>

for z in zip_re:
    print(z)
'''
('hong', 100)
('lee', 200)
('kang', 300)
'''

zip_re2=list(zip(name,pay))
print(zip_re2) 
# [('hong', 100), ('lee', 200), ('kang', 300)]














































