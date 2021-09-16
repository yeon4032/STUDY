# -*- coding: utf-8 -*-
"""
lecture01_vextorizing_encoding

1. 택스트 벡터화
 - 텍스트 -> 숫자형 벡터 변환
 - 딥러닝 모델에서 텍스트 처리를 위한 전처리

2. 작업 절차
    단계1 : 토큰(token) 생성: 텍스트 -> 단어(문자) 추출
    단계2 : 정수 인덱스 : 토큰 -> 정수 인덱스(고유슛자)
    단계3 : 인코딩(encoding) : 딥러닝 모델에 공급할 숫자형 벡터

3. 인코딩 : one-hot encoding, word embedding
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

# 2. 정수 인덱스 -> 정수 인덱스(단어 순서 인덱스)
seq_vector = tokenizer.texts_to_sequences(texts)
print(seq_vector)
# [[1, 2, 3, 4, 1, 5], [1, 2, 6, 7, 8]]

# 3. 패딩(padding): 정수 인덱스 길이 맞춤 (encoding 작업 오류 피하기 위해)
padding = pad_sequences(seq_vector)
print(padding)
#[[1 2 3 4 1 5] - doc1
#[0 1 2 6 7 8]] - doc2

# 4. 인코딩 : one-hot encoding(2진수)
one_hot = to_categorical(padding)
print(one_hot)
'''
[[[0. 1. 0. 0. 0. 0. 0. 0. 0.] - the
  [0. 0. 1. 0. 0. 0. 0. 0. 0.] - dog
  [0. 0. 0. 1. 0. 0. 0. 0. 0.] - sat
  [0. 0. 0. 0. 1. 0. 0. 0. 0.] - on
  [0. 1. 0. 0. 0. 0. 0. 0. 0.] 
  [0. 0. 0. 0. 0. 1. 0. 0. 0.]]

 [[1. 0. 0. 0. 0. 0. 0. 0. 0.] - padding
  [0. 1. 0. 0. 0. 0. 0. 0. 0.] - the
  [0. 0. 1. 0. 0. 0. 0. 0. 0.] 
  [0. 0. 0. 0. 0. 0. 1. 0. 0.]
  [0. 0. 0. 0. 0. 0. 0. 1. 0.]
  [0. 0. 0. 0. 0. 0. 0. 0. 1.]]] - poodle
'''
one_hot.shape # (2, 6, 9) - (docs, words, total_words)
'''
docs: 전체 문서수
words: 문서에 포함된 최대 단어수 (각각위 문장은 6개의 단어로 되어있다.)
total_words: 전체 단어수(중복x) +1(padding 에서 생긴 0 때문에)
'''
