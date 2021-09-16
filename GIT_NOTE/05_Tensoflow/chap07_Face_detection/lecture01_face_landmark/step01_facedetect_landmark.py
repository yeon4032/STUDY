# -*- coding: utf-8 -*-
"""
image 얼굴인식과 68 point landmark 인식 

1. Anaconda python 3.8 설치 : 가상환경(tensorflow)

단계1 : 패키지 설치 
(base) > conda activate tensorfow

(1) cmake 설치 : dlib 의존성 패키지 설치 
(tensorflow) >pip install cmake

(2) dlib 설치 : 68 랜드마크 인식(얼굴인식)
(tensorflow) >conda install -c conda-forge dlib
(tensorflow) >pip install dlib
   -> 프로그램 허용 알림 창 : 허용 
(3) scikit-image 설치 : image read/save
(tensorflow) >pip install scikit-image

단계2 : 68 포인트 랜드마크 data 다운로드 
(1) 다운로드 :http://dlib.net/files
    shape_predictor_68_face_landmarks.dat.bz2
    lecture01 압축풀기 
(2) images 폴더 제공 
(3) croped_images 폴더 생성 
"""

import dlib # face detection/face landmark
from skimage import io # image read/save
from glob import glob # dir 패턴검색(*jpg)

# 현재 경로 기준  
path = 'C:\\ITWILL\\5_Tensoflow\\workspace\\chap07_Face_detection\\lecture01_face_landmark'
fpath = path + "/images" # raw image 위치 
fpath2 = path + "/croped_images" # croped image 저장 위치

# 68 landmark 학습 data 
predictor ="shape_predictor_68_face_landmarks.dat"

# hog 얼굴 인식기(알고리즘)
face_detector = dlib.get_frontal_face_detector()
# 68 landmark 인식기 
face_68_landmark = dlib.shape_predictor(predictor)



i = 0
for file in glob(fpath+"/*.jpg") : # 한 명 얼굴 인식  
#for file in glob(path+"\\person.jpg"): # 여러명 얼굴인식(person.jpg파일) 하고프면 <- 이것만 바꾸면 된다.
    print('file :', file)
    image = io.imread(file)
    print(image.shape) # (928, 650, 3)
    
    # image 출력장 표시 
    win = dlib.image_window()
    win.set_image(image)
        
    detected = face_detector(image, 1)
    print('인식한 face size =', len(detected))
        
    i += 1
    for face in detected : # 한 명 얼굴 인식
    #for i, face in enumerate(detected) : # person.jpg   
        # 감지된 image 사각점 좌표 
        print(face) # [(141, 171) : 왼쪽 위  (409, 439) : 오른쪽 아래]
        
        print(f'왼쪽 : {face.left()}, 위 : {face.top()}, 오른쪽 : {face.right()}, 아래 : {face.bottom()}')
        # 왼쪽 : 141, 위 : 171, 오른쪽 : 409, 아래 : 439
        
        
        # 이미지 출력장에 face 사각점 좌표 겹치기 
        win.add_overlay(face)
        
        # 이미지 face 사각점안에 68 point 겹치기
        face_landmark = face_68_landmark(image, face)
        win.add_overlay(face_landmark)
        
        # 크롭(crop) : 얼굴 부분만 자르기 : image[h, w]
        crop = image[face.top():face.bottom(), face.left():face.right()]
        
        # croped image save
        io.imsave(fpath2 + "/croped"+str(i)+".jpg", crop)
























