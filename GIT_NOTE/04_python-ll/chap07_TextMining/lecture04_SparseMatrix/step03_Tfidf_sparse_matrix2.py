# -*- coding: utf-8 -*-
"""
step03_Tfidf_sparse_matrix2.py

sparse_matrix 순서
1. csv file 가져오기 
2. texts, target 전처리 
3. max features
4. sparse matrix
5. train/test split[추가]
6. file save[추가]
"""

import string # texts 전처리 
import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # sparse matrix 

# 1. csv file 가져오기[수정] 
path = "C:\\ITWILL\\4_Python-II\\workspace\\chap07_TextMining\\data"
spam_data = pd.read_csv(path + '/temp_spam_data2.csv', 
                        header=None, encoding='utf-8')

print(spam_data.info())
'''
 0   0       5574 non-null   object
 1   1       5574 non-null   object
'''
print(spam_data.head())
'''
      0                                                  1
0   ham  Go until jurong point, crazy.. Available only ...
1   ham                      Ok lar... Joking wif u oni...
2  spam  Free entry in 2 a wkly comp to win FA Cup fina...
3   ham  U dun say so early hor... U c already then say...
4   ham  Nah I don't think he goes to usf, he lives aro...
'''

# 2. texts, target 전처리

# 1) target 전처리 : dummy변수 
target = spam_data[0]
target # ham=0, spam=1
target = [1 if t == 'spam' else 0 for t in target ] # list 반환 
print(target) # [0, 1, 0, 1, 0]

# 2) texts 전처리 : 공백, 특수문자, 숫자  
texts = spam_data[1]

print('전처리 전')
print(texts)

# texts 전처리 함수 
def text_prepro(texts): # 문단(sentences)
    # Lower case : 문단 -> 문장 -> 영문소문자 변경  
    texts = [x.lower() for x in texts]
    # Remove punctuation : 문단 -> 문장 -> 음절 -> 필터링 -> 문장  
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers : 문단 -> 문장 -> 음절 -> 필터링 -> 문장 
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace : 문단 -> 문장 -> 공백 제거 
    texts = [' '.join(x.split()) for x in texts]
    return texts


texts = text_prepro(texts)
print('전처리 후 ')
print(texts)
'''
'go until jurong point crazy available only in 
 bugis n great world la e buffet cine there got 
 amore wat', 'ok lar joking wif u oni','free entry 
 in a wkly comp to win fa cup final tkts st may text fa to to receive entry questionstd txt ratetcs apply overs'
'''

# 3. max features : 희소행렬의 열 수(word size)
obj = TfidfVectorizer() # 단어 생성기 
fit = obj.fit(texts)
voca = fit.vocabulary_
print(voca)

len(voca) # 8603

max_features = 5000 # 전체 단어수 
'''
max_features = len(voca) : 전체 단어(8603)를 이용해서 희소행렬 
max_features = 5000 : 중요단어 5,000개를 이용해서 희소행렬 
'''

# 4. sparse matrix : max features 지정 
obj2 = TfidfVectorizer(max_features = max_features,
                       stop_words='english')
'''
max_features : 사용할 단어 개수 
stop_words : 불용어 단어 제거 
'''

# 희소행렬 
sp_mat = obj2.fit_transform(texts)

print(sp_mat)
'''
  (0, 4517)	0.23028059868952055
  (0, 1286)	0.1893428233646285
  (0, 551)	0.3411906679200504
  (0, 396)	0.38553507725150876
    :
  (5572, 1485)	0.3036649798158202
  (5572, 1158)	0.20992497007997934
  (5573, 3012)	0.7912446244465056
  (5573, 4120)	0.6114997500281654  
'''

# numpy array 변환 
sp_mat_arr = sp_mat.toarray()

print(sp_mat_arr)
sp_mat_arr.shape # (5574, 5000)


# 5. train/test split[추가]
from sklearn.model_selection import train_test_split # datase split 
import numpy as np

x_train, x_test, y_train, y_test = train_test_split(
    sp_mat_arr, target, test_size=0.3)

x_train.shape # (3901, 5000)
x_test.shape # (1673, 5000)

# target -> numpy 변환 
y_train = np.array(y_train) 
y_test = np.array(y_test) 

y_train.shape # (3901,)
y_test.shape # (1673,)


# 6. file save[추가] : np.save() 
spam_train_test = (x_train, x_test, y_train, y_test)

# np.save("file", object)
np.save(path + "/spam_train_test.npy", spam_train_test)

# np.load("file", allow_pickle=True)
x_train, x_test, y_train, y_test = np.load(path + "/spam_train_test.npy", 
                                           allow_pickle=True)

x_train.shape # (3901, 5000)
x_test.shape # (1673, 5000)

y_train.shape # (3901,)
y_test.shape # (1673,)



















































