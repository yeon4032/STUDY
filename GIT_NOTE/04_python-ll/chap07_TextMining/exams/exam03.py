# -*- coding: utf-8 -*-
"""
문) text_data.txt 파일의 텍스트를 대상으로 다음 <출력 결과>와 같이 단계별로 
    희소행렬을 만드시오.
    
 <출력 결과> 
    mining  text  개발  기법  기술  데이터  분석  시작  전문가  직업  초반  형태소
0       0     0   0   0   0    1   2   1    0   0   0    1
1       1     1   1   1   1    1   1   0    1   1   1    0
"""

import string # text 전처리
from sklearn.feature_extraction.text import CountVectorizer# 단어생성
from konlpy.tag import Okt #형태소 분석 -> 문장,단어 추출

okt = Okt() # object 

# 1. text file red
path = 'C:\\ITWILL\\4_python-ll\\workspace\\chap07_TextMining\\data'
file = open(path + '/text_data.txt', mode='r', encoding='utf=8')

texts = file.readlines()
len(texts) #2

print('texts 전처리 전')
print(texts)


# 2. text 전처리 : 숫자, 특수문자, 공백 
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


texts=text_prepro(texts)
print('전처리 후')
print(texts)

'''
'형태소 분석을 시작합니다 나는 데이터 분석을 '
형태소 분석 시작 나 데이터 분석: 단어 
'''


# 3. 형태소 분석 : 한글 명사 + 영문 단어 '

#1) 문장 추출
sents = [okt.normalize(sent) for sent in texts]
print(sents)

#2) 단어: 한글 명사 + 영문 단어
sentences=[ ] # 문장 저장 : 단에 백터 -> 문장
for sent in sents:
    ex_pos = okt.pos(sent) # {'형태소':'품사'}
    
    sentence=""
    for word, wclass in ex_pos: # ('형태소' : '품사')
        if wclass=='Noun' or wclass=='Alpha':
            word = word + " "
            sentence += word
    sentences.append(sentence)

print(sentences)


# 4. 희소행렬 : TF 가중치 이용  
cv=CountVectorizer() #단어 생성기 (TF방식)
sp_mat=cv.fit_transform(sentences)
print(sp_mat)
sp_mat_arr=sp_mat.toarray()
print(sp_mat_arr)
'''
[[0 0 0 0 0 1 2 1 0 0 0 1]
 [1 1 1 1 1 1 1 0 1 1 1 0]]
'''


# 5. 희소행렬 -> DataFrame 변환 
words=cv.get_feature_names()

import pandas as pd

df=pd.DataFrame(sp_mat_arr,columns = words)
print(df)
'''
   mining  text  개발  기법  기술  데이터  분석  시작  전문가  직업  초반  형태소
0       0     0   0   0   0    1   2   1    0   0   0    1
1       1     1   1   1   1    1   1   0    1   1   1    0
'''




