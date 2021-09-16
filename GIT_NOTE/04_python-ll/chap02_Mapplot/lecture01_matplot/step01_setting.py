# -*- coding: utf-8 -*-
"""
step01_setting.py

 - matplotlib 사용법
 - 한글/음수 부호 처리방법
"""
import numpy as np #별칭 -수치  data 생성
import matplotlib.pyplot as plt #별칭 -data 시각화

#1. 차트 dataset 생성
data = np.random.randn(100) # 정규분포(평균:0,st:1) 난수 생성
print(data)


#2. 정규분포 시각화
plt.plot(data) #시각화(선 그래프)
plt.title('vaisulize the normal dist')
plt.xlabel('index')
plt.ylabel('random number')
plt.show() # 보이기 


#한글과 음수 부호 지원
# 차트에서 한글 지원 
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 한글 서체명-> 영문 서체명
path="C:\\Windows\\Fonts\\malgun.ttf"
import matplotlib.font_manager as fm
font_name=fm .FontProperties(fname=path).get_name()
print(font_name) # Malgun Gothic <- 이걸 위에 반영

#다른 서체명 (예시2)
path="C:\\Windows\\Fonts\\malgun.ttf"
import matplotlib.font_manager as fm
font_name=fm .FontProperties(fname=path).get_name()
print(font_name) 

# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

#3. 정규분포 시각화: 한글 적용
plt.plot(data) #시각화(선 그래프)
plt.title('정규분포 난수 시각화')
plt.xlabel('색인')
plt.ylabel('난수')
plt.show() # 보이기 



























































