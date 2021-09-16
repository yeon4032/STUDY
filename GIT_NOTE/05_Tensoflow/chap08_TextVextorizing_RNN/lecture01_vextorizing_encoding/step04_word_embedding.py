# -*- coding: utf-8 -*-
"""
step03_word_embedding.py

 -word embedding(인코딩) + DNN model

1. encoding 유형
 1) 희소행렬 : 
    texts -> 희소행렬 -> DNN model(label 분류)
 2) 단어 임베딩 : 
    texts -> [sequence(정수 색인) -> 패딩 -> Embedding(사상)] -> DNN model(label)

2. Embedding(input_dim, output_dim, input_length)
 1)input_dim: 전체 단어수 + 1
 2)output_dim: embedding 층에서 출력된느 vector 크기 
 3)input_length : 문장을 구성하는 단어 길이(padding,과 maxlength 에 의해 결정) 
    
step03_features_classifier.py 참고
"""

# texts 처리
import pandas as pd # CSV file
import numpy as np # list -> numpy
import string # texts 전처리
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences  # [추가] 패딩

import time
# DNN model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,Flatten # [추가]

# 1. csv file load
path='C:\\ITWILL\\5_Tensoflow\\workspace\\chap08_TextVextorizing_RNN\\data'
spam_data = pd.read_csv(path + '/temp_spam_data2.csv', header=None)

spam_data.info()
'''
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object -label (hame/spam)
 1   1       5574 non-null   object -texts
'''

label = spam_data[0]
texts = spam_data[1]

print(label.value_counts())
'''
ham     4827
spam     747
Name: 0, dtype: int64
'''

# 2. texts와 label 전처리

# 1) label 전처리
label =[1 if lab=='spam' else 0 for lab in label]
label[:10] # [0, 0, 1, 0, 0, 1, 0, 0, 1, 1]

# list -> numpy
label=np.array(label)

# 2) texts 전처리
# texts 전처리
def text_prepro(texts):   # text _sample.txt 참고
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

# 함수 호출
text_prepro=text_prepro(texts)
print(text_prepro)


# 3. num_words = 4000 제한
tokenizer = Tokenizer(num_words = 4000 ) # 2차 : 4000 개 단어 이용

tokenizer.fit_on_texts(texts=texts) # 텍스트 반영 -> token 생성
words = tokenizer.index_word # 단어 반환
print(words)
print('전체 단어수 =',len(words)) #  전체 단어수 = 8925

voc_size = len(words) + 1 # [추가] 전체 단어수 + 8926

'''
삭제
# 4. Sparse matrix: [docs, terms]
x_data = tokenizer.texts_to_matrix(texts=texts, mode='tfidf')
x_data.shape # (5574, 4000) :num_words = 4000 적용시    
'''

# 4. [추가]sequence(정수 색인)
seq_result = tokenizer.texts_to_sequences(texts)
print(seq_result)

lens = [len(sent) for sent in seq_result]
print(lens)

maxlen=max(lens)
maxlen #183

#[추가] 5. padding : maxlen 기준으로 단어 길이 맞춤
x_data=pad_sequences(seq_result, maxlen=maxlen)
x_data.shape # (5574, 183) - (문장, 단어길이)

# 6. train/test split :80% vs 20%
x_train,x_val,y_train, y_val = train_test_split(
    x_data, label, test_size= 20)
type(y_train)# list
type(x_train)# numpy.ndarray


# 7. DNN model
model = Sequential() # keras model 생성



# [추가] 8. Embedding layer
model.add(Embedding(input_dim=voc_size, output_dim=32, input_length=maxlen)) # 1층
'''
input_dim : 전체단어수 + 1
output_dim: 임베딩 벡트 차원(32~128)
input_length : 1 문장을 구성하는 단어 길이
'''
# [추가]2d->1d
model.add(Flatten())

# hidden layer1: w[32, 32]
model.add(Dense(units=32, activation='relu')) # 2 층

# output layer : [32, 1]
model.add(Dense(units=1, activation='sigmoid')) # 3층

model.summary()
'''
_______________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 64)                552384   =(8630*64)+64 
_________________________________________________________________
dense_1 (Dense)              (None, 32)                2080      =(64*32)+32
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 33        =(32*1)+1
=================================================================
'''
# 7. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='adam',
              loss = 'binary_crossentropy', # y: one hot encoding 
              metrics=['accuracy'])

start = time.time()
# 8. model training : train(105) vs val(45)
model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=10, # 반복학습[수정]
          batch_size=512,
          verbose=1, # 출력여부
          validation_data=(x_val, y_val)) # 검증셋

# 9. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)

end=time.time()- start
print('소요시간:',end)
'''
model evalution
1/1 [==============================] - 
0s 996us/step - loss: 0.2086 - accuracy: 1.0000
소요시간: 5.44587779045105
'''