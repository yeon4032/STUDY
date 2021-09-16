# -*- coding: utf-8 -*-
"""
step02_DF_reshape.py

DataFrame 모양 변경(reshape)
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_Python-II/data')
buy = pd.read_csv('buy_data.csv')

print(buy.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
'''

# 1. 모양(shape) 확인 
buy.shape # (22, 3) : 2차원 
buy.head()
'''
       Date  Customer_ID  Buy
0  20150101            1    3
1  20150101            2    4
2  20150102            1    2
3  20150101            2    3
4  20150101            1    2
'''

# 2. 2차원(wide) -> 1차원(long) 구조 변경 
buy_long = buy.stack()
buy_long.shape # (66,) : 1차원(22*3=66)
buy_long

# 3. 1차원(long) -> 2차원(wide)
buy_wide = buy_long.unstack()
buy_wide.shape  # (22, 3)

# 4. 전치행렬 : 행축 <-> 열축 
buy_tran = buy.T
buy_tran.shape # (3, 22)

# 5. 중복 행 제거 
buy.duplicated() # 중복 여부 확인

buy2 = buy.drop_duplicates() # 중복 제거 
buy2.duplicated()
buy2.shape # (20, 3)

# 6. 특정 칼럼을 index 지정 
buy.columns # ['Date', 'Customer_ID', 'Buy']

buy_new = buy.set_index('Date')
buy_new.shape # (22, 2)

# 색인 확인 
buy_new.index
'''
[20150101, 20150101, 20150102, 20150101, 20150101, 20150103,
            20150102, 20150102, 20150103, 20150103, 20150103, 20150107,
            20150107, 20150103, 20150104, 20150104, 20150104, 20150105,
            20150106, 20150106, 20150107, 20150107]
'''
buy_new

# 날짜 기준 구매정보 확인 
buy_new.loc[20150101]
buy_new.loc[20150104]

# Data type 
'''
buy_new.loc[2015] -> 년도별 조회 
buy_new.loc[201504] -> 월별 조회 
'''






