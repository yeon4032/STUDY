# -*- coding: utf-8 -*-
"""
step04_word_embedding_LSTM_imdb.py

IMDB Movie Review Sentiment Analysis
x_data: 25000 개 영화 review 텍스트 -> 단어 정수 인덱스
y_data: review 에 대한 긍정(1), 부정(0) label
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

from tensorflow.keras.datasets.imdb import load_data # [추가] dataset

# DNN model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,LSTM # LSTM[추가] & Flatten[제외] [추가]

# seed 값 지정
tf.random.set_seed(123)
np.random.seed(123)

num_words=10000 # 주요단어 10000개 사용
maxlen=200 # 문장을 구성하는 단어 길이

# 1. dataset load
(x_train, y_train), (x_test, y_test)=load_data(num_words=10000)
x_train.shape #(25000,)
y_train.shape #(25000,)
x_train[0] # texts - 정수 인덱스
y_train[0] # 1 - 긍정

x_test.shape #(25000,)
y_test.shape #(25000,)

len(x_train[0])  # 218
len(x_train[1])  # 189
# 단어의 길이가 다르면 인코딩시 무제가된다.
# max len 찾아서 embedding 해야한다. 

# 2. 전처리,토큰 생성, 정수 인텍스 생략 

# 3. padding: 단어길이 맞춤 -> maxlen 적용
x_train = pad_sequences(x_train,maxlen=maxlen) # 단어 길이 = 200
x_test = pad_sequences(x_test,maxlen=maxlen) # 단어 길이 = 200
x_train.shape # (25000, 200)
'''
200개 이상: 짤림
200개 이하: 채움 (0 padding)
'''

# 4. encoding : word embedding 
model = Sequential() # keras model 생성

#Embedding layer : 인코딩 수행
model.add(Embedding(input_dim=num_words, output_dim=32, input_length=maxlen)) # 1층
'''
input_dim : 전체단어수 + 1
output_dim: 임베딩 벡트 차원(32~128)
input_length : 1 문장을 구성하는 단어 길이
'''
2**32

# 5. 순환신경망(RNN layer) 추가
model.add(LSTM(units=32, activation='tanh')) # 2 층

# hidden layer1: w[32, 32]
model.add(Dense(units=32, activation='relu')) # 3 층

# output layer : [32, 1]
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


# 13. model training : train(105) vs val(45)
model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=10, # 반복학습
          batch_size=512,
          verbose=1, # 출력여부
          validation_data=(x_test, y_test)) # 검증셋

# 14. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_test, y=y_test)
