# -*- coding: utf-8 -*-
"""
step01_line_bar_pie.py

형식) object.plot(kind='차트유형', 속성)
object:Series(1차원),DataFrame(2차원)
kind=bar,pie,scatter,hist,boxplot 등
속성: 차트제목, 축이름, 등
"""

import pandas as pd # plot()
import numpy as np  # dataset
import matplotlib.pyplot as plt #plt.show()


#1. 기본 차트 시각화

#1) Series 객체 시각화
ser = pd.Series(np.random.randn(10),
          index = np.arange(0,100,10))
ser

ser.plot() # 선 그래프
plt.show()


# 2) DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10,4),
                  columns=['one','two','three','fore'])
df

# 기본 차트 :선그래프
df.plot() # 선 그래프
plt.show()

# 막대차트
df.plot(kind='bar',title='bar chart')
plt.show()

# 가로막대차트, 누적형
df.plot(kind='barh',title='barh chart',stacked=True)
plt.show()



# 2.dataset 이용 
import os 
os.chdir('C:/ITWILL/4_python-ll/data')

tips = pd.read_csv('tips.csv')
tips.info()

#범주형 변수 빈도수
tips['day'].unique() # ['Sun', 'Sat', 'Thur', 'Fri']
tips['size'].unique() #[2, 3, 4, 1, 6, 5]

# 행사 요일별 빈도수 & 파이 차트
cnt=tips['day'].value_counts()
'''
Sat     87
Sun     76
Thur    62
Fri     19
'''
type(cnt) # pandas.core.series.Series

cnt.plot(kind='pie')
plt.show()


# 요일(day) vs 규모(size) : 교차분할표
tab=pd.crosstab(index=tips['day'],columns=tips['size'])
tab
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''
type(tab) # pandas.core.frame.DataFrame (DataFrame이다)
tab.shape # (4,6)

print(tab.columns) # [1, 2, 3, 4, 5, 6]
print(tab.index)   # ['Fri', 'Sat', 'Sun', 'Thur']

#size:2~5 -> subset
party_tab=tab.loc[:,2:5] #Label index 방식
party_tab
'''
size   2   3   4  5
day                
Fri   16   1   1  0
Sat   53  18  13  1
Sun   39  15  18  3
Thur  48   4   5  1
'''
party_tab.plot(kind='barh',stacked=True,
               title='day va size plotting')
plt.show()

































