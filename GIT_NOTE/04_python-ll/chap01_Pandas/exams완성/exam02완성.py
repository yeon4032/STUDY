'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd
import os
os.chdir("c:/ITWILL/4_Python-II/data") # file 경로 변경 

# 단계 1 : 파일 가져오기, 정보 확인 
wdbc = pd.read_csv('wdbc_data.csv')
print(wdbc.info())
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 569 non-null    int64  
 1   diagnosis          569 non-null    object 
'''

# 단계 2 : y변수, x변수 선택
cols = list(wdbc.columns)
print(cols) # 전체 칼럼명 

# 중간 변수 제거 
del cols[20] # 21번째 변수 제거 
len(cols) # 31

wdbc_y = wdbc[cols[1]] # y변수 선택 
wdbc_x = wdbc[cols[2:]] # x변수 : 3번째 이후 변수 선택 

print(wdbc_y.shape) # (569,)
print(wdbc_x.shape) # (569, 30)

# 칼럼명 + 5개 관측치 
wdbc_x.head()
wdbc_x.tail()










    
