'''
문4) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd
import os
os.chdir('C:/ITWILL/3_Python-I/workspace/chap07_FileIO/data/')


# 1. file read
emp = pd.read_csv('emp.csv', encoding='utf-8')
print(emp.info())
       
