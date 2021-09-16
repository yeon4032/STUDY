# -*- coding: utf-8 -*-
"""
step02_Tfidf_sparse_matrix.py

sparse_matrix 순서
1. csv file 가져오기
2. texts,target 전처리
3. max features
4. sparse matrix
"""

import pandas as pd #csv file
from sklearn.feature_extraction.text import CountVectorizer # spare matrix
import string # texts 전처리

#1. csv file 가져오기
path= "C:\\ITWILL\\4_python-ll\\workspace\\chap07_TextMining\\data"
spam_data=pd.read_csv(path+'/temp_spam_data.csv',header=None,encoding='utf-8')

print(spam_data.info())
'''
 0   0       5 non-null      object
 1   1       5 non-null      object
'''
print(spam_data)
'''
      0                        1
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동
'''

# 2. texts,target 전처리

#1) target 전처리: dummy 변수 생성
target=spam_data[0]
target # ham=0, spam=1
target=[1 if t=='spam' else 0 for t in target]
print(target) # [0, 1, 0, 1, 0]

texts=spam_data[1]

#2) text 전처리: 공백, 특수문자, 숫자
texts =spam_data[1]

print('전처리 전')
print(texts)
'''
0      우리나라    대한민국, 우리나라 만세
1        비아그라 500GRAM 정력 최고!
2                 나는 대한민국 사람
3    보험료 15000원에 평생 보장 마감 임박
4                     나는 홍길동
'''
# text 전처리 함수
def text_prepro(texts): # 문단(sentences)
    # Lower case: 문단-> 문장 -> 영문 소문자로 변경
    texts = [x.lower() for x in texts]
    # Remove punctuation: 문단-> 문장-> 음절추출(for c in x) -> 필터링 문장부호(if c not in string.punctuation)-> join 을 이용해서 다시 문장으로
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers: 문단-> 문장-> 음절-> 필터링-> join 통해 문장
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace: 문단 -> 문장 -> 공백제거
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts=text_prepro(texts)
print('전처리 후')
print(texts)
'''
['우리나라 대한민국 우리나라 만세', '비아그라 gram 정력 최고', '나는 대한민국 사람', 
 '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 3. max features : 희소행렬 열 수(word size)
obj=CountVectorizer()
fit = obj.fit(texts)
voca=fit.vocabulary_ # 단어 사전
print(voca)
'''
{'우리나라': 9, '대한민국': 2, '만세': 4, '비아그라': 7, 'gram': 0,
 '정력': 12, '최고': 13, '나는': 1, '사람': 8, '보험료': 6, '원에': 10,
 '평생': 14, '보장': 5, '마감': 3, '임박': 11, '홍길동': 15}
'''
type(voca) #16

max_features = len(voca) # 전체 단어수
'''
max_feature=len(voca) 전체 단어를 이요해서 희소행렬
max_feature=10: 중요 단어 10개를 이용해서 희소행렬 만들기
'''

# 4. sparse matrix : max_feature 지정
obj2=CountVectorizer(max_features=max_features)

# 희소행렬
sp_mat = obj2. fit_transform(texts)
print(sp_mat)
'''
  (0, 9)	2
  (0, 2)	1
  (0, 4)	1
  (1, 7)	1
  (1, 0)	1
  (1, 12)	1
  (1, 13)	1
  (2, 2)	1
  (2, 1)	1
  (2, 8)	1
  (3, 6)	1
  (3, 10)	1
  (3, 14)	1
  (3, 5)	1
  (3, 3)	1
  (3, 11)	1
  (4, 1)	1
  (4, 15)	1
'''

# numpy array 변환
sp_mat_arr = sp_mat.toarray()
print(sp_mat_arr)
'''
[[0 0 1 0 1 0 0 0 0 2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0]
 [0 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 1 0 1 1 0 0 0 1 1 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1]]
'''
sp_mat_arr.shape # TF방식의 희소행렬:(5, 16)

# numpy-> DF 변환
words=obj.get_feature_names() # 단어 이름 추출
words

df=pd.DataFrame(sp_mat_arr,columns=words)
df























