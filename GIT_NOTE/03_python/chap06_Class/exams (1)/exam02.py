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
        pass

    def var_func(self): # 분산 메서드
        pass

    def std_func(self): # 표준편차 메서드
        pass


scatt = Scattering(x)  # 생성자 -> 객체 생성
var = scatt.var_func()  # 분산 반환
st = scatt.std_func()  # 표준편차 반환

print('분산 = ', var)
print('표준편차 =', st)




 
        
    
    



