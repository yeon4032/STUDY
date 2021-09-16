'''
 <급여 계산 문제> 
문4) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 구현하시오.
    <조건1> 정규직과 임시직의 급여 계산 방식에 따라서 pay_pro 메서드 재정의   
    <조건2> 정규직 급여 = 기본급(basic) + 보너스(bonus)
    <조건3> 임시직 급여 = 근무시간(time) * 시급(tpay)
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    
    # 원형 메서드 : 급여 계산 함수     
    def pay_pro(self):
        pass

# 자식클래스 - 정규직 
class Permanent(Employee):
    # 생성자 
    def __init__(self, basic, bonus,name) : #기본급 +상여금
        self.basic = basic
        self.bonus = bonus
        self.name = name
        
    def pay_pro(self):
        self.pay=self.basic+self.bonus
        return self.pay
        
    def display(self):
        print('%s,정규직 급여=%d'%(self.name, self.basic+self.bonus))

p=Permanent(10000000000000000000, 1000000, '정규직')
p.display()

print('구분:{0}, 정규직 급여 = {0:3,d}'.format(p.name, p.pay_pro()))

    
# 자식클래스 - 임시직 
class Temporary(Employee):
    # 생성자 
    def __init__(self, time, tpay,name) : # 금여 = 시간 *시급
        self.time = time
        self.tpay = tpay
        self.name = name

    def pay_pro(self):
      self.pay=self.time * self.tpay
      return self.pay
  

    
p1=Temporary(1000000000,10,'정규직')
print('구분:{0}, 임시직 급여= {0:3, d}'.format(p1.name, p1.pay_pro()))


    
    
