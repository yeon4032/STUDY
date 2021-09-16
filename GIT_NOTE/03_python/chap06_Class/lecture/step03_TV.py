# -*- coding: utf-8 -*-
"""
기본 생성자(묵시적 생성자)
 - 생성자를 생략하면 기본적으로 생성되는 생성자 
"""

class defualt :
    # 생성자 없음 
    
    # 멤버메서드 : data 생성 
    def data(self, x, y) :
        # 동적 멤버변수 생성 
        self.x = x
        self.y = y
        
    # 멤버메서드 : 곱셈     
    def mul(self) :
        print(self.x * self.y)
        
# 기본 생성자 
obj = defualt()
obj.data(10, 5)
obj.mul() # 50


# TV 클래스 정의 
class TV :
    # 멤버 변수 : tv 상태
    power = False # off(False)/on(True)
    channel = 10 # 채널 번호  
    volume = 5 # 볼륨 크기 
    
    # 기본 생성자 : 생략 -> 객체만 생성 
    def __init__(self) :
        pass
    
    # 멤버 메서드 : tv 동작 
    def changePower(self) :
        self.power = not(self.power) # F <-> T
        
    def channelUp(self) :
       self.channel += 1 # 카운터 변수 
       
    def channelDown(self) :
        self.channel -= 1
        
    def valumeUp(self) :
        self.volume += 1
        
    def valumeDown(self) :
        self.volume -= 1 
        
    def display(self) :
        print(f'전원 상태 : {self.power}, 채널 번호 : {self.channel}, 볼륨 크기 : {self.volume}')
        
    
tv1 = TV()    
tv1.display() # 전원 상태 : False, 채널 번호 : 10, 볼륨 크기 : 5

tv1.changePower() # off -> on
tv1.channelUp() # +1
tv1.valumeUp() # +1

tv1.display()
# 전원 상태 : True, 채널 번호 : 11, 볼륨 크기 : 6

'''
문) tv2 객체를 다음과 같이 생성하시오.
     조건1> 전원 on
     조건2> 채널 : 18번 
     조건3> 볼륨 : 10
     조건4> tv 정보 출력 : display() 호출 
'''
tv2 = TV() # 기본 생성자 

# 멤버 호출 
tv2.changePower()
for i in range(8) :
    tv2.channelUp() # 8회 호출 

for i in range(5) :
    tv2.valumeUp()
    
tv2.display() # 전원 상태 : True, 채널 번호 : 18, 볼륨 크기 : 10






