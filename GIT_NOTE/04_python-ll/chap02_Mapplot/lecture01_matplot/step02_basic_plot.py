# -*- coding: utf-8 -*-
"""
step02_basic_plot.py

 - 기본 차트 그리기
"""
import numpy as np #별칭 -수치  data 생성
import matplotlib.pyplot as plt #별칭 -data 시각화

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'

# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

#1. 차트 자료 생성
data=np.arange(-3,7) # (start,stop)
print(data) #[-3 -2 -1  0  1  2  3  4  5  6]
len(data) # 10


# 2. 기본 차트 
plt.plot(data) # 기본: 선색:파랑, 스타일 :실선
plt.title('선색:파랑, 스타일 :실선')
plt.show()

help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1 #y데이터의 색인이 x 값이된다.
plot(y, 'r+')     # ditto, but with red plusses # 
'''

#3.색상:빨강, 선스타일 (+) 
plt.plot(data,'r+')
plt.title('선색:빨강, 스타일 :+')
plt.show()

#4. x,y축 선스타일 색상
data2 = np.random.randn(10)# y축 data 만들기
plt.plot(data,data2)
plt.show()

#5. color,maker사용
plt.plot(data,data2,'ro')# color+marker # r=빨강, o= 점
plt.show()

'''
'bo'->blue circle markers
'ro'->red circle markers
'r+'->red plusses markers
'''














































