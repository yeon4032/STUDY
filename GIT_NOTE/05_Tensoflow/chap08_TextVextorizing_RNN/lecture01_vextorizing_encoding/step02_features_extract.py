# -*- coding: utf-8 -*-
"""
step02_features_extract.py

1. 텍스트 -> 특징(features) 추출
    -> texts-> 희소핼렬(sparse matrix): 딥러닝 모델 공급data
    -> 희소행렬 가중치 방법: binary, count,freq(비율), Tfidf(단어 출형 빈도*1/문서출현)
    
2. num_words(max features)
    - 희소행렬의 차수 지정(단어의 개수)
    ex) num_words=500: 전체 단어에서 중요단어 500개 선정

3. max length
    - 한 문장을 구성하는 최대 단어수 지정
    ex) max_length =100 : 모든 문장의 단어 100개 사용(짤림 or 채움)
"""
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences 
from tensorflow.keras.utils import to_categorical # 인코딩

# text_sample.txt 참고
texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 토근 생성기
tokenizer = Tokenizer() # number_words 생략 : 전체 단어 이용

# 1. 토큰 생성 : 전체 단어 확인
tokenizer.fit_on_texts(texts)

token=  tokenizer.word_index # 토큰 반환

print(token) # {'word':고유숫자} : 고유숫자 -> 단어 순서 index
#{'the': 1, 'dog': 2, 'sat': 3, 'on': 4, 'table': 5, 'is': 6, 'my': 7, 'poodle': 8}

print('전체 token(단어) 길이=', len(token))
# 전체 token(단어) 길이= 8

#희소 행렬: 단어 출현 여부 (가중치) -> 1과 영으로만 
binary_mat=tokenizer.texts_to_matrix(texts=texts,mode='binary')
print(binary_mat)
'''
[[0. 1. 1. 1. 1. 1. 0. 0. 0.]
 [0. 1. 1. 0. 0. 0. 1. 1. 1.]]
'''
binary_mat.shape # (2, 9) -> (docs, terms=words +1)

# 2 num_words : 희소행렬 단어 차수 제한
tokenizer = Tokenizer(num_words=6) # 5개 단어 선정(단어기링+1)
tokenizer.fit_on_texts(texts) # 텍스트 반영

help(tokenizer.texts_to_matrix)
# mode: one of "binary", "count", "tfidf", "freq".

# 3. 희소행렬: 텍스트 -> 특징 추출 
# 단어 출현 빈도(tf)
count_mat = tokenizer.texts_to_matrix(texts=texts,mode='count')
print(count_mat)
'''
[[0. 2. 1. 1. 1. 1.]  - the : 2
 [0. 1. 1. 0. 0. 0.]] - 4번째 부터 마지막 6 번째 단어는 0이다 이유는 첫번째 문장에서 4,5,6번 단어를 쓴적이 없어서 이다. 
'''
count_mat.shape # (2, 6) # 5개의 단어만 사용 <- tokenizer = Tokenizer(num_words=6)에서 단어수 제한해서 임

# 단어 비율(단어 출현빈도)
freq_mat=tokenizer.texts_to_matrix(texts=texts,mode='freq')
print(freq_mat)
'''          실제단어 
[[0.         0.33333333 0.16666667 0.16666667 0.16666667 0.16666667]
 [0.         0.5        0.5        0.         0.         0.        ]]
'''
# the 0.3333(=2/6) 
# dog 0.16666(=1/6)
# 0.5 (=1/2) <- 두번째 문장에서 (첫문장 기준으로 2번째문장에 있는단어)

freq_mat.shape # (2, 6)

#4) 단어출현비율(tf*(1/df))
tfidf_mat=tokenizer.texts_to_matrix(texts=texts,mode='tfidf')
print(tfidf_mat)
'''
[[0.         0.86490296 0.51082562 0.69314718 0.69314718 0.69314718]
 [0.         0.51082562 0.51082562 0.         0.         0.        ]]
'''
#the :08649 -> the : 0.51082562
# 단어의 출현 빈도수 증가시 중요도 떨어진다.


# 4. max length: 한 문장의 길이 제한 (고정)
seq_index = tokenizer.texts_to_sequences(texts = texts)
print(seq_index)
#[[1, 2, 3, 4, 1, 5], [1, 2]]

# list +for
lens = [len(sent) for sent in seq_index]
print(lens) #[6, 2]

maxlen = max(lens)
print(maxlen) # 6

# 패딩(padding): 정수 인덱스 길이 맞춤 ( maxlen 기준)
x_data = pad_sequences(sequences=seq_index, maxlen=maxlen)
print(x_data)
'''
[[1 2 3 4 1 5]  <- 
 [0 0 0 0 1 2]] <-
'''





matching
- 금융 분야 enginearing -> 수집 -> 
- 통신

