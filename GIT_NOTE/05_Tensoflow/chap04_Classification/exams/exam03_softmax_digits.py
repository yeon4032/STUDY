# -*- coding: utf-8 -*-
"""
문) 다음 digits 데이터셋을 이용하여 다항분류기를 작성하시오.
    <조건1> digits 데이터셋의 특성을 보고 전처리/공급data 생성  
    <조건2> 아래 <출력결과>를 참고하여 학습율과 반복학습 적용
    <조건3> epoch에 따른 loss value 시각화 : 아래 (이미지파일) 참고
           (exam03_lossValue.png)     
   
 <출력결과>
step = 200 , loss = 0.06003735238669643
step = 400 , loss = 0.02922042555340125
step = 600 , loss = 0.01916724251850193
step = 800 , loss = 0.01418028865527556
step = 1000 , loss = 0.011102086315873883
step = 1200 , loss = 0.008942419709185086
step = 1400 , loss = 0.007311927138572721
step = 1600 , loss = 0.006023632246639046
step = 1800 , loss = 0.004981346240771604
step = 2000 , loss = 0.004163072611802871
========================================
accuracy = 0.9648148148148148
"""

import tensorflow as tf # ver 2.0
from sklearn.preprocessing import OneHotEncoder # y data -> one hot
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
 
'''
digits 데이터셋 : 숫자 필기체 이미지 -> 숫자 예측(0~9)

•타겟 변수 : y
 - 0 ~ 9 : 10진수 정수 
•특징 변수(64픽셀) : X 
 -0부터 9까지의 숫자를 손으로 쓴 이미지 데이터
 -각 이미지는 0부터 15까지의 16개 명암을 가지는 
  8x8=64픽셀 해상도의 흑백 이미지
'''

digits = load_digits() # dataset load

X = digits.data  # X변수 
y = digits.target # y변수 
print(X.shape) # (1797, 64) : 64=8x8
print(y.shape) # (1797,)



# 1. digits dataset split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 2. 전처리 : X변수 정규화, Y변수 one-hot encoding  


# 3. 공급 data : 


# 4. w, b 변수 정의 


# 5. 회귀방정식 
def linear_model(X) :
    y_pred = tf.matmul(X, w) + b  
    return y_pred

# 6. softmax 활성함수 적용 
def soft_fn(X):
    y_pred = linear_model(X)
    soft = tf.nn.softmax(y_pred)
    return soft

# 7. 손실 함수 정의 : 손실계산식 수정 
def loss_fn() : #  인수 없음 
    soft = soft_fn(x_train) # 훈련셋 -> 예측치 : 회귀방정식  
    loss = -tf.reduce_mean(y_train*tf.math.log(soft)+(1-y_train)*tf.math.log(1-soft))
    return loss

# 8. 최적화 객체 



# 9. 반복학습 
    
    
# 10. 적적화된 model 검증 


# 11. loss value vs epochs 시각화 






