# -*- coding: utf-8 -*-
"""
step04_keras_mnist_tensorboard.py

Tensorboard: loss value, accuracy 시각화

lecture02 > step03_keras_mnist_earlyStopping.py참고
"""

from tensorflow.keras.datasets.mnist import load_data # MNIST dataset
from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense,Dropout # DNN layer 구축
from tensorflow.keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt # 
import tensorflow as tf
import numpy as np 
import random as rd
import time # 실행 시간 측정

########################################################################
### keras 내부 seed 적용
########################################################################3
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)


#1. mnist dataset load
(x_train,y_train),(x_val,y_val) = load_data() # (images, labels)
x_train.shape # (60000, 28, 28) - 3d(size, h, w) -> 2d(size, h*w)
y_train.shape # (60000,)

x_train[0] # first image pixel
x_train[0].max() # 0~255

plt.imshow(x_train[0])
plt.show()

y_train[0] # first label -  10 진수 : 5

# 2. x,y 변수 전처리

# 1) x변수 : 정규화 & reshape(3d -> 2d)
#정규화
x_train = x_train / 255.
x_val = x_val / 255.

x_train[0]


# reshape
x_train = x_train.reshape(-1, 784) #28 * 28 = 748
x_train.shape # (60000, 784)

x_val= x_val.reshape(-1,784)
x_val.shape # (10000, 784)


# 2) y 변수: one hot encoding
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_train.shape # (60000, 10) 

y_train[0] # [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.] <- 5 
#5번 인덱스 만 1이고 나머지는 0임 
#<=y_train[0] # first label -  10 진수 : 5 가 변경된거임

y_val[0] # [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.] <- 7 
# 7번 인텍스 가 1이고 나머지는 0


# 3. Keras model
model = Sequential()


# 4. DNN model layer 구축 : hidden layer(3) -> output layer(1)
'''
model.add() : layer 추가 매소드
Dense(units= 뉴런수, input_shape=입력수, activation=활성홤수)  - 1층 
Dense(units= 뉴런수, activation=활성홤수)  - 2층 ~ n층 
'''

# hidden layer1 : 784, 128] -> [input, output] 
model.add(Dense(units=128, input_shape=(784,), activation = 'relu')) # 1층
model.add(Dropout(rate = 0.3)) #[추가]

# hidden layer2 : [128, 64] -> [input, output] 
model.add(Dense(units=64, activation = 'relu')) # 2층
model.add(Dropout(rate = 0.1)) #[추가]

# hidden layer3 : [64, 32] -> [input, output] 
model.add(Dense(units=32, activation = 'relu')) # 3층
model.add(Dropout(rate = 0.1)) #[추가]

# output layer: [32, 10] -> [input, output] 
model.add(Dense(units=10,activation ='softmax')) # 4층 

# layer 확인
model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 128)               100480    
_________________________________________________________________
dense_1 (Dense)              (None, 64)                8256      
_________________________________________________________________
dense_2 (Dense)              (None, 32)                2080      
_________________________________________________________________
dense_3 (Dense)              (None, 10)                330       
=================================================================
Total params: 111,146
Trainable params: 111,146
Non-trainable params: 0
'''
chktime = time.time()  # 소요 시간 체크


# 5. model compile : 학습과정 설정(이항분류기) - [수정]
from tensorflow.keras import optimizers

# optimizer='adam' -> default =0.001
model.compile(optimizer= optimizers.Adam(), # lr default =0.001
              loss = 'categorical_crossentropy', # y: one hot encoding  
              metrics=['accuracy'])

# [추가]
from tensorflow.keras.callbacks import TensorBoard
from datetime import datetime # 20210716-1540

# 6. [수정] model training : train(60000) vs val(10000)  [추가]
logdir = 'c:\\grapth\\' + datetime.now().strftime("%Y%m%d-%H%M%S")
callback = TensorBoard(log_dir = logdir)
# epoch=10 이후 검증 손실이 개선되지 않으면 조기종료

model_fit = model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=20, # 반복학습
          batch_size = 100, 
          verbose=1, # 출력여부
          validation_data=(x_val, y_val),
          callbacks = [callback]) # 검증셋

# 실행 시간 비교 (full vs mini)
chktime = time.time() -chktime
print('실행 시간:', chktime)
#실행 시간: 40.08854269981384 full batch
#실행 시간: 19.76519536972046 mini batch


# 7. model evaluation : val dataset 이용.
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)


# 8. model history
print(model_fit.history.keys())
#dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

import matplotlib.pyplot as plt 

# loss vs val_loss : overfitting 시작점 : epoch 2
plt.plot(model_fit.history['loss'], 'y', label='train loss')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

# accuracy vs val_accuracy: overfitting 시작점 : epoch 2
plt.plot(model_fit.history['accuracy'], 'y', label='train acc')
plt.plot(model_fit.history['val_accuracy'], 'r', label='val acc')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

'''
<작업절차>
1. log file 확인(train, vlidation)
2. log file 실행
(base) > conda activate tensorflow 
(tensorflow) > tnesorboard --logdir='c:\\grapth\\C:\grapth\20210716-155002\train'

(tensorflow) > tnesorboard --logdir='c:\\grapth\\C:\grapth\20210716-155002\tvalidation'
'''



















