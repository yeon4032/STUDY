# -*- coding: utf-8 -*-
"""
lecture02_celeb_classifier

 1. celeb5 이미지 분류기 : CNN
 2. Image Generator : MODEL 공급할 이미지 생성기
 
 Chap06> lecture02> step01_cats_dogs_imageGenerator.py 참조
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D # Convolution layer
from tensorflow.keras.layers import Dense, Flatten # DNN layer
import os


# image resize
img_h = 150 # height
img_w = 150 # width
input_shape = (img_h, img_w, 3) # 입력된느 image 모양

# 1. CNN Model layer 
print('model create')
model = Sequential()

# Convolution layer1 :[3,3,3,32]
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu',
                 input_shape = input_shape))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer2 :[3,3,32,64]
model.add(Conv2D(64,kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer3 : 제외 (정제된 image 여서 더 학습 시킬 이유 없음)


# Flatten layer : 3d -> 1d
model.add(Flatten()) # 전결합층

# DNN hidden layer(Fully connected layer)
model.add(Dense(256, activation = 'relu'))

# DNN Output layer
model.add(Dense(5, activation = 'softmax')) # 5 classes: 5 명 분류

# model training set : Adam or RMSprop 
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy', # Y = 10진수(0,1,2,3,4)
              metrics = ['sparse_categorical_accuracy'])
'''
loss = 'categorical_crossentropy' -> Y=2진수(one-hot encoding)
loss = 'sparse_categorical_crossentropy' ->  Y=10진수 

metrics = accuracy -> Y=2진수(one-hot encoding)
metrics = 'sparse_categorical_accuracy' -> Y=10진수 (다항분류여서categorical, 이항분류이면 binary)
'''


# 2. image file preprocessing : image 제너레이터 이용  
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dir setting
base_dir = "C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\lecture02_celeb_classifier\\celeb5__image"

train_dir = os.path.join(base_dir, 'train_celeb5')
validation_dir = os.path.join(base_dir, 'val_celeb5')


# 특정 폴더의 이미지 분류를 위한 학습 데이터셋 생성기
train_data = ImageDataGenerator(rescale=1./255) # 정규화 

# 특정 폴더의 이미지 분류를 위한 검증 데이터셋 생성기
validation_data = ImageDataGenerator(rescale=1./255)

train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(150,150), # image reshape
        batch_size=20, # batch size
        class_mode='binary') # binary label
# Found 990 images belonging to 5 classes.

validation_generator = validation_data.flow_from_directory(
        validation_dir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary')
# Found 250 images belonging to 5 classes.

# 3. model training : image제너레이터 이용 모델 훈련 

model_fit = model.fit_generator(
          train_generator, 
          steps_per_epoch=50,  # 50(step) * 20(batch size) = 1000(1epoch)
          epochs=5,  # 1000*5 =5,0000
          validation_data=validation_generator,
          validation_steps=13) # 13*20 =260(1epoch)
# 50*20 = 1000
# 13*20 = 260

# model evaluation
model.evaluate(validation_generator)


# 4. model history graph
import matplotlib.pyplot as plt
 
print(model_fit.history.keys())
# dict_keys(['loss', 'sparse_categorical_accuracy', 'val_loss', 'val_sparse_categorical_accuracy'])

# [ket 변경]
loss = model_fit.history['loss'] # train
acc = model_fit.history['sparse_categorical_accuracy'] # 변경
val_loss = model_fit.history['val_loss'] # validation
val_acc = model_fit.history['val_sparse_categorical_accuracy'] # 변경

## 3 epoch 과적합 시작점
epochs = range(1, len(acc) + 1)

# acc vs val_acc   
plt.plot(epochs, acc, 'b--', label='train acc')
plt.plot(epochs, val_acc, 'r', label='val acc')
plt.title('Training vs validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuray')
plt.legend(loc='best')
plt.show()

# loss vs val_loss 
plt.plot(epochs, loss, 'b--', label='train loss')
plt.plot(epochs, val_loss, 'r', label='val loss')
plt.title('Training vs validation loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()



