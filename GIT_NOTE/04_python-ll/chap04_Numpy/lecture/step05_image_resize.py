# -*- coding: utf-8 -*-
"""
step05_image_resize.py

imager reshape vs image resize
- imager reshape: 모양 변경,size 변경 불가
- image resize : picel 수를 변경
    ex) 500 x 300 x 3 -> 150 x 220 x 3
"""

import matplotlib.image as img #image read
import matplotlib.pyplot as plt # image show

# image file path
path ='C:/ITWILL/4_python-ll/workspace/chap04_Numpy/images'
file =path +'/test1.jpg'

#1. matplotlib 이용 imagre read/show
img_arr=img.imread(file)
type(img_arr) #numpy.ndarray
img_arr # pixel
'''       R    G     B
        [128, 113,  94],
        [127, 112,  93],
        [126, 111,  92]]], dtype=uint8) -> uint8-부호없는 int 데이터
        uint8: 2^8=256(0~255) 256개의 색상의 정보
'''
img_arr.shape #(360, 540, 3)-(h,w,color)
img_arr.size #583200=360x540x3
plt.imshow(img_arr)
plt.show()

# 2. PIL (python image library) 이용 image 크기 변경(resize)
from PIL import Image #Python Imaging Library
import numpy as np 

img=Image.open(file)
type(img) #PIL.JpegImagePlugin.JpegImageFile
np.shape(img) #(360, 540, 3) <- np가 아니니까 np.shape함수히용해서 사용

#image resize: 100,150
img_re = img.resize( (150,100) ) #(가로, 세로)
np.shape(img_re) #(100, 150, 3)

plt.imshow(img_re)
plt.show()

# PIL image -> numpy image 변환
type(img_re) #PIL.Image.Image
img_arr=np.asarray(img_re)
type(img_arr) #numpy.ndarray

img_arr.shape #(100, 150, 3)
img_arr.size #45000 
img_arr.max() # 255

img_arr.min() # 0

#3.전체 이미지 크기 규격화 
from glob import glob  # 파일 검색 패턴 사용(*.jpg,*.txt)

img_resize=[] # 이미지 데이터 저장
img_w=150;img_h=100 # 이미지 규격 

#glob(path+'/*jpg') <- 컴푸터에 서 특정 파일일 읽어(or검색)오기 위하여 사용하는 명려어
for file  in glob(path+'/*.jpg'): # path 에있는 모든(*) JPG파일은 가지고와서file 이라는 겍체에 넘긴다
    #print(file)
    img=Image.open(file)
    #image 크기 변경
    img_re = img.resize((img_w,img_h)) #(가로, 세로)
    #PIL -> numpy변환
    np.asarray(img_re)
    img_resize.append(img_arr)


print(img_resize)
type(img_resize) #list

# list-> numpy
img_resize_arr=np.array(img_resize)
img_resize_arr.shape 
#(2, 100, 150, 3) -> (size,h,w,color)

img_size=img_resize_arr.shape[0] #2

#image show
for i in range(img_size):
    plt.imshow(img_resize_arr[i])
    plt.show()




