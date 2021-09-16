# -*- coding: utf-8 -*-
"""
step04_reshape2.py

 - image reshape
"""

import numpy as np
import matplotlib.pyplot as plt # image show
from sklearn.datasets import load_digits #dataset load

#1. dataset load
digits=load_digits() # 머신러닝에서 사용되는 데이터셋
'''
입력변수(x): 숫자(0~9) 필기페의 흑백 이미지
결과변수(y): 10진수 정수 - 이미지 정답
'''

X = digits.data#input data
y = digits.target #output data

X.shape #(1797, 64) -(size,pixel)
y.shape #(1797,)
y #array([0, 1, 2, ..., 8, 9, 8])

# 첫번째 image 추출
first_img=X[0]
first_img.shape# (64,)

#2. image reshape
#1d->2d
img=first_img.reshape(8,8) # 모양변경
img.shape#(8, 8)

#image 출력
plt.imshow(img,cmap='gray') #cmap='gray':흑백보기
plt.show()

y[0] # 첫 이미지 정답 - 0

#3. Newaxis:차원 추가
X.shape # (1797, 64)

#2d->3dsize: 수 변경 불가
X_3d=X.reshape(-1, 8, 8) # -1: 전체:image
X_3d.shape #(1797, 8, 8) : (size,h,w)

#3d->4d : (size,h,w,c) c=1:흑백,c=3컬러
X_4d=X_3d[:,:,:,np.newaxis] #4차원 위치: 축 추가
X_4d.shape #(1797, 8, 8, 1) : (size,h,w,c)

#마지막 이미지 show
plt.imshow(X_4d[-2],cmap='gray')
plt.show() #9

y[-2] #정답: 9
y[:10] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# image 행렬 시각화: 10개 이미지
fig = plt.figure(figsize=(15,8))

for i in np.arange(10):
    fig.add_subplot(2,5,i+1) # 격자 추가 (2행,5열,위치)
    plt.title(f'images:{y[i]}',size=20) # 제목
    plt.imshow(X_4d[i],cmap='gray')
    




























