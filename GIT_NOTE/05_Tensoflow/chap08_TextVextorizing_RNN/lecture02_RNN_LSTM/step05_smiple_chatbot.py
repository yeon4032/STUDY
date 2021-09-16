# -*- coding: utf-8 -*-
"""
step05_smiple_chatbot.py

many to one: 단어1> 단어2> 단어3 -> 단어4

"""

# 작업 순서
# texts -> 토큰 -> 정수 인덱스 -> 순차 data(RNN 공급) -> padding(인코딩) -> X, Y

# texts 처리
import numpy as np # list -> numpy
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences  #패딩
from tensorflow.keras.utils import to_categorical # y변수:  one hot 인코딩

# RNN + DNN model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM

# ppt 참고
text="""이름은 홍길동
취미는 음악감상 독서 등산
직업은 강사 프로그래머"""

#1. 토큰(token)
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text]) # 텍스트 반영 (입력값을 list 형이여햐한다.)
voca=tokenizer.word_index # 토큰 단어
print(voca)
'''
{'이름은': 1, '홍길동': 2, '취미는': 3, '음악감상': 4, '독서': 5, '등산': 6, '직업은': 7, '강사': 8, '프로그래머': 9}
'''

# 전체 단어수 + 1
vocab_size = len(voca) + 1
print('전체 단어수=', vocab_size)

# 2. 정수 인텍스 -> 순차data(RNN 공급)
'''
이름은 -> 홍길동
취미는 -> 등산
취미는 음악감상 -> 독서
취미는 음악감상 독서 -> 등산
'''

seqences = []
for line in text.split('\n'):
    #1) 정수 인텍스
    seq = tokenizer.texts_to_sequences([line])[0] # 단일 리스트로 받으로려고 [0] 붙인거임
    print(seq)
    '''
    [1, 2]
    [3, 4, 5, 6]
    [7, 8, 9]
    '''
    
    # 2) sequence data 생성
    for i in range(1, len(seq)): # 1 ~ n-1
        seqence=seq[:i+1]
        print(seqence)
        '''
        [1, 2]
        [1, 2]
        [3, 4, 5, 6]
        [3, 4]
        [3, 4, 5]
        [3, 4, 5, 6]
        [7, 8, 9]
        [7, 8]
        [7, 8, 9]
        '''
        seqences.append(seqence)
    
print(seqences) # 학습할 문장 = 6 개
# [[1, 2], [3, 4], [3, 4, 5], [3, 4, 5, 6], [7, 8], [7, 8, 9]]


# 3. padding(인코딩): maxlen -> 0 padding
lens = [len(s) for s in seqences]
maxlen = max(lens) 
print(maxlen) # 4

# 최대 단어 길이 이용 padding
sequences = pad_sequences(seqences,maxlen=maxlen)
print(sequences)
'''
[[0 0 1 2] -> x=[0 0 1], y = [2]
 [0 0 3 4] -> x=[0 0 3], y = [4]
 [0 3 4 5]             :
 [3 4 5 6]
 [0 0 7 8]
 [0 7 8 9]]
'''

# 4. X, y 변수 생성
X= sequences[:,:-1]
'''
array([[0, 0, 1],
       [0, 0, 3],
       [0, 3, 4],
       [3, 4, 5],
       [0, 0, 7],
       [0, 7, 8]])
'''
X.shape # (6, 3) -> (1,6,3): (batch_size, time_step, features)

y= sequences[:,-1]
'''
array([2, 4, 5, 6, 8, 9])
'''

# 10 진수 -> one-hot encoding
y= to_categorical(y,num_classes=vocab_size)
'''
array([[0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]], dtype=float32)
'''

# 5. model 생성
model = Sequential()

# 6. embedding: 정수 인덱스 -> 인코딩
model.add(Embedding(input_dim = vocab_size ,output_dim=4,
                    input_length=maxlen-1))
'''
input_dim : 전체 단어수
output_dim: embedding vector 크기(차원)
input_length: 한 문장을 구성하는 단어 길이(maxlen)  # y값으로 하나사용해서 -1 하는거임
'''

# 7. RNN(순환 신경망)
model.add(LSTM(units=32, activation='tanh'))

# 8. output layer
model.add(Dense(units= vocab_size, activation='softmax'))

# 9. model 학습환경
model.compile(optimizer='adam',
              loss='categorical_crossentropy', # y : one hot encoding
              metrics=['accuracy'])

# 10. model 학습
model.fit(X, y, epochs=200, verbose=1)



# 문장 생성기 
def sentence_generation(search_word, n=0): # 검색 단어, 단어길이
    global model, tokenizer, max_len, X
      
    seq_idx = tokenizer.texts_to_sequences([search_word])[0]      
    # 검색 단어 길이 결정  
    for row in X :
        if seq_idx in row : 
                n += 1
                
    if n == 0 : # "해당 단어 없음"
        return 0
    
    sentence = '' # 문장 save
    start_word = search_word # 검색 단어 변수 저장 

    for i in range(n): # n번 반복       
        # 1. 인코딩 : 검색단어-> 정수 인덱스
        seq_idx = tokenizer.texts_to_sequences([search_word])[0]#현재 단어 정수인코딩
        encoded = pad_sequences([seq_idx], maxlen=max_len-1) # 데이터에 대한 패딩
        #2. RNN model 예측
        result = model.predict_classes(encoded, verbose=0)   

        #3. 디코딩: 예측치(인코딩) - 단어 변환
        for word, index in tokenizer.word_index.items(): 
            if index == result: # 만약 예측한 단어와 인덱스와 동일한 단어가 있다면
                break # 해당 단어가 예측 단어이므로 break
        search_word = search_word + ' '  + word # 현재 단어+ ' '+예측 단어 ->현재 단어 변경
        sentence = sentence + ' ' + word # 예측 단어 문장 생성
    
    sentence = start_word + sentence
    return sentence

# 검색 단어 입력 
while(True) :
    result = sentence_generation(input("검색단어 : "))
    print(result)
    if result == 0 :
        print("해당 단어 없음")
        break













