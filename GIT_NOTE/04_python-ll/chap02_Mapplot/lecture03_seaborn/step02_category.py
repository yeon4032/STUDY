# -*- coding: utf-8 -*-
"""
step02_category.py

Object vs Category
 - 공통점: 자료형이 모두 문자열
 - object:셀수 없는 문자열 - 문자순서 정렬
 - category: 셀수 있는 문자열 - level 순서(숫자 배열 순서) 정렬
"""

import matplotlib.pyplot as plt
import seaborn as sn

#1. object vs category

#dataset load
tips = sn.load_dataset('tips')
print(tips.info())
titanic=sn.load_dataset('titanic')

print(titanic.info())

#subset 만들기
df = titanic[['survived','age','class','who']]
df.info()
'''
 0   survived  891 non-null    int64   
 1   age       714 non-null    float64 
 2   class     891 non-null    category
 3   who       891 non-null    object  
'''

df.head()
'''
   survived   age  class    who
0         0  22.0  Third    man
1         1  38.0  First  woman
2         1  26.0  Third  woman
3         1  35.0  First  woman
4         0  35.0  Third    man
'''

# category형 정렬: level 순서(숫자 배열 순서)
df.sort_values(by='class') #category 오름차순 
#First> Second> Third 


#object형 정렬:문자 순서
df.sort_values(by='who')  #object 오름차순
# child> man> woman ->알파벳순


#objext -> category 자료형 변경
df['who_new']=df['who'].astype('category')
df.info()


#level 순서 변경
df['who_new']=df['who_new'].cat.set_categories(['man','woman','child'])
df.sort_values(by='who_new')
# man > woman > child


# 2. 범주형 자료 시각화
#1) 배경 스타일
sn.set_style(style='darkgrid')

#2) category형 자료 시각화
sn.countplot(x='smoker',data=tips) # 2개 범주
plt.title('smoker of tips')
plt.show()


sn.countplot(x='class',data=titanic) # 3개 범주
plt.title('class of titanic')
plt.show()



sn.countplot(x='day',data=tips) # 4개 범주
plt.title('day of tips')
plt.show()


