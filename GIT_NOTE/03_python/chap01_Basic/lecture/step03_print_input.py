# -*- coding: utf-8 -*-
"""
step03_print_input.py

1.print() :표준출력장치 - 콘솔 출력
2.input() : 표준입력장치 -키보드 입력


"""

#1.print()
help(print)
#Help on built-in function print in module builtins:

#print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)  
    
#1)기본 인수
print("value=", 10, 10+20) # sep=''
print('010','1234','1111', sep='-') # 010-1234-1111 #sep='-' 일때

#end 속성 (end='\n'-> 줄바꿈 속성)
print('value=', 10,end=',')
print('value=', 20) #value= 10,value= 20

#2) % 양식문자
#형식) print('%양식문자')

num1=10;num2=20
tot=num1+num2
print('%d +%d = %d'%(num1,num2,tot))#10 +20 = 30

#%s 외부의 문자열 받음
#%d 외부의 10진수 숫자 받음
print('이름은 %s이고, 나이는 %d 이다' %('홍길동',35))#이름은 홍길동이고, 나이는 35 이다

# %8.3f는 실수형 숫자 받음
print('원주율= %8.3f' %(3.14159)) #원주율=    3.142

#50% (%%을 사용해야 %를 프린트 한다.)
print('전체 찬성률은 %d%%' %50) #전체 찬성률은 50%

#3) format()함수 이용
#형식) '{형식}'.format(값)
print('이름은 {}이고, 나이는 {}이다.'.format('홍길동',35))
#이름은 홍길동이고, 나이는 35이다.

#{상수위치: 형식}
print('정수형= {0:d},{1:5d}' .format(123,123))
#정수형= 123,  123  

print('원주율={0:.3f},{1:8.3f}'.format(3.14159,3.14159))
#원주율=3.142,   3.142

#축약형 format
name='홍길동'; age=35
sql=f"select *from emp where name ='{name}' and age= {age}"
#위의 문장과 같다.-> sql=f"select *from emp where name ='{}' and age= {}".format(name,age)
print(sql)
#select *from emp where name ='홍길동' and age= 35

# 2. input()

# 키보드(문자) -> 정수형 변환 
a = int(input('첫번째 숫자 입력 : ')) # 10
b = int(input('두번째 숫자 입력 : ')) # 20

c = a + b
print('c=', c) # c= 30


# 키보드(문자) -> 실수형 변환  
x = float(input('첫번째 실수 입력 : '))
y = float(input('두번째 실수 입력 : '))
z = x + y
print('z=', z) # z= 48.010000000000005


# 3. 형 변환(Casting)
print(int(24.5)) # 실수 -> 정수 
#print(int('hello')) # ValueError:
print(2 + int('2')) # 문자열 -> 정수 : 덧셈 연산 
print('나이 :' + str(35)) # 정수 -> 문자열 : 결합 연산 

# boolean형 -> 정수 
print(int(True)) # 1
print(int(False)) # 0




















