# -*- coding: utf-8 -*-
"""
step02_Car.py

동적 멤버변수 
 - 변수 선언 없이 특정 함수에서 멤버변수 생성 
self : 자신의 멤버를 호출하는 객체 
  - self.멤버변수
  - self.멤버메서드()
"""

# 1. 클래스 설계 
class Car :
    # 멤버변수 
    #door = cc = 0
    #name = None # null
    
    # 생성자 
    def __init__(self, name, door, cc) :
        # 동적 멤버변수 생성 
        # self.멤버변수 = 지역변수 
        self.name = name
        self.door = door
        self.cc = cc
        
    # 멤버메서드 
    def info(self) :
        self.kind = "" # 동적 멤버변수 
        if self.cc >= 3000 :
            self.kind = '대형'
        else :
            self.kind = '중소형'
            
        self.display() # 메서드 호출 
    
    def display(self) :
        print('%s는 %d cc이고(%s) 문짝은 %d개 이다.'
              %(self.name, self.cc, self.kind, self.door))

        
    
    
# 2. 객체 생성 : 차동차 생산 
car1 = Car('소나타', 4, 2000)    
# object.methed()
car1.info()     
# 소나타는 2000 cc이고(중소형) 문짝은 4개 이다.
    
car2 = Car('그랜저', 4, 3500)    
car2.info()    
# 그랜저는 3500 cc이고(대형) 문짝은 4개 이다.

car3= Car('소나타', 2000,4)
car3.info()
