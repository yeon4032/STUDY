# -*- coding: utf-8 -*-
"""
문2) 아래와 같은 단계로 kMeans 알고리즘을 적용하여 확인적 군집분석을 수행하시오.

 <조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
                   visit_count : 매장방문횟수, avg_price : 평균구매액

  단계1 : 3개 군집으로 군집화
 
  단계2: 원형데이터에 군집 예측치 추가
  
  단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
  
  단계4 : 산점도에 군집의 중심점 시각화

   단계5 : 군집별 특성분석 : 우수고객 군집 식별
"""

import pandas as pd
from sklearn.cluster import KMeans # kMeans model
import matplotlib.pyplot as plt


sales = pd.read_csv("C:\\ITWILL\\4_python-ll\\data/product_sales.csv")
print(sales.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
tot_price      150 non-null float64 -> 총구매금액 
visit_count    150 non-null float64 -> 매장방문수 
buy_count      150 non-null float64 -> 구매횟수 
avg_price      150 non-null float64 -> 평균구매금액 
'''
#<조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
#                   visit_count : 매장방문횟수, avg_price : 평균구매액

# 단계1 : 3개 군집으로 군집화
model = KMeans(n_clusters=3, max_iter=300, algorithm='auto')
model.fit(sales) # 학습


# 단계2: 원형데이터에 군집 예측치 추가
pred = model.predict(sales)
print(pred) # 0 ~ 3

# 예측치 추가
sales['predict'] = pred
  
# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
corr=sales.corr()
corr['tot_price']
'''
tot_price      1.000000
visit_count    0.817954
buy_count     -0.013051
avg_price      0.871754
predict       -0.349480
Name: tot_price, dtype: float64
'''
# tot_price vs avg_price
plt.scatter(x=sales['tot_price'],y=sales['avg_price'],c=sales['predict'])

  
# 단계4 : 산점도에 군집의 중심점 시각화
centers = model.cluster_centers_
#중앙값 추가
plt.scatter(x=centers[:,0],y=centers[:,3],
            c='r',marker='D')
plt.show()


# 단계5 : 군집별 특성분석 : 우수고객 군집 식별
grp=sales.groupby('predict') #예측치 기준 그룹 생성
grp.size() # 군집수 확인
'''
predict
0    38
1    50
2    62
dtype: int64
'''

#2) 통계
grp.mean()
'''
         tot_price  visit_count  buy_count  avg_price
predict                                              
0         6.850000     2.071053   3.071053   5.742105
1         5.006000     0.244000   3.284000   1.464000
2         5.901613     1.433871   2.754839   4.393548 -> 가장 우수한 고객 집단

'''

# 3) 가장 우수한 고객 집단 생성
vip = sales.loc[sales['predict']==2]
vip.info()




