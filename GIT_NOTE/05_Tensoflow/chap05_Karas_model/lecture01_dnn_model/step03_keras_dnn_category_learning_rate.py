# -*- coding: utf-8 -*-
"""
step03_keras_dnn_category_learning_rate.py

step02_keras_dnn_category.py 참고
 Keras :DNN model생성을 위한 고수준 API
 
 - iris dataset 다항분류기
X변수 : 스케이링(0~1)
Y변수 : one hot encoding 
optimizer =Adam(learning_rate = 0.01)
"""

from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # split
from sklearn.preprocessing import minmax_scale # x변수 : 스케일링(0~1)
from sklearn.metrics import accuracy_score # model 평가

from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense # DNN layer 구축
from tensorflow.keras.models import load_model # model load

import tensorflow as tf
import numpy as np 
import random as rd

########################################################################
### keras 내부 seed 적용
########################################################################3
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)

# 1. dataset load & 전처리
X,y = load_iris(return_X_y=True)
X.shape #(150, 4)
y.shape #(150,)

# X변수 : 정규화(0~1) 
X = minmax_scale(X)

# Y변수 : one hot encoding
y_one = to_categorical(y)
print(y_one)
y_one.shape # (150, 3)
'''
[1. 0. 0.] <- class 0
[0. 1. 0.] <- class 1 
[0. 0. 1.] <- class 2
'''

# 2. 공급 data 생성 : 훈련용, 검증용
x_train, x_val, y_train, y_val = train_test_split(
    X, y_one, test_size=0.3,random_state=123)

# 3. Keras model
model = Sequential()

# 4. DNN model layer 구축 
'''
model.add() : layer 추가 매소드
Dense(units= 뉴런수, input_shape=입력수, activation=활성홤수)  - 1층 
Dense(units= 뉴런수, activation=활성홤수)  - 2층 ~ n층 

'''

# hidden layer1 : [4, 12] -> [input, output] 
model.add(Dense(units=12, input_shape=(4,), activation = 'relu')) # 1층

# hidden layer1 : [12, 6] -> [input, output] 
model.add(Dense(units=6, activation = 'relu')) # 2층

# output layer: [6, 3] -> [input, output] 
model.add(Dense(units=3,activation ='softmax')) # 3층 

# layer 확인
model.summary()

'''
Model: "sequential_3"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_10 (Dense)             (None, 12)                60        
_________________________________________________________________
dense_11 (Dense)             (None, 6)                 78        
_________________________________________________________________
dense_12 (Dense)             (None, 3)                 21        
=================================================================
Total params: 159
Trainable params: 159
Non-trainable params: 0
_________________________________________________________________
'''


# 5. model compile : 학습과정 설정(이항분류기) - [수정]
from tensorflow.keras import optimizers

# optimizer='adam' -> default =0.001
model.compile(optimizer= optimizers.Adam(learning_rate = 0.01), # lr default =0.001
              loss = 'categorical_crossentropy', # y: one hot encoding  
              metrics=['accuracy'])
'''
optimizer : 죄적화 알고리즘('adma' or 'sdg')
loss : 비용함수('binary_crossentropy' or 'categorical_crossentropy' or 'mse')
metirics: 평가방법('accuracy' or 'mae')
'''

# 6. model training : train(105) vs val(45)
model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=200, # 반복학습 
          verbose=1, # 출력여부
          validation_data=(x_val, y_val)) # 검증셋

# 7. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)

# 8. model save & load: HDF5 파일 형식 
model.save('keras_model_iris.h5')

my_model = load_model('keras_model_iris.h5')

# 9. model test: new dataset 적용 

# 1) new dataset
x_train,x_test,y_train,y_test = train_test_split(
    X,y_one,test_size=0.5,random_state=123)

y_pred = my_model.predict(x_test)
print(y_pred) # 확률 예측 : softmax
print(y_pred.shape) # (75, 3)

#확률 예측 -> 10진수 변경
y_pred = tf.argmax(y_pred, axis=1) # 가장 높은 확률 색인 가지고 오기

# 정답 : 2진수 -> 10진수 변경
y_true = tf.argmax(y_test, axis=1)

acc = accuracy_score(y_true,y_pred)
print('accuracy =',acc)
# accuracy = 0.9733333333333334


















