# -*- coding: utf-8 -*-
"""
step01_ImageNet_Classifier.py

딥러닝 이미지넷 분류기
 - InmageNet으로 학습된 이미지 분류기
 - 가공을 통해서 전이학습 가능
##
# vgg16 vs Conv2D랑 Maxpool2D
- vgg
:vgg는 24,000개 이미지와 잘 훈련된 가중치를 이용하기 때문에 분류 성능이 좋습니다.
: 입력 이미지를 대상으로 1,000개 범주로 분류하는 학습된 모델

-Conv2D랑 Maxpool2D
Conv2D : 이미지에서 특징 추출
Maxpool2D : 이미지 픽셀수를 줄이는 레이어

In short
vgg는 학습량이 만하져서 정확도는 높임
Conv2D& Maxpool2D는 특징만 남겨서 이미지를 파악
"""

# 1. VGGNet(VGG16/VGG19) model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19

# 1) model load
vgg16_model = VGG16(weights='imagenet') # 학습된 가중치 load
vgg19_model = VGG19(weights='imagenet') # 학습된 가중치 load

# 2) model layer
vgg16_model.summary()


# input layer 
vgg16_model.layers[0].output
# <tf.Tensor 'input_1:0' shape=(None, 224, 224, 3) dtype=float32>

# output layer
vgg16_model.layers[-1].output
# <tf.Tensor 'predictions/Softmax:0' shape=(None, 1000) dtype=float32>

# 3) model test : 실제 image 적용
from tensorflow.keras.preprocessing import image # image read
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions

# image load
path='C:\\ITWILL\\5_Tensoflow\\data\\images\\'
img=image.load_img(path+'umbrella.jpg',target_size=(224,224))

X = image.img_to_array(img) # array 변환
X.shape # (224, 224, 3)

X=X.reshape(1, 224,224,3)

# image 전처리
X=preprocess_input(X)

# image 예측
pred = vgg16_model.predict(X)
pred.shape # (1, 1000)

print('predicted:',decode_predictions(pred,top=3)) # pred와 가장 유사한 3개 가지고오기
'''
화산
 predicted: [[('n09472597', 'volcano', 0.9999949), 화산 확률 :99.99%
             ('n04456115', 'torch', 3.266852e-06),
             ('n02939185', 'caldron', 4.753484e-07)]]
'''
'''
우산
predicted: [[('n04507155', 'umbrella', 0.9776497), 우산 확률: 97.64%
             ('n03944341', 'pinwheel', 0.021190464),
             ('n03888257', 'parachute', 0.0008389075)]]
'''

# 2. ResNet50 model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# 1) model load
resnet50_model = ResNet50(weights='imagenet') # 학습된 가중치 load

# 2) model layer
resnet50_model.summary()

# input layer 
resnet50_model.layers[0].output
# <tf.Tensor 'input_1:0' shape=(None, 224, 224, 3) dtype=float32>

# output layer
resnet50_model.layers[-1].output
# <tf.Tensor 'predictions/Softmax:0' shape=(None, 1000) dtype=float32>

# image load
path='C:\\ITWILL\\5_Tensoflow\\data\\images\\'
img=image.load_img(path+'umbrella.jpg',target_size=(224,224))

X = image.img_to_array(img) # array 변환
X.shape # (224, 224, 3)

X=X.reshape(1, 224,224,3)

# image 전처리
X=preprocess_input(X)

# image 예측
pred = resnet50_model.predict(X)
pred.shape # (1, 1000)

print('predicted:',decode_predictions(pred,top=3))
'''
predicted: [[('n04507155', 'umbrella', 0.9674324), 
             ('n03888257', 'parachute', 0.028271936), 
             ('n02782093', 'balloon', 0.0027301894)]]
'''

# 3. Inception_v2_model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions

# 1) model load
Inception_v3_model = InceptionV3(weights='imagenet') # 학습된 가중치 load

# 2) model layer
Inception_v3_model.summary()

# input layer 
Inception_v3_model.layers[0].output
# <tf.Tensor 'input_2:0' shape=(None, 299, 299, 3) dtype=float32>

# output layer
Inception_v3_model.layers[-1].output
# <tf.Tensor 'predictions/Softmax_1:0' shape=(None, 1000) dtype=float32>

# image load
path='C:\\ITWILL\\5_Tensoflow\\data\\images\\'
img=image.load_img(path+'volcano.jpg',target_size=(299,299))

X = image.img_to_array(img) # array 변환
X.shape # (299, 299, 3)

X=X.reshape(1, 299, 299, 3)

# image 전처리
X=preprocess_input(X)

# image 예측
pred = Inception_v3_model.predict(X)
pred.shape # (1, 1000)

print('predicted:',decode_predictions(pred,top=3))
'''
predicted: [[('n09472597', 'volcano', 0.96333694), 
             ('n03347037', 'fire_screen', 0.0013190561), 
             ('n03729826', 'matchstick', 0.0008878633)]]
'''

