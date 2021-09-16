'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd

# 1. file read
emp = pd.read_csv('C:/ITWILL/3_Python-I/workspace/chap07_FileIO/data/emp.csv', encoding='utf-8')
print(emp.info())
'''
No      5 non-null int64
Name    5 non-null object
Pay     5 non-null int64
'''        

print(emp)
print('관측치 길이 : ', len(emp)) 

pay = emp.Pay
name = emp.Name

print('전체 급여 평균 : ', pay.mean())
max_pay = max(pay) # 최고 급여 
min_pay = min(pay) # 최저 급여 

print("="*30)
for i,p in enumerate(pay) : 
    if p == min_pay :
        print('최저 급여 : %d, 이름 : %s'%(p, name[i]))
    if p == max_pay :
        print('최고 급여 : %d, 이름 : %s'%(p, name[i]))
        
print("="*30)             
        

