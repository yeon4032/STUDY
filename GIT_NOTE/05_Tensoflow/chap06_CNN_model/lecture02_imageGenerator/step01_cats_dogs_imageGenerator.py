# -*- coding: utf-8 -*-
"""
Cats vs Dogs image classifier 
 - image data generator 이용 : 학습 데이터셋 만들기 
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D # Convolution layer
from tensorflow.keras.layers import Dense, Flatten # Affine layer
import os


# image resize
img_h = 150 # height
img_w = 150 # width
input_shape = (img_h, img_w, 3) 

# 1. CNN Model layer 
print('model create')
model = Sequential()

# Convolution layer1 
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu',
                 input_shape = input_shape))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer2 
model.add(Conv2D(64,kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer3 : maxpooling() 제외 
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# Flatten layer : 3d -> 1d
model.add(Flatten()) 

# DNN hidden layer(Fully connected layer)
model.add(Dense(256, activation = 'relu'))

# DNN Output layer
model.add(Dense(1, activation = 'sigmoid')) # one hot encoding 사용시 units 은 2 여야만 하나 여기서는 ?

# model training set : Adam or RMSprop 
model.compile(optimizer = 'adam',
              loss = 'binary_crossentropy', # one hot encoding
              metrics = ['accuracy'])

# 2. image file preprocessing : image 제너레이터 이용  
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dir setting
base_dir = "C:\\ITWILL\\5_Tensoflow\\data\\images\\cats_and_dogs"

train_dir = os.path.join(base_dir, 'train_dir')
validation_dir = os.path.join(base_dir, 'validation_dir')


# 특정 폴더의 이미지 분류를 위한 학습 데이터셋 생성기
train_data = ImageDataGenerator(rescale=1./255) # 정규화 

# 특정 폴더의 이미지 분류를 위한 검증 데이터셋 생성기
validation_data = ImageDataGenerator(rescale=1./255)

train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(150,150), # image reshape
        batch_size=20, # batch size
        class_mode='binary') # binary label
# Found 2000 images belonging to 2 classes.

validation_generator = validation_data.flow_from_directory(
        validation_dir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary')
# Found 1000 images belonging to 2 classes.

# 3. model training : image제너레이터 이용 모델 훈련 
model_fit = model.fit_generator(
          train_generator, 
          steps_per_epoch=100,  #batch size의 step =100(step)*20 = 1epoch
          epochs=10,  # 2000*10 =20,0000
          validation_data=validation_generator,
          validation_steps=50) # batch_sizedml step 수=50*20=1,000= 1epoch

# model evaluation
model.evaluate(validation_generator)


# 4. model history graph
import matplotlib.pyplot as plt
 
print(model_fit.history.keys())
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

loss = model_fit.history['loss'] # train
acc = model_fit.history['accuracy']
val_loss = model_fit.history['val_loss'] # validation
val_acc = model_fit.history['val_accuracy']

## 3 epoch 과적합 시작점
epochs = range(1, len(acc) + 1)

# acc vs val_acc   
plt.plot(epochs, acc, 'bo', label='train acc')
plt.plot(epochs, val_acc, 'r', label='val acc')
plt.title('Training vs validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuray')
plt.legend(loc='best')
plt.show()

# loss vs val_loss 
plt.plot(epochs, loss, 'bo', label='train loss')
plt.plot(epochs, val_loss, 'r', label='val loss')
plt.title('Training vs validation loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

