# -*- coding: utf-8 -*-
"""
step03_Descriptive.py

1. DataFrame의 요약통계량 
2. 상관계수
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_python-ll/data')
product = pd.read_csv('product.csv')

# 1. DataFrame의 요약통계량 
product.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 264 entries, 0 to 263
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   a       264 non-null    int64
 1   b       264 non-null    int64
 2   c       264 non-null    int64
'''

product.head()
product.tail()

# 요약통계량 
summ = product.describe()
print(summ)

# 행/열 통계
product.shape # (264, 3)
product.sum(axis = 0) # 행축 : 264개 더하기 - 같은 열 모음 
product.sum(axis = 1) # 열축 : 3개 더하기 - 같은 행 모음 

# 산포도 : 분산, 표준편차 
product.var() # axis = 0
product.std() # axis = 0

# 빈도수 : 집단변수 
product['a'].value_counts()
'''
3    126
4     64
2     37
1     30
5      7
'''

# 유일값 
product['b'].unique()
# array([4, 3, 2, 5, 1], dtype=int64)

# 2. 상관관계 
cor = product.corr()
print(cor) # 상관계수 행렬 


# iris dataset 
iris = pd.read_csv('iris.csv')
iris.info()

# 요약통계량 
des = iris.describe()
print(des)


# 집단변수 : 빈도수 
species = iris.Species
species.value_counts()
'''
virginica     50
versicolor    50
setosa        50
'''

species.unique()
# array(['setosa', 'versicolor', 'virginica'], dtype=object)

