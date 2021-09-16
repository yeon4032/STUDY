# -*- coding: utf-8 -*-
'''
문3) seaborn의  titanic 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기
  <단계2> 'survived' 칼럼을 집단변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도행렬 시각화
  <단계3> 산점도행렬의 시각화 결과 해설하기              

문4) seaborn의 tips 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
   <단계1> 'total_bill','tip','sex','size' 칼럼으로 서브셋 만들기 
   <단계2> 성별(sex) 칼럼을 집단변수로 하여 total_bill, tip, size 칼럼 간의 산점도행렬 시각화 
   <단계3> 산점도행렬의 시각화 결과 해설하기 
'''

import matplotlib.pyplot as plt
import seaborn as sn


# 문3) seaborn의  titanic 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
titanic = sn.load_dataset('titanic')
print(titanic.info())

#  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기 
df = titanic[['survived','pclass', 'age','fare']]

# <단계2> 'survived' 칼럼을 집단변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도행렬 시각화
sn.pairplot(data=df,hue='survived',kind='scatter')
plt.show()

# <단계3> 산점도행렬의 시각화 결과 해설하기



# 문4) seaborn의 tips 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
tips = sn.load_dataset('tips')
print(tips.info())

# <단계1> 'total_bill','tip','sex','size' 칼럼으로 서브셋 만들기
df1 = tips[['total_bill','tip','sex','size']]

# <단계2> 성별(sex) 칼럼을 집단변수로 산점도행렬 시각화 
sn.pairplot(data=df1,hue='sex',kind='scatter')
plt.show()

# <단계3> 산점도행렬의 시각화 결과 해설하기




