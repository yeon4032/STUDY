# -*- coding: utf-8 -*-
"""
step01_cosine_similarity.py

코사인 유사도 이용-> 유사 문장 찾기: 내용기반 추천 시스쳄
<작업 절차>
1. 대상 문서(자연어) -> DTM(문서단어행렬: 희소행렬)
2. 코사인 유사도 적용
    -> 원리: 문서를 구성하는 단어들 간의 유사도 비교

코사인 유사도(Cosine similarity)
- 두 벡터 간의 코사인 각도를 이용한 유사도(1 ,0,-1)
"""

# 희소행렬(sparse matrix)
from sklearn.feature_extraction.text import TfidfVectorizer # 단어생성기
# 코사인 유사도
from sklearn.metrics.pairwise import cosine_similarity 

# 문장(자연어)
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

print(sentences)
len(sentences)#3

# 1. 대상 문서(자연어) -> DTM(문서단어행렬: 희소행렬) 변경
obj = TfidfVectorizer() # 1)  단어 생성기

# 단어 보기
fit = obj.fit(sentences)
voca = fit.vocabulary_
print(voca) # {'word':고유숫자}
len(voca) # 31

# 2) 희소행렬 (DTM) 
sp_mat = obj.fit_transform(sentences)
print(sp_mat)
'''
  (doc, term) weight(Tfidf)
  (0, 3)	0.2205828828763741
  (0, 16)	0.2205828828763741
  (0, 25)	0.2205828828763741
  (0, 17)	0.2205828828763741
     :             :
'''


# scipy -> numpy
sp_mat_arr = sp_mat.toarray()
print(sp_mat_arr) # 단어 백터 생성
sp_mat_arr.shape # (3, 31)


# 2. 코사인 유사도 적용

#1) 검색 쿼리 생성(search query)
query=['green plant in his study'] # 검색 문장

#2) 희소행렬(DTM)
query_sp_mat = obj.transform(query) # 함수명 주의 # 
#기존 fitting된 객체(obj)를 이용하여 희소행렬로 변형했다.
#기존 3행 31열의 희소행렬에 query로 사용된 문장에서 출현한 단어들의 가중치가 적용되어서 단어벡터가 만들어집니다.

#2) scipy -> numpy
query_sp_mat_arr = query_sp_mat.toarray()
query_sp_mat_arr.shape # (1,31)
query_sp_mat_arr

#3) 코사인 유사도 계산
sim = cosine_similarity(query_sp_mat_arr,sp_mat_arr) # (query, raw docment)
'''
(1,31) vs (3,31)
'''
sim.shape # (1,3)
print(sim) # [[0.25069697 0.74327606 0.24964024]]

# 4)2d(1,3) -> 1d(3,1)
sim = sim.reshape(3)
sim.shape #(3,)
print(sim) #[0.25069697 0.74327606 0.24964024]

# 5) 내림차순 정렬: index 정렬
sim_idx=sim.argsort()[::-1]  #sorted 안씀 <- 내용 기준으로 정렬됨
print(sim_idx) # [1 0 2] 2번째 문장이 유사도 가 가장 높고 그다음은 1번째 마지막은 3번째 이다.

# 6) query와 가장 유사도가 높은 순으로 문장 검색
for idx in sim_idx:
    print(f'similarity: {sim[idx]}, \n sentences:{sentences[idx]}')
'''
similarity: 0.7432760626367734, 
 sentences:Professor Plum has a green plant in his study.
similarity: 0.25069697393300555, 
 sentences:Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.
similarity: 0.2496402361939771, 
 sentences:Miss Scarlett watered Professor Plum's green plant while he was away from his office last week.
'''

#######################################################
### Cosine Similarity 수식
#######################################################

'''
def con_sim(A, B) :
    retrun dot(A, B) / (norm(A) * norm(B))

dot(A, B) : 행렬 A,B 에 대한 행렬곱
norm(A) : 행렬 A의 벡터 크기(노름)
    -> 표기법:||A||
    -> sqrt(sum(x**2))
'''

import numpy as np

# 1. 백터 크기 계산:노름
A = np.array([[1,-2,3,-4,5]]) # 백터 A

# 1) numpy 함수 이용
norm_A = np.linalg.norm(A)
print(norm_A) # 7.416198487095663

# 2) 노름 식 이용
norm_A2 = np.sqrt((A**2).sum())
norm_A2 # 7.416198487095663

#2. Cosine 유사도
def cos_sin(A, B):
    return np.dot(A, B)/(np.linalg.norm(A)*np.linalg.norm(B))

'''
np.doc(A, B)
1.A,B 모두 행렬
2.수일치: A(열) == B(행)
'''

query_sp_mat_arr.shape # (1, 31)<-A
sp_mat_arr.shape # (3, 31) <- B

# B행렬 -> 전치행렬 : 수일치를 위해서
sp_mat_arr.T.shape # (31, 3)

con_sime_re = cos_sin(query_sp_mat_arr,sp_mat_arr.T) # (A@B.T)
print(con_sime_re) #[[0.14473997 0.42913063 0.14412986]]























