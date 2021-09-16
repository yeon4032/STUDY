'''
 문2) 다음과 같은 출력 결과가 나타나도록 동적 멤버 변수 생성으로 산포도(Scattering)
      클래스를 완성하시오.

 << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

class Scattering:
    def __init__(self, x): # 생성자
        self.x = x # 동적 멤버변수 생성 

    def var_func(self): # 분산 메서드
        # var = sum((x-산술평균)**2) / n-1
        avg = mean(self.x) # x의 산술평균  -> 함수 이기 때문에 list 랑 튜블은 그냥 쓸수 있음
        diff = [(i-avg)**2  for i in self.x] # 차의 제곱  -> 함수가 아님으로 list 인  self.x 는 for 문을 사용해 list 에서 벗어나게 한다.
        self.var = sum(diff) / (len(self.x) - 1) # 분산 : 동적멤버변수  
        return self.var 

    def std_func(self): # 표준편차 메서드
        #st = sqrt(분산)
        st = sqrt(self.var)
        return st


# 객체 생성 
scatt = Scattering(x)  # 생성자 -> 객체 생성
# 메서드 호출 
var = scatt.var_func()  # 분산 반환
st = scatt.std_func()  # 표준편차 반환
# 결과 출력 
print('분산 = ', var)
print('표준편차 =', st)




 
        
    
    



