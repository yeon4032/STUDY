# -*- coding: utf-8 -*-
"""
step01_Tfidfvectorizer.py

TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기[word tokenizer] : 문장(sentences) -> 단어(word) 생성
  2. 단어 사전[word dictionary] : (word, 고유수치)
  3. 희소행렬[sparse matrix] : 단어 출현 비율에 의해서 가중치 적용[type-TF, TFiDF]
    1] TF : 가중치 설정 - 단어 출현 빈도수
    2] TFiDF : 가중치 설정 - 단어 출현 빈도수 x 문서 출현빈도수의 역수            
    - tf-idf(d,t) = tf(d,t) x idf(t) [d(document), t(term)]
    - tf(d,t) : term frequency - 특정 단어 빈도수 
    - idf(t) : inverse document frequency - 특정 단어가 들어 있는 문서 출현빈도수의 역수
       -> TFiDF = tf(d, t) x log( n/df(t) ) : 문서 출현빈도수의 역수(n/df(t))
"""

from sklearn.feature_extraction.text import TfidfVectorizer


#1. 단어 생성기

#문장
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."]

sentences

#1. 단어 생성기
obj=TfidfVectorizer() # 생성자
obj

# 2.단어 사전
fit = obj.fit(sentences) # 문장 적용
voca=fit.vocabulary_
print(voca) #Dict 형 {'word': 고유숫자} - 고유숫자: 영문 오름차순
'''
{'mr': 14, 'green': 5, 'killed': 11, 'colonel': 2, 'mustard': 15, 'in': 9, 'the': 24, 'study': 23, 'with': 30, 'candlestick': 1, 'is': 10, 'not': 17, 'very': 25, 'nice': 16, 'fellow': 3, 'professor': 21, 'plum': 20, 'has': 6, 'plant': 19, 'his': 8, 'miss': 13, 'scarlett': 22, 'watered': 27, 'while': 29, 'he': 7, 'was': 26, 'away': 0, 'from': 4, 'office': 18, 'last': 12, 'week': 28}
'''
len(voca) # 31

#3. 희소행렬[sparse matrix]
sp_mat=obj.fit_transform(sentences)
print(sp_mat)
'''
  (Doc,단어)  가중치(weight)=TF*IDF
  (0, 3)	0.2205828828763741
  (0, 16)	0.2205828828763741
  (0, 25)	0.2205828828763741
          :
  (2, 20)	0.2057548299742193
  (2, 21)	0.2057548299742193
  (2, 5)	0.15978698032384395
'''
type(sp_mat) #scipy.sparse.csr.csr_matrix

# scipy -> numpy 희소행렬 변경
sp_mat_arr = sp_mat.toarray()
print(sp_mat_arr)
sp_mat_arr.shape # (3, 31)










