# -*- coding: utf-8 -*-
"""
step04_model_plot.py

-분석모델 관련 식가화

"""

import matplotlib.pyplot as plt
import seaborn as sn

#dataset 로드
flights=sn.load_dataset('flights')
flights.info()
'''
 0   year        144 non-null    int64    -> x:시간축
 1   month       144 non-null    category -> 집단변수
 2   passengers  144 non-null    int64    -> y:탑승객
 '''
 
iris =sn.load_dataset('iris')
iris.info()

 #1.오차대역폭을 갖는 시계열: x:시간축, y:통계량
sn.lineplot(x='year',y='passengers', data=flights)
plt.show()

#hue 추가
sn.lineplot(x='year',y='passengers', hue='month', data=flights)
plt.show()

#2. 선형회귀모델: 산점도 +회귀선
sn.regplot(x='sepal_length',y='petal_length',
           data = iris) #hue 사용 불가
plt.show()


sn.lmplot(x='sepal_length',y='petal_length',
           hue='species', data = iris) #hue 사용 가능
plt.show()

#3. heatmap: 분류분석 평가
import pandas as pd


#y_true vs y_pred 
y_true=pd.Series([1,0,1,1,0]) #정답
y_pred=pd.Series([1,0,0,1,0]) #예측치

#교차분할표 (혼돈 메트릭스)
tab=pd.crosstab(y_true,y_pred,rownames=['관측치'],colnames=['예측치'])

print(tab)
'''
예측치  0  1
관측치      
0    2  0
1    1  2
'''
#분류정확도
score= (tab.iloc[0,0]+tab.iloc[1,1])/ len(y_true)
print(score) #0.8

# 차트에서 한글 지원 
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

#heatmap
sn.heatmap(data=tab, annot=True) # annot=True: box에 빈도수 추가
acc_score=f'Accuracy Score:{score}'
plt.title(acc_score,size=18)
plt.show()



















