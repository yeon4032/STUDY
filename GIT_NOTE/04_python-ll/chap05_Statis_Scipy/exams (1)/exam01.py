# -*- coding: utf-8 -*-
"""
문01) 이항검정 : 95% 신뢰수준에서 토요일(Sat)에 오는 여자 손님 중 비흡연자가 흡연자 보다 많다고 할 수 있는가?

 귀무가설 : 비흡연자와 흡연자의 비율은 차이가 없다.(P=0.5)
"""

from scipy import stats # 이항검정 
import pandas as pd # csv file read
import os # file path 

os.chdir('c:/ITWILL/4_Python-II/data')
tips = pd.read_csv("tips.csv")
print(tips.info())
print(tips.head())

# 1. 행사 요일 빈도수 
day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

# 2. 성별 빈도수 
gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''

# 3. Sat 기준 subset 생성 
sat_day = tips[tips['day'] == 'Sat']
print(sat_day.head())
'''
    total_bill   tip     sex smoker  day    time  size
19       20.65  3.35    Male     No  Sat  Dinner     3
20       17.92  4.08    Male     No  Sat  Dinner     2
21       20.29  2.75  Female     No  Sat  Dinner     2
22       15.77  2.23  Female     No  Sat  Dinner     2
23       39.42  7.58    Male     No  Sat  Dinner     4
'''

# 4. sat_day를 대상으로 Female 기준 subset 생성 


# 5. subset을 대상으로 smoker 기준 group 
# - 성공회수(비흡연자)와 시행회수(비흡연자+흡연자)  확인 


# 6. 이항검정(binom test) : 성공회수와 시행회수 이용 
















































from scipy import stats # 이항검정 
import pandas as pd # csv file read
import os # file path 

os.chdir('C:/ITWILL/4_python-ll/data')
tips = pd.read_csv("tips.csv")
print(tips.info())
print(tips.head())

# 1. 행사 요일 빈도수 
day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

# 2. 성별 빈도수 
gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''

# 3. Sat 기준 subset 생성 
sat_day = tips[tips['day'] == 'Sat']
print(sat_day.head())
'''
    total_bill   tip     sex smoker  day    time  size
19       20.65  3.35    Male     No  Sat  Dinner     3
20       17.92  4.08    Male     No  Sat  Dinner     2
21       20.29  2.75  Female     No  Sat  Dinner     2
22       15.77  2.23  Female     No  Sat  Dinner     2
23       39.42  7.58    Male     No  Sat  Dinner     4
'''

# 4. sat_day를 대상으로 Female 기준 subset 생성 
sat_day_female=sat_day[sat_day['sex']=='Female']
sat_day_female

# 5. subset을 대상으로 smoker 기준 group 
# - 성공회수(비흡연자)와 시행회수(비흡연자+흡연자)  확인 
grp= sat_day_female.groupby('smoker')
grp.size()
print(grp.first())
grp.head()
for g in grp:
    print(g)

'''
smoker
No     13
Yes    15
dtype: int64
'''
no_rate=13 / (13+15)
no_rate


# 6. 이항검정(binom test) : 성공회수와 시행회수 이용 
pvalue = stats.binom_test(x=13,n=28,p=0.5,alternative='two-sided')#양측검정

alpha=0.05

if pvalue >= alpha:
    print('비흡연자와 흡연자의 비율은 차이가 없다-가설 채택')
else:
    print('비흡연자와 흡연자의 비율은 차이가 있다.-가설 기각')

#비흡연자와 흡연자의 비율은 차이가 없다-가설 채택




