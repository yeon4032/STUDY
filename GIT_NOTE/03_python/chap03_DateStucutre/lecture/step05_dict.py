# -*- coding: utf-8 -*-
"""
step05_dict.py

dict특징
- set과 유사함
형식) {key1:value1,key2:value2, .....}
- key를 색인 사용
- key 이용 -> 수정,삭제,추가, 검색
- key 중복 불가,순서 없음

"""

#1. dict 생성
person={'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) #{'name': '홍길동', 'age': 35, 'addr': '서울시'}
print(len(person), type(person)) # 3 <class 'dict'>

person['name'] #'홍길동' #색인 : 키

#2. 수정, 삭제, 추가, 검색
person['age'] =45 #수정
print(person)

del person['addr'] # 삭제
print(person)

person['pay'] = 350 #추가
print(person)

#key 검색
print('age' in person) #True (person 이라는 dict 에서 age 라는 키가 있다.)

#3. 단어 빈도수
charset = ['pay', 'name', 'pay', 'name', 'age']
charset

#방법1
wc={} # 빈 set

for ch in charset: #'pay'
    wc[ch]=wc.get(ch,0)+1 #{'pay':2, 'name':2, 'age':1}

print(wc)
#{'pay': 2, 'name': 2, 'age': 1}

help(wc.get)
#사전에 ket가 있으면 value를 반화하고, 없으면 defualt 수행

#방법2
wc2={}

for ch in charset:
    if ch in wc2: #사전에 key유무
        wc2[ch] += 1 #key 있음
    else:
        wc2[ch]=1 #key 없음

print(wc2)

#4. for + dict

for key in person: # person 의 key 값 만  key에 넘김
    print(key,end=' ') #key
    print(person[key]) #value
'''
name 홍길동
age 45
pay 350
'''


for key in person.keys(): # person 의 key 값 만  key에 넘김
    print(key,end=' ') #key
    print(person[key]) #value

for value in person.values(): # person 의 value 값 만  value에 넘김
    print(value) #key

for item in person.items(): # key와 value 둘다 넘김
    print(item)

# 5. {key : [value1,value2,....]}
#예시) {'사번' : [급여,수당]}
emp = {'1001' : [250,50], '1002': [200,40], '1003' : [300,80]}

#급여가 250 이상 이면 사번 출력 & 수당 합계 구라하라
su_tot=0

for eno, pay_su in emp.items(): # key +value
    if pay_su[0]>= 250: #급여 이용
        print(eno)#사번 출력
        su_tot += pay_su[1] #수당 누적

print('수당 합계: %d'%su_tot)

# 급여 +보너스
pay={'홍길동' : 200, '이순신' : 250, '유관순' : 200} #dict
bonus={'홍길동' : 50, '이순신' : 80, '유관순' : 30} #dict

pays= [pay[k]+bonus[k] for k in pay.keys()] # list  내포 한줄 for 문
pays # [250, 330, 230]

avg= sum(pays)/len(pays)
print('급여 평균=',avg)
#급여 평균= 270.0













