# -*- coding: utf-8 -*-
"""
step03_word2vec.py

1. pip install gensim
2. word2vec 개요
    - 중심단어와 주변단어 벡터 간의 연산으로 유사단어 예측
3. word2vec 유형
    1) CBOW : 주변단어 학습-> 중심단어 예측
    2) SKIP-Gram : 중심단어 -> 주변단어 예측
        ex) window=2
                my name is hong -> (my, name) (my, is), (my, hong) 이와 같은 방식으로 학습 해서 예측함
"""
from gensim.models import Word2Vec # model
import nltk
nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # sentence -> word token
from nltk.tokenize import sent_tokenize # texts -> sentence tokend
import pandas as pd # csv file

# 1. dataset load
data=pd.read_csv('C:\\ITWILL\\4_python-ll\\data/movies_metadata.csv')
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 45466 entries, 0 to 45465
Data columns (total 24 columns):
'''

# 2. 변수 선택 & 전처리
df = data[['title','overview']]
df.dropna(axis = 0)
df.info()
'''
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   title     45460 non-null  object : 영화 제목
 1   overview  44512 non-null  object : 영화 줄거리
'''

# 3. token 생성 

# 1) 문장 토큰: texts-> sentence (sent_tokenize)
texts="my name is hong. my hobby is reading"
re_sent = sent_tokenize(texts)
print(re_sent)# . 기준으로 문장 생성
#['my name is hong.', 'my hobby is reading']

#2) 단어 토큰: sentences -> word
sents = "my name is hong."
re_words = word_tokenize(sents)
print(re_words) # 스페이스 기준으로 단어 생성
#['my', 'name', 'is', 'hong', '.']


# 3) overview 단어 벡터 생성
overview = df['overview'].tolist() # 판다스 column-> list 변환 (word_tokenize를 사용하기 위해 list 변환)
overview
type(overview)
len(overview) #45466[0, 1, ~ ,44505]
overview[0]
type(overview)

result=[]
for row in overview:
    words = word_tokenize(str(row))# sentence-> words : 단어 벡터
    result.append(words) # [[단어 벡터],....[단어 벡터]]

len(result)
result[0]

# 4. word2vec
model = Word2Vec(sentences = result, window=5, 
                 min_count=1, sg=1) #sg=0 도가능
'''
sentences: 단어벡터
window : 1회 학습할 단어수
min_count: 단어 최소 빈도수 제한
sg : 0 - CBOW, 1-SKIP-Gram
'''

# 5. 유사 던어 검색
word_search_re = model.wv.most_similar(['husband'])
print('top5:', word_search_re[:5])
'''
top5: [('lover', 0.8472157716751099), 
       ('boyfriend', 0.8397032022476196), 
       ('fiancé', 0.8181553483009338), 
       ('ex-husband', 0.7856030464172363), 
       ('fiance', 0.781024694442749)]

'''

word_search_re = model.wv.most_similar(['woman'])
print('top5:', word_search_re[:5])
'''
top5: [('lady', 0.8185963034629822), 
       ('man', 0.8176683783531189), 
       ('schoolgirl', 0.8116124868392944), 
       ('countess', 0.8074464201927185), 
       ('nurse', 0.8006460070610046)]
'''


word_search_re = model.wv.most_similar(['success'])
print('top5:', word_search_re[:5])
'''
top5: [('fame', 0.819200873374939), 
       ('achieves', 0.7780908346176147), 
       ('stardom', 0.7738733291625977), 
       ('sensation', 0.7580776214599609), 
       ('commercial', 0.7549660801887512)]
'''






