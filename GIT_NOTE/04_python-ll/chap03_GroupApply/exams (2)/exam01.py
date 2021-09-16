# -*- coding: utf-8 -*-
"""
문1) titanic 데이터셋을 대상으로 단계별로 처리하시오. 
"""

import seaborn as sn
import matplotlib.pyplot as plt


titanic = sn.load_dataset('titanic')
titanic.info()


# 단계1 : age, sex, class, fare, survived 칼럼으로 서브셋 생성 
df = titanic[['age','sex','class','fare','survived']]
print("승객 수 :", len(df))
print(df.head())

# 단계2 : class와 sex 칼럼 기준으로 그룹 객체 생성 및 크기 확인 



# 단계3 : 그룹별 평균 구하기 



# 단계4 : 그룹별 평균에서 survived 칼럼 기준 막대차트 시각화  

































# 단계1 : age, sex, class, fare, survived 칼럼으로 서브셋 생성 
df = titanic[['age','sex','class','fare','survived']]
print("승객 수 :", len(df))
print(df.head())

# 단계2 : class와 sex 칼럼 기준으로 그룹 객체 생성 및 크기 확인 
titanic_grp=df.groupby(['class','sex'])
titanic_grp.size()


# 단계3 : 그룹별 평균 구하기 
titanic_mean=titanic_grp.mean()

# 단계4 : 그룹별 평균에서 survived 칼럼 기준 막대차트 시각화  
titanic_mean['survived'].plot(kind='bar')
plt.show()

