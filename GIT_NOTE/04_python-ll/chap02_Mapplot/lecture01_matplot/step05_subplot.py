# -*- coding: utf-8 -*-
"""
step05_subplot.py

subplot차트 시각화

"""
import numpy as np #별칭 -수치  data 생성
import matplotlib.pyplot as plt #별칭 -data 시각화

#1. subolot생성
fig=plt.figure(figsize = (10,5)) # 차트 size 지정
x1=fig.add_subplot(2,2,1) # 2행 2열 1번 
x2=fig.add_subplot(2,2,2) # 2행 2열 2번 
x3=fig.add_subplot(2,2,3) # 2행 2열 3번 
x4=fig.add_subplot(2,2,4) # 2행 2열 4번 

#x1격자 차트 그리기
data1=np.random.randn(100)
data2=np.random.randint(1,100,100)
cdata=np.random.randint(1,4,100)

x1.hist(data1) #히스토 그램
x2.scatter(data1,data2,c=cdata) #산점도
x3.plot(data2) #기본차트
x4.plot(data1,data2,'g--') #기본차트 : 선 색과 스타일
plt.show()



