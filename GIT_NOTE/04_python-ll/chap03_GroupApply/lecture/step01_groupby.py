# -*- coding: utf-8 -*-
"""
step01_groupby.py

-집단변수(범주형)를 이용한 자료처리

1. 집단변수 기준 subset 만들기
2. 집단변수 기준 그룹&통계량
3. 그룹&통계량 시각화
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_python-ll/data')

#dataset load & 변수 확인
wine=pd.read_csv('winequality-both.csv')
print(wine.info())
'''
 0   type                  6497 non-null   object  object 집단변수
 :
 11  alcohol               6497 non-null   float64 float64 : 알콜
 12  quality               6497 non-null   int64   int64:와인 품질
'''

# 칼럼 공백->'-'교체
wine.columns = wine.columns.str.replace(' ','_')
wine.info()

wine.head()
wine.tail()

# subset 생성: 5 개 변수 선택
wine_df=wine.iloc[:,[0,1,4,11,12]]
wine_df.info()

#특정 칼럼명 수정
columns={'fixed_acidity':'acidity','residual_sugar':'sugar'} #dict
wine_df=wine_df.rename(columns=columns)
wine_df.info()

#집단변수 확인: 와인 유형
wine_df['type'].unique() #array(['red', 'white'], dtype=object)
wine_df['type'].value_counts() # 빈도수
'''
white    4898
red      1599
Name: type, dtype: int64
'''

#집단변수 확인 :와인품질
wine_df['quality'].unique() #[5, 6, 7, 4, 8, 3, 9] 3~9
wine_df['quality'].value_counts() #빈도수


#1. 집단변수 기준 subset 만들기

#1) 1개 집단 기준
red_wine = wine_df[wine['type']=='red'] # 레드 와인 선택
red_wine.shape #(1599, 5)

white_wine = wine_df[wine['type']=='white'] # 레드 와인 선택
white_wine.shape #(4898, 5)

#2) 2개 이상 집단 기준 
#- red, white, blue -> red & white
two_wine_df=wine_df[wine_df['type'].isin(['red','white'])]
two_wine_df.shape #(6497, 5)

#2. 집단변수 기준 특정 칼럼 선택: 1차원 구조
#1)레드와인 품질 칼럼
red_wine_quality=wine_df.loc[wine_df['type']=='red','quality']
red_wine_quality.shape #(1599,)

#2) 화이트와인 품질(quality) 칼럼
white_wine_quality=wine_df.loc[wine_df['type']=='white','quality']
white_wine_quality.shape #(4898,)

#3.집단변수 기준 그룹&통계량

#1) 집단 변수 1개 이용 그룹
#형식)DF.groupby('집단변수')

wine_group = wine_df.groupby('type')
wine_group #DataFrameGroupBy
wine_group.size()
#그룹별 서브셋 확인
for grp in wine_group:
    print(grp)
#[1599 rows x 5 columns]) red
#('red',칼럼명)
#[4898 rows x 5 columns]) white
#('white',칼럼명)

#집단별 통계량
wine_group.sum()
'''
        acidity     sugar   alcohol  quality
type                                        
red    13303.10   4059.55  16666.35     9012
white  33574.75  31305.15  51498.88    28790
'''
wine_group.mean()
'''
        acidity     sugar    alcohol   quality
type                                          
red    8.319637  2.538806  10.422983  5.636023
white  6.854788  6.391415  10.514267  5.877909
'''

#white 와인 기준: 알콜 높도,품질 우수
wine_group.var()

#wine_group 에서 사용가능한 함수 보여줌
dir(wine_group)

#그룹 특정 칼럼 기준 요약통계량
wine_group['alcohol'].describe()
'''
        count       mean       std  min  25%   50%   75%   max
type                                                          
red    1599.0  10.422983  1.065668  8.4  9.5  10.2  11.1  14.9
white  4898.0  10.514267  1.230621  8.0  9.5  10.4  11.4  14.2
'''

# 2) 집단변수 2개 이용
#형식) DF.groupby(['집단변수1','집단변수2'])
wine_grp = wine_df.groupby(['type','quality']) # 2*7=14(최대)
wine_grp.size()
'''
색인   색인         값
type quality
red    3            10
       4            53
       5           681
       6           638
       7           199
       8            18
white  3            20
       4           163
       5          1457
       6          2198
       7           880
       8           175
       9             5
'''

size=wine_grp.size()
size.shape #(13,)

#stack(1차원) -> unstack(2차원)-> 행열구조로 변경
wine_wide=size.unstack()
'''
quality     3      4       5       6      7      8    9
type                                                   
red      10.0   53.0   681.0   638.0  199.0   18.0  NaN
white    20.0  163.0  1457.0  2198.0  880.0  175.0  5.0
'''
wine_wide.shape#(2, 7) 2차원으로 변경

#4. 그룹&통계량 시각화
import matplotlib.pyplot as plt
type(wine_wide)#pandas.core.frame.DataFrame

#1)와인 유형별 품질: 빈도수 기준
wine_wide.plot(kind='barh',stacked=True,
               title='red vs white wine quality')
plt.show()

#2) 와인 유형별 품질:비율 기준
wine_wide.loc['red',:].plot(kind='pie')
plt.show()

wine_wide.loc['white',:].plot(kind='pie')
plt.show()

#3) 그룹 통계 시각화
grp_mean = wine_grp.mean() # 그룹평균
grp_mean

#그룹평균 시각화
grp_mean[['sugar','alcohol']].plot(kind='bar')
plt.show()
#해설-> 양질의 와인: 대체적으로 suger양 낮고,알콜농도 높음
