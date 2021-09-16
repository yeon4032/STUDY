# -*- coding: utf-8 -*-
"""
step03_features_classifier.py

 - 희소행렬 + DNN model
 < 작업 절차>
 1. csv file load
 2. texts와 label 전처리
 3. num_words = 4000 제한
 4. Sparse matrix: features
 5. train/test split
 6. DNN model 
"""

# texts 처리
import pandas as pd # CSV file
import numpy as np # list -> numpy
import string # texts 전처리
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences  #패딩
from tensorflow.keras.utils import to_categorical # 인코딩
import time
# DNN model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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
#tokenizer = Tokenizer() # 1차 : 전체 단어 이용
tokenizer = Tokenizer(num_words = 4000 ) # 2차 : 4000 개 단어 이용

tokenizer.fit_on_texts(texts=texts) # 텍스트 반영 -> token 생성
words = tokenizer.index_word # 단어 반환
print(words)
print('전체 단어수 =',len(words)) #  전체 단어수 = 8925


# 4. Sparse matrix: [docs, terms]
x_data = tokenizer.texts_to_matrix(texts=texts, mode='tfidf')
x_data.shape # (5574, 8926) 8630 = 전체단어길이 + 1      # 1차
             # (5574, 4000) :num_words = 4000 적용시    # 2차

# 5. train/test split :80% vs 20%
x_train,x_val,y_train, y_val = train_test_split(
    x_data, label, test_size= 20)
type(y_train)# list
type(x_train)# numpy.ndarray


# 6. DNN model
model = Sequential() # keras model 생성

#input_shape=(8926,) # 1 차
input_shape=(4000,) # 2차

# hidden layer1: w[8630, 64]
model.add(Dense(units=64, input_shape=input_shape, activation='relu')) # 1 층

# hidden layer2: w[64, 32]
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
          epochs=5, # 반복학습
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
1차: 8630 단어
model evalution
1/1 [==============================] - 0s 2ms/step - loss: 0.1229 - accuracy: 0.9500
소요시간: 4.213438034057617

2차: 4000 단어
model evalution
1/1 [==============================] - 0s 3ms/step - loss: 0.0181 - accuracy: 1.0000
소요시간: 2.4274070262908936

'''

