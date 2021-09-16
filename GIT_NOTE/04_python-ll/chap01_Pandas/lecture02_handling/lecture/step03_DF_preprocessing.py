# -*- coding: utf-8 -*-
"""
step03_DF_preprocessing.py

 - 네이버 영화 리뷰 데이터 참조 
 - 영화 리뷰 텍스트 전처리 
   -> 동일한 리뷰 중복제거, 불용어 처리, 결측치 처리
"""

import pandas as pd 
import os

os.chdir('C:/ITWILL/4_python-ll/data')

# 1. file read
'''
pd.read_csv() : 콤마 구분자 
pd.read_table() : 특수문자(\t, :, ;, 공백) 구분자  
'''
review_df = pd.read_table('naver_movie_review.txt')
print(review_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 35237 entries, 0 to 35236
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   id      35237 non-null  int64   - 사용자 구분자 
 1   review  35233 non-null  object  - 감상평(한글) 
 2   label   35237 non-null  int64   - 긍정(1), 부정(0)
'''

# 2. dataset 특징 확인 
review_df.head()
review_df.tail()

# 칼럼 유일값/빈도수 확인 
review_df['id'].nunique() # 개수 : 35237
review_df['label'].unique() # 내용 : [1, 0]


# label 빈도수 
review_df['label'].value_counts()
'''
1    17751
0    17486
'''
review_df.value_counts()
# review 중복 확인 
review_df['review'].nunique() # 개수 
# 34694

35233 - 34694 # 539 중복 확인 

# 중복 여부 빈도수 
review_df['review'].duplicated().value_counts()
'''
False    34695
True       542
'''
# review_df.duplicated().value_counts() <-이러면 어쩌나용?

# 3. dataset 전처리 

# 1) 전처리1 : 중복제거 
review_df.drop_duplicates(subset='review', inplace=True)
'''
subset='칼럼' : 해당 칼럼으로 중복 제거 -> subset 생성 
inplace=True : 현재 객체 반영 
inplace=False : 새로운 객체 반영(변수 지정)
'''
review_df.shape # (34695, 3) 

# 2) 전처리2 : 불용어 처리(영문, 숫자, 특수문자 등 제거)
review_df['review'][:10] # review 10개 확인 

# 파생변수 
review_df['review2'] = review_df['review'].str.replace("[^가-힣|' ']","")
review_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 34695 entries, 0 to 35236
---  ------   --------------  ----- 
 0   id       34695 non-null  int64 
 1   review   34694 non-null  object  -> 원본 
 2   label    34695 non-null  int64 
 3   review2  34694 non-null  object  -> 파생변수 
'''

# 정제 전 vs 정제 후 
review_df['review'][:10] # 정제 전
review_df['review2'][:10] # 정제 후 


# 3) 전처리3 : 결측치 처리 
review_df.isnull() # True/False

import numpy as np  # np.nan

# null('') -> NaN 처리 
review_df['review2'].replace('', np.nan, inplace=True)
'''
np.nan : null -> 결측치 처리 
inplace=True : 결과를 현재 객체 반영 
'''
#불용어 처리 반영
review_df['review2'].isnull()

# 결측치 제거 
new_review = review_df.dropna() # 행 제거 

# 결측치 제거 
new_review.isnull() # True/False

new_review.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 34525 entries, 0 to 35236
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object
'''

34695 - 34525 # 170

