# -*- coding: utf-8 -*-
"""


@author: sihun
"""
#1.단일 list & 색인
lst=[1,2,3,4,5]
print(lst)
len(lst)


#색인(index):값의 위치(시작=2 부터)
lst[:]# 전체 원소
lst[0] # 1 - 첫번째 원소
lst[-1] # 5- 마지막 원소

#for 변수 이용
for i in lst: # [1,2,3,4,5]
    print(lst[i-1:]) # i-1 이후
#[1, 2, 3, 4, 5]
#[2, 3, 4, 5]
#[3, 4, 5]
#[4, 5]
#[5]

for i in lst: # [1,2,3,4,5]
    print(lst[:i]) # i 이전까지
#[]
#[1]
#[1, 2]
#[1, 2, 3]
#[1, 2, 3, 4]

x = list(range(1,101)) # 1 ~ 100
print(x)

print(x[:5])
print(x[-5:])

# 2씩 증가
# 형식) 변수[start:stop:step] 
print(x[:]) #전체  [start:stop]
print(x[::2]) #홀수 수열 [start:stop:step] 

print(x[1::2]) #[start=1,stop=전체,step=2]


# 2. 중첩 list & 색인
y= [['a','b','c'],[1,2,3]]
print(y) #[['a', 'b', 'c'], [1, 2, 3]]

print(y[0]) #['a', 'b', 'c']
print(y[1]) #[1, 2, 3]
print(y[1][2]) # 3 - 두번째 원소 (3번째 개별 원소)
print(y[0][1:])#['b', 'c']

#3. 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 2, 'three', 4]
print(num) #['one', 2, 'three', 4]
len(num) # 4

# list 추가
num.append('five') # object.method()
print(num) # ['one', 2, 'three', 4, 'five']

#list 삭제
num.remove('three')
print(num) #['one', 2, 4, 'five']

#list 수정: 색인 이용
num[1]='two'
print(num) # ['one', 'two', 4, 'five']

#list 삽입
num.insert(0,'zero')
print(num) #['zero', 'one', 'two', 4, 'five']

# 4. list 연산
x=[1,2,3,4]
y=[1.5,2.5]

# 1) list 결합(+)
z= x + y # new object 
print(z) #[1, 2, 3, 4, 1.5, 2.5]

# 2) list  확장
x.extend(y) # old object -단일
print(x) #[1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가
x.append(y) #old object -중첩 list 
print(x) #[1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 반복(*)
result = y * 2
print(result) # [1.5, 2.5, 1.5, 2.5]

# 5) 사칙연산: 원소 대상
y[0] * 2 #3.0
y[1] * 2 

for i in y: 
    print(i * 2)

#5. list 객체 메서드 확인
type(x) #list

dir(x) # 객체 메서드 확인
x  # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

x.count(4) # 1 - x 에서 4 값은 하나 있다. (개수 반환)
x.pop(0) # 1 - 해당원소 추출/ 제거
x # [2, 3, 4, 1.5, 2.5, [1.5, 2.5]] # 1 없어짐
y.sort() # 오름차순 정렬
y #[1.5, 2.5]

y.sort(reverse = True) # 내림차순 정렬x
y #[2.5, 1.5]

x.clear() #모든 원소 제거
x #[]



# 6. 얕은 복사, 깊은 복사
names=['홍길동','이순신','유관순']
names

# 1) 얕은 복사: 주소 복사
names2=names#주소복사3
print(id(names),id(names2)) #2826237463872 2826237463872 #주소 같음
print(names,names2) #내용도 동일

#2) 깊은 복사: 내용 복사
names3=names.copy()
print(id(names),id(names3)) #2826237463872 2826237732096 # 주소는 다름
print(names,names3) #내용 동일


# 원본 객체 수정
names[0] = 'hong'
print(names,names2,names3)
#['hong', '이순신', '유관순'] ['hong', '이순신', '유관순'] ['홍길동', '이순신', '유관순']



#7. list 에서 원소 찾기
'''
if '원소' in list:
    list에 '원소' 포함
'''

num=[] #빈 list: 숫자 저장

for i in range(5): #0~4
    num.append(10)

num #[10, 10, 10, 10, 10]

#####################################################33
num=[] # 빈 list: 숫자 저장

for i in range(5): #0~4
    num.append(int(input('숫자 입력: ')))
num #[1, 2, 3, 4, 5]

#원소 찾기
if int(input()) in num:
    print("숫자 있음")
else:
    print('숫자 없음')




































