# -*- coding: utf-8 -*-
"""
step02_KMeans.py

kMeans 알고리즘
 - 확인적 군집분석
 - 군집수 k를 알고 있는 분석 방법
"""

import pandas as pd # DataFrame
from sklearn.cluster import KMeans # model 
import matplotlib.pyplot as plt # 구집결과 시각화
import numpy as np # array 

# 1. text file - dataset 생성
file = open('C:\\ITWILL\\4_python-ll\\data\\testSet.txt')
lines = file.readlines() # list 반환

print(lines)

dataset=[] # 2차원(80X2)
for line in lines: # '1.658985\t4.285136\n'
    cols = line.split('\t') # '1.658985'  '4.285136'
    
    rows = [] # 1 줄 저장
    for col in cols: # '1.658985' ->'4.285136'
        rows.append(float(col)) # 1.658985 
        
    dataset.append(rows)# [[1.658985,4.285136]]    
    

print(dataset) #중첩 list -> [[1.658985, 4.285136], [-3.453687, 3.424321], [4.838138, -1.151539],...]

# list :1d -> numpy(array): 2d
dataset_arr = np.array(dataset)
dataset_arr.shape # (80, 2) 
print(dataset_arr)

#2. numpy -> DataFrame(column 지정) 
data_df = pd.DataFrame(dataset_arr,columns=['x','y'])
data_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 80 entries, 0 to 79
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   x       80 non-null     float64
 1   y       80 non-null     float64
'''

# 3. Kmeans model 생성
model = KMeans(n_clusters=4, max_iter=300, algorithm='auto')
model.fit(data_df) # 학습

# 예측치 생성
pred = model.predict(data_df)
print(pred) # 0 ~ 3

# 군집 중앙값 
centers = model.cluster_centers_
type(centers)
print(centers)
'''
      X             Y
[[ 2.80293085 -2.7315146 ]
 [-2.46154315  2.78737555]
 [-3.38237045 -2.9473363 ]
 [ 2.6265299   3.10868015]]
'''

# clusters 시각화 :예측 결과 확인
data_df['predict'] = pred # 칼럼추가

#산점도
plt.scatter(x=data_df['x'],y=data_df['y'],c=data_df['predict'])

#중앙값 추가
plt.scatter(x=centers[:,0],y=centers[:,1],
            c='r',marker='D')

plt.show()












































