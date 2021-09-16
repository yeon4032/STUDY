# -*- coding: utf-8 -*-
"""
step02_similarity_recomm.py

영화 검색 시스템
 - 영화 키워드 -> 관련 영화 검색(추천)
"""
import pandas as pd # csv file
from sklearn.feature_extraction.text import TfidfVectorizer # 희소행렬
from sklearn.metrics.pairwise import cosine_similarity  # 유사도 계산

# 1. dataset load
data =pd.read_csv('C:\\ITWILL\\4_python-ll\\data\\movie_reviews.csv')
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object : 영화 후기
 1   title    1492 non-null   object : 영화 제목
 2   label    1492 non-null   int64  : 긍정/부정
'''

# 2. 전처리 : 결측치 행 단위 제거
data_df = data.dropna(axis = 0)
data_df.info()

# 3. Sparse matrix(DTM) : reviews 대상
obj=TfidfVectorizer(stop_words='english') # 단어생성기
#희소행렬
movie_sm = obj.fit_transform(data_df['reviews'])
movie_sm.shape #(1492, 34641) -> 1492 문장에서 34641 단어 생성

# scipy -> numpy array
type(movie_sm) # scipy.sparse.csr.csr_matrix
movie_sm_arr = movie_sm.toarray()
movie_sm_arr.shape # (1492, 34641)


title =data_df['title']
# 4. query 작성 -> DTM -> 유사도 계산 -> 영화 추천(검색)
def movie_search(query):
    #1) query 작성
    query_data = [query] # 문장 -> list 변경
    
    # 2)query DTM
    query_sm = obj.transform(query_data)
    query_sm = query_sm.toarray()
    
    # 3)유사도 계산
    sim = cosine_similarity(query_sm,movie_sm_arr) # (query, raw doc)
    print(sim.shape)
    sim=sim.reshape(1492) # 2d->1d  #내림차순 정렬하기 위해서 2차원을 1차원으로 모양을 변경했습니다.
    
    # 4) 내림차순 정렬: index 정렬
    sim_idx = sim.argsort()[::-1]
    print(sim_idx) #[1281 1304  373 ...  906  907    0]
    
    # 5) TopN=5 영화추천하기
    for idx in sim_idx[:5]:
        print(f'similarity:{sim[idx]} \n movie title:{title[idx]}')

# 함수 호출 : 영화 관련 키워드
movie_search(input('search query input:'))# action
'''
search query input:action
(1, 1492)
[1281 1304  373 ...  906  907    0]
similarity:0.20192921485638887 
 movie title:Soldier (1998)
similarity:0.1958404700223592 
 movie title:Romeo Must Die (2000)
similarity:0.18885169874338412 
 movie title:Aliens (1986)
similarity:0.18489066174805405 
 movie title:Speed 2: Cruise Control (1997)
similarity:0.16658803590038168 
 movie title:Total Recall (1990)
 
 
 search query input:drama
(1, 1492)
[ 671 1359 1223 ...  981  982    0]
similarity:0.1931737274266525 
 movie title:Apollo 13 (1995)
similarity:0.11796112357272329 
 movie title:Double Jeopardy (1999)
similarity:0.11374906390472769 
 movie title:Practical Magic (1998)
similarity:0.11037479275255738 
 movie title:Civil Action, A (1998)
similarity:0.09607905933279662 
 movie title:Truman Show, The (1998)
 
'''













































