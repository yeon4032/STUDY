# -*- coding: utf-8 -*-
"""
step04_keras_cnn_cifa_tensorboard.py

step03_keras_cnn_cifar10.py -참조

-keras CNN layer tensorboard 시각화

"""
import tensorflow as tf
from tensorflow.keras.datasets.cifar10 import load_data # image dataset
from tensorflow.keras.utils import to_categorical # one hot encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Conv2D, MaxPool2D # Conv layer
from tensorflow.keras.layers import Dense,Flatten, Dropout # DNN layer
import matplotlib.pyplot as plt

#[추가] tensorboard 초기화
tf.keras.backend.clear_session()

# 1. image dataset load
(x_train,y_train), (x_val,y_val) = load_data()
x_train.shape # image: (50000 ,32 ,32 ,3) - (size, h, w, c)
y_train.shape # label: (50000, 1)

first_img = x_train[0]
first_img.shape # (32, 32, 3)

plt.imshow(first_img)
plt.show()

print(y_train[0]) # [6]

x_val.shape # image: (10000, 32, 32, 3)
y_val.shape # label: (10000, 1)


# 2. image dataset 전처리
type(x_train)#numpy.ndarray
#1) image pixel 실수형 변환
x_train = x_train.astype(dtype='float32') # image vs filter
x_val = x_val.astype(dtype='float32')

# 2) image 정규화: 0~1
x_train = x_train/255
x_val = x_val/255

x_train[0]

# 3) label 전처리 : 10 - > one hot encoding (2 진수)
y_train = to_categorical(y_train, num_classes=10)
y_val = to_categorical(y_val, num_classes=10)
y_train.shape# (50000,10)
y_train[0] #1., 0., 0., 0., 0., 0., 0., 0., 0., 0.], ....



# 3. CNN model 생성 : layer 구축 + 학습환경 + 학습

input_shape=(32,32,3) #3차원 이미지 들어온다.

# 1) model 생성
model= Sequential()

# 2) layer 구축
# filters= 특징 map 생성 개수 
# kernel_size= 필터 크기

# Conv layer1: filter[5, 5, 3, 32] 
model.add(Conv2D(filters=32,kernel_size=(5,5),
                 input_shape=input_shape, activation='relu')) # image 28x28 (32x32->28x28)
model.add(MaxPool2D(pool_size=(3,3),strides=(2,2))) # image[16x16]
# filters = 특징맵 개수, kernel_size = 필터 크기, pool_size = 다운샘플링을 위한 윈도 크기

model.add(Dropout(0.3))


# Conv layer2: filter[5, 5, 32, 64] 
model.add(Conv2D(filters=64,kernel_size=(5,5),activation='relu'))
model.add(MaxPool2D(pool_size=(3,3),strides=(2,2))) # image[4x4]
model.add(Dropout(0.1))


# Conv layer3: filter[5, 5, 64, 128] -Maxp=Pool2D 없음
model.add(Conv2D(filters=128,kernel_size=(3,3),activation='relu')) 
# 4x4 이미지인데 필터 사이즈는 이미지 사이즈 보다 클수 없음으로 4x4 보다 작은 3x3으로 됨.
model.add(Dropout(0.1))

# Flatten Flayer : 3d[h,w,c] -> 1d[n=h*w*c] 
# 차원 변경 해주는 래이어
model.add(Flatten())


# DNN: hidden layer 4 층
model.add(Dense(units=64,activation='relu'))


# DNN: hidden layer 5 층
model.add(Dense(units=10,activation='softmax'))


model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 28, 28, 32)        2432      
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
dropout (Dropout)            (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 9, 9, 64)          51264     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 4, 4, 64)          0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 4, 4, 64)          0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 2, 2, 128)         73856     
_________________________________________________________________
dropout_2 (Dropout)          (None, 2, 2, 128)         0         
_________________________________________________________________
flatten (Flatten)            (None, 512)               0         
_________________________________________________________________
dense (Dense)                (None, 64)                32832     
_________________________________________________________________
dense_1 (Dense)              (None, 10)                650       
=================================================================
Total params: 161,034
Trainable params: 161,034
Non-trainable params: 0

'''



#3) model 환경설정
model.compile(optimizer= 'adam', # lr default =0.001
              loss = 'categorical_crossentropy', # y: one hot encoding  
              metrics=['accuracy'])


#[추가] Tensorboard 
from tensorflow.keras.callbacks import TensorBoard
from datetime import datetime # '20210720- 1041'

logdir = 'c:/graph/' + datetime.now().strftime('%Y%m%d_%H%M%S') # datetime에서 .now() 는 현제 시간을 의미/ strftime은 년월일 그리고 시간 을 str 형식으로 가지고 온다.
callback=TensorBoard(log_dir=logdir)

# 4). model training : train vs val
model_fit = model.fit(x=x_train,y=y_train, # 훈련셋
          epochs=10, # 반복학습
          batch_size = 100, # 1회 공급 image size (100*500=1epoch=50,000)
          verbose=1, # 출력여부
          validation_data=(x_val, y_val), # 검증셋
          callbacks=[callback]) # [추가]


#  4. CNN model 평가 : val dataset 
print('='*30)
print('model evalution')
model.evaluate(x=x_val, y=y_val)


# 5. CMM model history 
print(model_fit.history.keys())
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

# loss vs val_loss 
plt.plot(model_fit.history['loss'], 'y', label='train loss')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

# accuracy vs val_accuracy
plt.plot(model_fit.history['accuracy'], 'y', label='train acc')
plt.plot(model_fit.history['val_accuracy'], 'r', label='val acc')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()


'''
Tensorboard 실행순서
1. logdir 확인: log 파일 확인
2. (base) conda activate tensorflow
3. (tensorflow) tensorboard --logdir=C:\graph\20210720 - 104905\train
 #or            tensorboard --logdir=C:\graph\20210720 - 104905\validation
4. http://localhost/6006
'''
























