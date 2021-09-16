# -*- coding: utf-8 -*-
"""
문) fashion_mnist 데이터셋을 이용하여 다음과 같이 keras 모델을 생성하시오.
    
  조건1> keras layer
       L1 =  (28, 28) x 128
       L2 =  128 x 64
       L3 =  64 x 32
       L4 =  32 x 16
       L5 =  16 x 10
  조건2> output layer 활성함수 : softmax     
  조건3> optimizer = 'Adam',
  조건4> loss = 'categorical_crossentropy'
  조건5> metrics = 'accuracy'
  조건6> epochs = 15, batch_size = 32   
  조건7> model evaluation : validation dataset
"""
from tensorflow.keras.utils import to_categorical # one hot
from tensorflow.keras.datasets import fashion_mnist # fashion
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Dense, Flatten # model layer
import matplotlib.pyplot as plt

# 1. MNIST dataset loading
(train_img, train_lab),(val_img, val_lab)=fashion_mnist.load_data() # (images, labels)
train_img.shape # (60000, 28, 28) 
train_lab.shape # (60000,) 
 


# 2. x, y변수 전처리 
# x변수 : 정규화(0~1), 3d -> 2d(reshape)
train_img = train_img / 255.
val_img = val_img / 255.
train_img[0] # first image(0~1)
val_img[0] # first image(0~1)


# y변수 : one hot encoding 
train_lab = to_categorical(train_lab)
val_lab = to_categorical(val_lab)
val_lab.shape # (10000, 10)

# 입력 : 28x28
# 출력 : 10개 


# 3. keras model
model = Sequential() 

model.add(Flatten(input_shape=(28,28)))
model.add(Dense(units=128,input_shape=(784,),activation = 'relu'))
model.add(Dense(units=64,activation = 'relu'))
model.add(Dense(units=32,activation = 'relu'))
model.add(Dense(units=16,activation = 'relu'))
model.add(Dense(units=10,activation = 'softmax'))


# 4. DNN model layer 구축 
model.compile(optimizer = 'Adam',
              loss = 'categorical_crossentropy',
              metrics = 'accuracy')


# 5. model training 
model.fit(x=train_img, y=train_lab,
          epochs = 15,
          batch_size = 32,
          validation_data=(val_img, val_lab))

# 6. model evaluation : validation dataset
print('='*30)
print('model evalution')
model.evaluate(x=val_img, y=val_lab)


