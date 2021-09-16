# -*- coding: utf-8 -*-
"""
step03_word_embedding_LSTM.py

    - word Embedding + LSTM 
    - Embedding + DNN vs Embedding + LSTM
lecture01> step04_word_embedding.py 참고
"""

# texts 처리
import tensorflow as tf
import pandas as pd # CSV file
import numpy as np # list -> numpy
import string # texts 전처리
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences  # [추가] 패딩

import time
# DNN model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,LSTM # LSTM[추가] & Flatten[제외] [추가]

# seed 값 지정
tf.random.set_seed(123)
np.random.seed(123)

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

voc_size = len(words) + 1 # 전체 단어수 + 8926

'''
삭제
# 4. Sparse matrix: [docs, terms]
x_data = tokenizer.texts_to_matrix(texts=texts, mode='tfidf')
x_data.shape # (5574, 4000) :num_words = 4000 적용시    
'''

# 4. sequence(정수 색인)
seq_result = tokenizer.texts_to_sequences(texts)
print(seq_result)

lens = [len(sent) for sent in seq_result]
print(lens)

maxlen=max(lens)
maxlen #183

# 5. padding : maxlen 기준으로 단어 길이 맞춤
x_data=pad_sequences(seq_result, maxlen=maxlen)
x_data.shape # (5574, 183) - (문장, 단어길이)

# 6. train/test split :80% vs 20%
x_train,x_val,y_train, y_val = train_test_split(
    x_data, label, test_size= 20)
type(y_train)# list
type(x_train)# numpy.ndarray


# 7. DNN model
model = Sequential() # keras model 생성

#  8. Embedding layer : 1 층
model.add(Embedding(input_dim=voc_size, output_dim=32, input_length=maxlen)) # 1층
'''
input_dim : 전체단어수 + 1
output_dim: 임베딩 벡트 차원(32~128)
input_length : 1 문장을 구성하는 단어 길이
'''
# [수정]2d->1d
# model.add(Flatten()) -LSTM 에 Flatten 기능이 포함 되어 있다.

# [추가] 9. 순환신경망(RNN layer) 추가
model.add(LSTM(units=32, activation='tanh')) # 2 층

# 10. hidden layer1: w[32, 32]
model.add(Dense(units=32, activation='relu')) # 3 층

# 11. output layer : [32, 1]
model.add(Dense(units=1, activation='sigmoid')) # 4층

model.summary()
'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, 183, 32)           285632    
_________________________________________________________________
lstm (LSTM)                  (None, 32)                8320      
_________________________________________________________________
dense (Dense)                (None, 32)                1056      
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 33        
=================================================================
'''
# 12. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='rmsprop', # [수정] 순환신경망: rmsprop
              loss = 'binary_crossentropy', # y: one hot encoding 
              metrics=['accuracy'])

start = time.time()
# 13. model training : train(105) vs val(45)
model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=10, # 반복학습
          batch_size=512,
          verbose=1, # 출력여부
          validation_data=(x_val, y_val)) # 검증셋

# 14. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)

end=time.time()- start
print('소요시간:',end)
'''
==============================
model evalution
1/1 [==============================] - 0s 2ms/step - loss: 0.0086 - accuracy: 1.0000
소요시간: 48.5825514793396
'''

