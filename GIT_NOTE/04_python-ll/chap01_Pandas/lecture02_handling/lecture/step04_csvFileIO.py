# -*- coding: utf-8 -*-
"""
step04_csvFileIO.py

1. csv file read
2. read data 처리 
3. csv file write
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_python-ll/data')


# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv('student.csv', header = None)
st #      0     1    2   3

# 칼럼명 전체 수정 
st.columns = ['sno', 'name', 'height', 'weight']
st.info()

# 특정 칼럼명 수정 
col_names = list(st.columns)
col_names[1] = 'sname'

st.columns = col_names
st.info()

# 2) 칼럼명 : 특수문자(.) or 공백  -> '_'
'''
test_123
DF.test_123 (O)
DF['test 123'] (O)
'''
iris = pd.read_csv('iris.csv')

iris.info()

# 특수문자(.) -> '_'
iris.columns = iris.columns.str.replace('.', '_')
iris.info()


# 2. read data 처리
print(st)
'''
비만도 지수(bmi)
bmi = 몸무게 / 키^2
몸무게 단위 : kg
키 단위 : cm -> m
'''

175 * 0.01 # 1.75

bmi = st['weight'] / (st['height']*0.01)**2
bmi

# 파생변수 추가 
st['bmi'] = bmi

print(st)

'''
label = 정상(18~23), 비만, 저체중 
'''

label = []

for bmi in st.bmi : 
    if bmi >= 18 and bmi <= 23 :
        label.append('정상')
    elif bmi > 23 :
        label.append('비만')
    else :
        label.append('저체중')

print(label)

# 파생변수 추가 
st['label'] = label

print(st)


# 3. csv file write

st.to_csv('st_df.csv', index=None, encoding='utf-8')

st_df = pd.read_csv('st_df.csv', encoding='utf-8')
print(st_df)













