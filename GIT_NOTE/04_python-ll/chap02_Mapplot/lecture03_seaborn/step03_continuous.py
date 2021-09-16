# -*- coding: utf-8 -*-
"""
step03_continuous.py

-연속형 변수 시각화:hist, displot, scatterplot
"""
import matplotlib.pyplot as plt
import seaborn as sn

#dataset load
tips=sn.load_dataset('tips')
iris=sn.load_dataset('iris')
iris.columns #(['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'],dtype='object')

#1. hist
x=iris.sepal_length
sn.hist(x) # AttributeError: module 'seaborn' has no attribute 'hist' -> sn 은 hist 함수 없음 대신 displot 이라는 함수 있다.

#대안
sn.distplot(x, hist=True, kde=False) # hist 만
plt.show()

#distplot : 히스토그램+밀도분포곡선
sn.distplot(x, hist=True, kde=True) # hit and 확률 분포곡선 
plt.show()


# 2.산점도 행렬
#sn.pairplot(data=DF,hue='집단변수',kind='scatter')
sn.pairplot(data=iris,hue='species',kind='scatter')
plt.show()

#3. 산점도 -1차:연속형+연속형 
sn.scatterplot(x='sepal_length',y='petal_length', data=iris)
plt.show()


#3. 산점도 -2차:연속형+연속형 +범주형(hue) #변수와의 관꼐를 색깔로
sn.scatterplot(x='sepal_length',y='petal_length', hue='species', data=iris)
plt.show()


#4. 산점도 -3차:연속형+연속형 +범주형(size)#변수와의 관꼐를 점 크기로
sn.scatterplot(x='total_bill',y='tip', size='size',sizes=(10,200), data=tips)
plt.show()


#5. boxplot: 요약통계량: 연속형 + 범주형 + 범주형
sn.boxplot(x='day' ,y='total_bill' ,hue='sex' , data=tips)
plt.show()
















