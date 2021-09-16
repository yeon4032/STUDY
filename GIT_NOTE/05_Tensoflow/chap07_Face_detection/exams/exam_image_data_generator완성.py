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
import tensorflow as tf
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D,Activation
from tensorflow.keras.layers import Dense, Flatten, Dropout 
from tensorflow.keras.callbacks import EarlyStopping
import os

tf.random.set_seed(123)

# images dir 
base_dir = "C:/ITWILL/5_Tensorflow/workspace/chap07_Face_detection/"
train_dir = os.path.join(base_dir, 'exams/train_celeb4')
val_dir = os.path.join(base_dir, 'exams/val_celeb4')


# Hyper parameters
img_h = 120 # height
img_w = 120 # width
input_shape = (img_h, img_w, 3) 

# 1. CNN Model layer 
print('model create')
model = Sequential()

# 합성곱 1층 : [3,3,3,32]
model.add(Conv2D(32, kernel_size=(4,4),input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# 합성곱 2층 : [3,3,32,64]
model.add(Conv2D(64, kernel_size=(4,4)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2,2)))


# 전결합층 
model.add(Flatten())

# 완전연결층 3층 : Affine + relu
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(rate=0.5))

# 완전연결층 4층 : Affine + relu
model.add(Dense(32, activation = 'relu'))
model.add(Dropout(rate=0.2))

# 출력층 5층 : Affine + softmax
model.add(Dense(4, activation = 'softmax')) # 4 classes


# model training set : Adam or RMSprop 
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy', # Y = 10진수(0,1,2,3,4) 
              metrics = ['sparse_categorical_accuracy'])

# 2. image file preprocessing : 이미지 제너레이터 이용  
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# training dataset
train_data = ImageDataGenerator(rescale=1./255)

# validation datast 
val_data = ImageDataGenerator(rescale=1./255)

# train image 생성기 
train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(120,120), # image resize
        batch_size=20, # batch size        
        class_mode='binary') # loss = categorical_crossentropy
# Found 609 images belonging to 4 classes.

# validation image 생성기

val_generator = val_data.flow_from_directory(
        val_dir,
        target_size=(120,120),
        batch_size=20,
        class_mode='binary') # loss = categorical_crossentropy
# Found 200 images belonging to 4 classes.


# 3. model training : 이미지 제너레이터 객체 이용  
callback = EarlyStopping(monitor='val_loss', patience=2) # [추가]
# epoch=2 이후 검증 손실이 개선되지 않으면 조기종료 

model_fit = model.fit_generator(
          train_generator, 
          steps_per_epoch=31, #(620 = 31*20)
          epochs=10, 
          validation_data=val_generator,
          validation_steps=10,
          callbacks=[callback]) #(200 = 10*20)


# 4. model history graph
import matplotlib.pyplot as plt
 
print(model_fit.history.keys())
# dict_keys(['loss', 'sparse_categorical_accuracy', 'val_loss', 'val_sparse_categorical_accuracy'])

loss = model_fit.history['loss'] # train
acc = model_fit.history['sparse_categorical_accuracy']
val_loss = model_fit.history['val_loss'] # validation
val_acc = model_fit.history['val_sparse_categorical_accuracy']


# acc vs val_acc   
plt.plot(acc, 'b', label='train acc')
plt.plot(val_acc, 'r', label='val acc')
plt.title('Training vs validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuray')
plt.legend(loc='best')
plt.show()

# loss vs val_loss 
plt.plot(loss, 'b', label='train loss')
plt.plot(val_loss, 'r', label='val loss')
plt.title('Training vs validation loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()







