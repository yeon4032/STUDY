# -*- coding: utf-8 -*-
"""
step01_DF_merge

1. DataFrame 병합(merge) - join 
   ex) DF1(id) + DF2(id) = DF3
2. DataFrame 결합(concat)
   ex) DF1 + DF2 = DF3
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_Python-II/data')
wdbc = pd.read_csv('wdbc_data.csv')
print(wdbc.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 569 non-null    int64  
 1   diagnosis          569 non-null    object 
'''

# 1. DataFrame 병합(merge)
# - ex) DF1(id) + DF2(id) = DF3

cols = list(wdbc.columns)
cols 
DF1 = wdbc[cols[:16]] # 16(id)
DF2 = wdbc[cols[16:]] # 16(x)

DF1.shape # (569, 16)
DF2.shape # (569, 16)

# DF2에 id 칼럼 추가 
DF2['id'] = wdbc['id']
DF2.shape # (569, 17)
print(DF2.head())

# DF 병합(join) 
DF3 = pd.merge(left=DF1, right=DF2, on='id') # how = 'inner'
DF3.shape # (569, 32)


# 2. DataFrame 결합(concat)
# -  ex) DF1 + DF2 = DF3
DF1 = wdbc[cols[:16]] # 16(id)
DF2 = wdbc[cols[16:]] # 16(x)

DF4 = pd.concat(objs = [DF1, DF2], axis = 1) # axis = 1(cbind)
DF4.shape # (569, 32)

print(DF4.head())

DF5 = pd.concat(objs = [DF1, DF2], axis = 0)
DF5.shape
# 3. inner join vs outer join 
'''
inner join : 양쪽 DF 자료가 있는 경우 
outer join : 한쪽 DF 자료가 있는 경우
'''

name = ['hong', 'lee', 'park', 'kim']
age = [35, 20, 55, 35]

df1 = pd.DataFrame(data={'name':name, 'age':age})
df1


name2 = ['hong', 'lee', 'kim']
age2 = [35, 20, 35]
pay = [250, 300, 200]

df2 = pd.DataFrame(data={'name':name2, 'age':age2, 'pay':pay})
df2

# 내부 조인 : 공통칼럼(name, age)
inner = pd.merge(left=df1, right=df2, 
                 on=['name','age'], how='inner')
print(inner)
'''
   name  age  pay
0  hong   35  250
1   lee   20  300
2   kim   35  200
'''

# 내부 조인 : 공통칼럼(name)
inner = pd.merge(left=df1, right=df2, on='name', how='inner')
print(inner)
'''
   name  age_x  age_y  pay
0  hong     35     35  250
1   lee     20     20  300
2   kim     35     35  200
'''

# 외부 조인 
outer = pd.merge(left=df1, right=df2, how='outer')
print(outer)
'''
   name  age    pay
0  hong   35  250.0
1   lee   20  300.0
2  park   55    NaN -> 결측치 
3   kim   35  200.0
'''

