'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd
import os
os.chdir("c:/ITWILL/4_Python-ll/data") # file 경로 변경 

# 단계 1 : 파일 가져오기, 정보 확인 

# 단계 2 : y변수, x변수 선택





































# 단계 1 : 파일 가져오기, 정보 확인 
wdbc=pd.read_csv('wdbc_data.csv')
print(wdbc.info())

# 단계 2 : y변수, x변수 선택
col_names=list(wdbc.columns)
wdbc_x=wdbc[col_names[2:]]
wdbc_y=wdbc[col_names[1]]
print(wdbc_x.shape) #(569, 30)
print(wdbc_y.shape) #(569,)

#중간 변수 제거
del col_names[20] #만약 21번째 컬럼을 삭제 해야하는 경우
len(col_names)

















