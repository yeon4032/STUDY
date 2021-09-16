# -*- coding: utf-8 -*-
"""
Pandas 객체 시각화 : 연속형 변수 시각화  
 kind = hist, kde, scatter, box 등 
"""

import pandas as pd # object
import numpy as np # dataset 
import matplotlib.pyplot as plt # chart
import os

# file 경로 
os.chdir('C:/ITWILL/4_python-ll/data')

# 1. 산점도 
dataset = pd.read_csv('dataset.csv')
print(dataset.info())

plt.scatter(dataset['age'], dataset['price'], c=dataset['gender'])
plt.show()


# 2. hist, kde, box

# DataFrame 객체 
df = pd.DataFrame(np.random.randn(10, 4),
               columns=('one','two','three','fore'))
print(df)

# 1) 히스토그램
df['one'].plot(kind = 'hist', title = 'histogram')
plt.show()

# 2) 커널밀도추정 :확률변수 X에 대한 활률 크기 추정 -> 밀도분포곡선
df['one'].plot(kind = 'kde', title='kernel density plot')
plt.show()

# 3) 박스플롯
df.describe() #요약통계량

df.plot(kind='box', title='boxplot chart')
plt.show()

