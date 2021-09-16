'''
문3) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <출력 결과>
 전체 사원 급여 평균 : 260
'''

from re import findall
from statistics import mean

# <Vector 준비>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def pay_pro(emp):
    payment=[]
    for e in emp:
        re=findall('[0-9]{3}$',e) #['220']
        print(re) #['220']
        #pays.append(re) #[['220]]
        payment.append(int(re[0])) #'220' -> 220
    
    #list 내포
    payment2= [int(findall('[0-9]{3}$',e)[0]) for e in emp]
    
    return mean(payment), mean(payment2)


# 함수 호출 
pays_mean,pays_mean2 = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)
print('전체 사원의 급여 평균 :', pays_mean2)



def pay_pro(emp):
    payment=[]
    for e in emp:
        re=findall('[0-9]{3}$',e)
        payment.append(int(re[0]))
      
    return mean(payment)


# 함수 호출 
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)