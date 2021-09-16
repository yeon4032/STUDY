'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd
import os
os.chdir("C:/ITWILL/4_python-ll/data") # file 경로 변경 

iris = pd.read_csv('iris.csv')

#조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    


#조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
#col1


#col2


#col3


#col4


#조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성



#조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성     

























# 조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']

# 조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기
col1.sum()
col1.mean()
col1.std()

col4.sum()
col4.mean()
col4.std()


# 조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.concat(objs=[col1, col2], axis=1)
#df1 = pd.DataFrame({'col1':col1, 'col2':col2})
df2 = pd.concat(objs=[col3, col4], axis=1)
#df2 = pd.DataFrame({'col3':col3, 'col4':col4})
df1.head()
df2.head()


# 조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성
iris_df = pd.concat(objs=[df1, df2], axis = 1)
iris_df.info()
iris_df.head()
iris_df.tail()

























