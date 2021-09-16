# -*- coding: utf-8 -*-
"""
문) 다음과 같이 Celeb image의 분류기(classifier)를 생성하시오.  
   조건1> train image : train_celeb4
   조건2> validation image : val_celeb4
   조건3> image shape : 120 x 120
   조건4> Image Data Generator 이용 image 자료 생성 
   조건5> model layer 
         1. Convolution layer1 : kernel_size=(4, 4), fmap=32
                                        pool_size=(2, 2)
         2. Convolution layer2 : kernel_size=(4, 4), fmap=64
                                         pool_size=(2, 2)
         3. Flatten layer
         4. DNN hidden layer1 : 64 node
         5. DNN hidden layer2 : 32 node
         6. DNN output layer : 4 node
   조건6> 기타 나머지는 lecture 내용 참고       
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D,Activation
from tensorflow.keras.layers import Dense, Flatten,Dropout 
from tensorflow.keras.callbacks import EarlyStopping # [추가]
import os

# images dir 
base_dir = "C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\"
train_dir = os.path.join(base_dir, 'exams/train_celeb4')
val_dir = os.path.join(base_dir, 'exams/val_celeb4')


# 1. CNN Model layer
model=Sequential()
 
# Convolution layer1
model.add(Conv2D(32, kernel_size=(4, 4),input_shape=(120,120,3),activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

# Convolution layer2 
model.add(Conv2D(64, kernel_size=(4, 4),activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

# Flatten layer
model.add(Flatten())

# DNN hidden layer1 : 64 node
model.add(Dense(64, activation='relu'))
model.add(Dropout(rate=0.5))
# DNN hidden layer2 : 32 node
model.add(Dense(32, activation='relu'))
model.add(Dropout(rate=0.2))

# DNN output layer : 4 node
model.add(Dense(4, activation='softmax'))

# model training set : Adam or RMSprop 
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy', # Y = 10진수(0,1,2,3,4)
              metrics = ['sparse_categorical_accuracy'])

# 2. image file preprocessing : 이미지 제너레이터 이용  
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dir setting
base_dir = "C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\exams"

train_dir = os.path.join(base_dir, 'train_celeb4')
validation_dir = os.path.join(base_dir, 'val_celeb4')

# 특정 폴더의 이미지 분류를 위한 학습 데이터셋 생성기
train_data = ImageDataGenerator(rescale=1./255) # 정규화 

# 특정 폴더의 이미지 분류를 위한 검증 데이터셋 생성기
validation_data = ImageDataGenerator(rescale=1./255)

train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(120,120), 
        batch_size=20, 
        class_mode='binary') 

validation_generator = validation_data.flow_from_directory(
        validation_dir,
        target_size=(120,120),
        batch_size=20,
        class_mode='binary')


# 3. model training : 이미지 제너레이터 객체 이용  
callback = EarlyStopping(monitor ='val_loss', patience=2)

model_fit = model.fit_generator(
          train_generator, 
          steps_per_epoch=31,  
          epochs=5,  
          validation_data=validation_generator,
          validation_steps=10,
          callbacks=[callback])


# 4. model history graph
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

