# -*- coding: utf-8 -*-
"""
step04_Ineritance

1.클래스 상속
-기존 클래스-> 새로운 클래스 문법
-부모클래스 vs 자식클래스
-상속 대상 : 맴버(변수,메서드)
-생성자는 상속 대상 아님


형식) 
class 자식클래스 (부모클래스):
    멤버변수
    생성자
    맴버메서드

2. 메서드 재정의(overriede)
- 상속관계에서 나오는 용어
- 부모클래스의 원형 메서드-> 자식클래스에서 다시 작성
- 인수,내용 재작성

"""
class Super :
    #맴버면수:2개
    name=None
    age=0
    
    #생성자 : 객체생성 + 맴버변수 초기화
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 멤버메서드 1개
    def display(self):
        print('name: %s, age: %d'%(self.name, self.age))

sup = Super('부모', 55)
sup.display() #name: 부모, age: 55

#자식 클래스
class Sub(Super):# class 자식클래스(부모클래스)
    #부모 맴버면수:2개 (물려받음)
    #name,age(물려받음)
    #자식 멤버변수 추가
    gender=None
    
    #생성자 
    def __init__(self, name, age,gender):
        self.name=name #상속
        self.age=age #상석
        self.gender=gender #추가
    
    #멤버메서드:1개(물려받음) but can add new 멤버매서드 in that case need to write dispay with new 변수. 
    def display(self):   #display() 2개 -> 3개(확장) : 메서드 재정의
        print('name: %s, age: %d, gneder:%s'
              %(self.name, self.age, self.gender))

sub=Sub('자식',25,'남자')
sub.display() #name: 자식, age: 25, gneder:남자


#1. 부모클랫스 정의
class Parent:
    #멤버변수
    name=job=None
    
    def __init__(self,name,job):
        self.name=name
        self.job=job
        
    #멤버메서드: 메서드 재정의 (2개) 
    def display(self):
        print('name:%s, job: %s'%(self.name, self.job))
        
p=Parent('홍길동','공무원')    
p.display() #name:홍길동, job: 공무원

#2. 자식클래스1
class Child1(Parent):
    #부모멤버변수: nma=job=None
    gender = None

    def __init__(self,name,job,gender):
        self.name=name
        self.job=job
        self.gender = gender
        
    #멤버메서드: 메서드 재정의 (3개) 
    def display(self):
        print('name:%s, job: %s, gender: %s'%(self.name, self.job, self.gender))
        
ch1=Child1('이순신','해군장군','남자')
ch1.display()


#3. 자식클래스2
class Child2(Parent):
    #부모멤버변수: nma=job=None
    gender = None
    addr=None

    def __init__(self,name,job,gender,addr):
        self.name=name
        self.job=job
        self.gender=gender
        self.addr=addr

    #멤버메서드: 메서드 재정의 (4개) 
    def display(self):
        print('name:%s, job: %s,gender: %s, addr: %s'%(self.name, self.job,self.gender,self.addr))

ch2=Child2('유관순','독립열사','여자','충남')
ch2.display() #name:유관순, job: 독립열사,gender: 여자, addr: 충남











   




